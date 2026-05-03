# ParkMate 🚗  
## FastAPI-Based Parking Space Reservation Web Application

ParkMate is a full-stack web application built with **FastAPI** that allows users to list, browse, and reserve parking spaces through a simple and secure web interface. The project demonstrates practical backend engineering concepts including authentication, database design, CRUD operations, booking workflows, session handling, and server-side rendering.

This project was developed as a portfolio-ready software engineering project to showcase real-world web application development using **Python, FastAPI, SQLite, SQLAlchemy, Jinja2, JWT authentication, and secure password hashing**.

---

## 📌 Project Overview

Finding parking in busy areas can be time-consuming and frustrating. At the same time, many private parking spaces remain unused. ParkMate solves this problem by creating a simple platform where parking owners can list their available spaces and drivers can search, reserve, and manage parking bookings from one dashboard.

The application simulates a real-world parking marketplace system with practical business logic, relational database design, secure authentication, protected routes, and user-specific dashboards.

---

## 🚀 Key Features

## User Authentication

- User registration
- User login
- Secure password hashing using bcrypt
- JWT-based authentication stored in HTTP-only cookies
- Logout functionality
- Protected pages for logged-in users

## Parking Spot Management

- Add a new parking spot
- View listed parking spaces
- Store parking details such as title, address, city, price, and description
- Toggle parking spot availability
- Delete owned parking spots
- Prevent users from managing spots they do not own

## Booking System

- Browse available parking spots
- Search parking spots by city
- Filter parking spots by maximum hourly price
- Book a parking spot for selected hours
- Automatically mark booked spots as unavailable
- Cancel existing bookings
- Restore spot availability after cancellation
- Prevent users from booking their own listings

## Dashboard

- View user-specific parking spots
- View personal booking history
- Track number of bookings on owned parking spots
- Manage parking listings from one place
- Display useful booking and listing statistics

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Frontend Rendering | Jinja2 Templates |
| Styling | HTML, CSS |
| Authentication | JWT |
| Password Security | bcrypt / passlib |
| Server | Uvicorn |
| Language | Python |

---

## 🧱 System Architecture

User Browser  
↓  
FastAPI Application  
↓  
Authentication Router / Parking Spot Router / Booking Router  
↓  
SQLAlchemy ORM  
↓  
SQLite Database  

The application follows a modular architecture where routes, database models, authentication utilities, templates, and static files are separated for better maintainability and scalability.

---

## 📁 Project Structure

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

---

## 🗄️ Database Design

## Users Table

Stores registered user information.

- id
- full_name
- email
- hashed_password
- role
- created_at

## Parking Spots Table

Stores parking spot listing details.

- id
- title
- address
- city
- price_per_hour
- description
- is_available
- owner_id
- created_at

## Bookings Table

Stores reservation details.

- id
- user_id
- parking_spot_id
- hours
- total_price
- status
- created_at

---

## 🔐 Authentication Flow

1. User registers with name, email, password, and role.
2. Password is hashed using bcrypt before storing in the database.
3. During login, the entered password is verified against the stored hashed password.
4. A JWT token is generated after successful authentication.
5. The token is stored in an HTTP-only cookie.
6. Protected pages check the cookie to identify the logged-in user.
7. Users can log out, which removes the authentication cookie.

---

## ⚙️ How to Run Locally

## 1. Clone the Repository

Replace `your-username` with your GitHub username.

git clone https://github.com/your-username/parkmate-fastapi.git  
cd parkmate-fastapi  

## 2. Create a Virtual Environment

For Windows:

python -m venv venv  
venv\Scripts\activate  

For macOS/Linux:

python3 -m venv venv  
source venv/bin/activate  

## 3. Install Dependencies

pip install -r requirements.txt  

## 4. Run the Application

uvicorn app.main:app --reload  

## 5. Open in Browser

http://127.0.0.1:8000  

---

## 🧪 Demo Workflow

1. Register as a parking owner.
2. Add a parking spot from the dashboard.
3. Logout.
4. Register or login as a different user.
5. Browse available parking spots.
6. Book a parking space.
7. View the booking in the user dashboard.
8. Cancel the booking if needed.

---

## 📸 Application Pages

- Home Page
- Register Page
- Login Page
- Dashboard
- Add Parking Spot Page
- Browse Parking Page
- My Bookings Page

---

## ✅ Software Engineering Concepts Demonstrated

This project demonstrates:

- RESTful web application design
- Backend routing with FastAPI
- Database modeling with SQLAlchemy
- One-to-many database relationships
- Authentication and authorization
- Password hashing and credential security
- JWT cookie-based session management
- CRUD operations
- Business logic implementation
- Server-side rendering with Jinja2
- Modular project structure
- Separation of concerns
- SQLite-based local persistence

---

## 🎯 Business Use Case

ParkMate represents a simplified parking reservation marketplace. The platform can be extended into a production-ready application for:

- Stadium parking
- University campus parking
- Apartment parking rentals
- Event parking reservations
- Downtown private parking spaces
- Airport parking management

---

## 🔮 Future Enhancements

Planned improvements include:

- Google Maps integration
- Distance-based parking search
- Stripe payment integration
- Admin dashboard
- Email notifications
- Parking spot image uploads
- User reviews and ratings
- PDF booking receipts
- PostgreSQL production database
- Docker deployment
- Unit testing with Pytest
- CI/CD pipeline using GitHub Actions
- Cloud deployment on Render, Railway, or AWS

---

## 📌 Portfolio Highlight

ParkMate is designed to demonstrate practical software engineering ability beyond a basic CRUD application. It includes authentication, database relationships, booking logic, state updates, protected routes, user-specific dashboards, and real-world marketplace functionality.

This makes it a strong portfolio project for roles such as:

- Python Developer
- Backend Developer
- FastAPI Developer
- Software Engineer
- Full-Stack Developer
- Web Application Developer

---

## 🧾 Resume Bullet

Built **ParkMate**, a full-stack parking reservation web application using **FastAPI, SQLite, SQLAlchemy, Jinja2, JWT authentication, and bcrypt password hashing**, enabling users to list parking spots, search available spaces, create bookings, cancel reservations, and manage listings through a clean web dashboard.

---

## 👨‍💻 Author

**Revanth Reddy**  
Master’s Student in Computer Science  
Focused on Python, Backend Development, FastAPI, Data Engineering, Machine Learning, and AI-powered applications.

---

## 📄 License

This project is open-source and available for educational and portfolio purposes.
