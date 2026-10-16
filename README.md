# ParkMate 🚗  
## FastAPI Parking Reservation Web App

ParkMate is a full-stack parking reservation web application built with **FastAPI**. It allows users to list parking spaces, browse available spots, book parking, and manage reservations through a simple web dashboard.

This project demonstrates practical backend engineering skills including **authentication, database modeling, CRUD operations, booking logic, protected routes, and server-side rendering**.

---

## Features

- User registration and login
- Secure password hashing with bcrypt
- JWT authentication using HTTP-only cookies
- Add, view, and manage parking spots
- Search parking spots by city
- Filter spots by maximum hourly price
- Book available parking spots
- Cancel bookings
- Automatically update spot availability
- User dashboard for listings and reservations
- SQLite database with SQLAlchemy ORM

---

## Tech Stack

| Area | Technology |
|---|---|
| Backend | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Frontend | HTML, CSS, Jinja2 |
| Authentication | JWT |
| Password Security | bcrypt / passlib |
| Server | Uvicorn |
| Language | Python |

---

## Project Structure

```text
parkmate_fastapi_project_v2/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── auth_utils.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── spots.py
│   │   └── bookings.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── add_spot.html
│   │   ├── spots.html
│   │   └── bookings.html
│   │
│   └── static/
│       └── style.css
│
├── requirements.txt
└── README.md



## Demo Workflow

1. Register as a parking owner.
2. Add a parking spot.
3. Logout and register/login as another user.
4. Browse available parking spots.
5. Book a parking spot.
6. View or cancel the booking from the dashboard.

---

## Database Models

The app uses three main database tables:

- **Users** — stores account details, roles, and hashed passwords
- **Parking Spots** — stores parking listing details such as title, address, city, price, and availability
- **Bookings** — stores reservation details, booking hours, total price, and booking status

---

## Software Engineering Concepts Used

- FastAPI routing
- SQLAlchemy ORM
- SQLite database integration
- User authentication and protected routes
- JWT cookie-based session handling
- Password hashing with bcrypt
- CRUD operations
- Relational database design
- Server-side rendering with Jinja2
- Modular project structure
- Separation of concerns
- Basic marketplace-style business logic

---
## How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/parkmate-fastapi.git
cd parkmate-fastapi
```

### 2. Create and Activate Virtual Environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Application

```bash
uvicorn app.main:app --reload
```

### 5. Open in Browser

```text
http://127.0.0.1:8000
```
## Future Improvements

- Google Maps integration
- Distance-based parking search
- Stripe payment support
- Admin dashboard
- Email notifications
- Parking spot images
- User reviews and ratings
- PDF booking receipts
- Docker deployment
- Unit testing with Pytest
- PostgreSQL production setup
- Cloud deployment on Render, Railway, or AWS

---

Built **ParkMate**, a full-stack parking reservation web application using **FastAPI, SQLite, SQLAlchemy, Jinja2, JWT authentication, and bcrypt**, enabling users to list parking spots, search available spaces, book reservations, cancel bookings, and manage listings through a clean web dashboard.

---

## Author

**Revanth Reddy**  
Interested in Python, Backend Development, FastAPI, Data Engineering, Machine Learning, and AI-powered applications.

---

## License

This project is available for educational and portfolio purposes.
