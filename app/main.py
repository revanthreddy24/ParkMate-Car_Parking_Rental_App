from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import ParkingSpot, Booking
from app.auth_utils import get_current_user_from_cookie
from app.routers import auth, spots, bookings

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ParkMate",
    description="FastAPI Parking Reservation Web Application",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

app.include_router(auth.router)
app.include_router(spots.router)
app.include_router(bookings.router)


@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    user = get_current_user_from_cookie(request, db)

    total_spots = db.query(ParkingSpot).count()
    available_spots = db.query(ParkingSpot).filter(ParkingSpot.is_available == True).count()
    total_bookings = db.query(Booking).count()

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "user": user,
            "total_spots": total_spots,
            "available_spots": available_spots,
            "total_bookings": total_bookings
        }
    )


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    user = get_current_user_from_cookie(request, db)

    if not user:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Please login to view your dashboard.", "user": None}
        )

    my_spots = db.query(ParkingSpot).filter(ParkingSpot.owner_id == user.id).all()
    my_bookings = db.query(Booking).filter(Booking.user_id == user.id).all()

    owner_booking_count = 0
    for spot in my_spots:
        owner_booking_count += len(spot.bookings)

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "user": user,
            "my_spots": my_spots,
            "my_bookings": my_bookings,
            "owner_booking_count": owner_booking_count
        }
    )
