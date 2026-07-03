"""
Run this ONCE (locally or as a one-off Lambda/script) whenever you add new
reference images to Bucket 2. It builds/updates a Rekognition Collection —
a searchable index of faces — from every image in Bucket 2.

Usage:
    pip install boto3
    python setup_collection.py

(If you're on the same EC2 instance as your Flask app, activate the venv
first: source venv/bin/activate)
"""

import boto3

REGION = "ap-south-1"
COLLECTION_ID = "bucket2-collection"  # name of the Rekognition face collection
BUCKET2 = "known-faces123"            # your reference-images bucket

rekognition = boto3.client("rekognition", region_name=REGION)
s3 = boto3.client("s3", region_name=REGION)


def create_collection():
    try:
        rekognition.create_collection(CollectionId=COLLECTION_ID)
        print(f"Created collection: {COLLECTION_ID}")
    except rekognition.exceptions.ResourceAlreadyExistsException:
        print(f"Collection '{COLLECTION_ID}' already exists, reusing it.")


def index_bucket2_images():
    paginator = s3.get_paginator("list_objects_v2")
    indexed, skipped = 0, 0

    for page in paginator.paginate(Bucket=BUCKET2):
        for obj in page.get("Contents", []):
            key = obj["Key"]
            if key.endswith("/"):  # skip "folders"
                continue
            try:
                response = rekognition.index_faces(
                    CollectionId=COLLECTION_ID,
                    Image={"S3Object": {"Bucket": BUCKET2, "Name": key}},
                    ExternalImageId=key.replace("/", "_"),  # lets you map FaceId -> filename
                    DetectionAttributes=[],
                    MaxFaces=1,
                    QualityFilter="AUTO",
                )
                faces_found = len(response.get("FaceRecords", []))
                if faces_found:
                    indexed += 1
                    print(f"Indexed '{key}' ({faces_found} face found)")
                else:
                    skipped += 1
                    print(f"No face detected in '{key}', skipped")
            except Exception as e:
                skipped += 1
                print(f"Failed to index '{key}': {e}")

    print(f"\nDone. Indexed: {indexed}, Skipped: {skipped}")


if __name__ == "__main__":
    create_collection()
    index_bucket2_images()
