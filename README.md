# ParkMate - FastAPI Parking Reservation Web App

ParkMate is a FastAPI-based parking reservation web application built for portfolio/demo purposes. It allows users to register, log in, list parking spots, reserve parking spots, manage bookings, and view dashboard data.

This version uses SQLite, so you do not need PostgreSQL, MySQL, Docker, or any external database software.

## Features

- User registration and login
- Password hashing with bcrypt
- JWT-based cookie authentication
- SQLite database
- Add parking spots
- View available parking spots
- Book parking spots
- Cancel bookings
- Owner dashboard
- User booking dashboard
- Clean HTML/CSS frontend using Jinja2 templates
- FastAPI backend with SQLAlchemy ORM

## How to Run

```bash
cd parkmate_fastapi_project_v2
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## Demo Flow

1. Register a new account.
2. Login.
3. Add a parking spot.
4. Go to Browse Parking.
5. Book a parking spot using a different user account.
6. View your bookings.
7. Cancel a booking if needed.

## Resume Bullet

Built ParkMate, a full-stack parking reservation web application using FastAPI, SQLite, SQLAlchemy, Jinja2, JWT authentication, and bcrypt password hashing, enabling users to list parking spots, search available spaces, create bookings, and manage reservations through a clean web dashboard.
