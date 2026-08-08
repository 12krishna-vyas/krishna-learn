# QR Code Generator (Django)

A Django-based web app to generate and manage QR codes, with user authentication. Containerized with Docker and deployed on AWS EC2.

## Features

- User signup and login
- Generate QR codes from user input
- View and manage generated QR codes
- Media storage for generated QR code images

## Tech stack

- Django (Python)
- qrcode + Pillow — QR code generation
- SQLite — database
- Docker — containerization
- AWS EC2 (Ubuntu) — hosting

## Project structure

```
qr_code/
├── Qr_Code_Project/     # Django project settings
├── myapp/                # Main app (views, models, forms)
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS)
├── media/                  # Generated QR code images
├── manage.py
├── requirements.txt
└── Dockerfile
```

## Running locally

```
git clone https://github.com/<your-username>/<your-repo>.git
cd qr_code
python -m venv venv
source venv/bin/activate      # venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

App runs at `http://127.0.0.1:8000`

## Running with Docker

Build the image:

```
docker build -t qr_code_app .
```

Run the container:

```
docker run -d -p 8000:8000 --name qr_container qr_code_app
```

Run migrations inside the container:

```
docker exec -it qr_container python manage.py migrate
```

App runs at `http://localhost:8000`

## Deployment

Deployed on an AWS EC2 (Ubuntu) instance:

1. Code copied to the server via `scp`
2. Docker installed on the instance
3. Image built and run as a container, exposing port 8000
4. Port 8000 opened in the EC2 security group

## Environment notes

- Database is set to SQLite by default (`db.sqlite3`) for simplicity. Update `DATABASES` in `settings.py` to use MySQL/Postgres for production.
- Update `ALLOWED_HOSTS` in `settings.py` with your actual domain or IP before deploying.

## License

This project is for learning and demonstration purposes.
