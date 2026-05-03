from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import ParkingSpot, Booking
from app.auth_utils import get_current_user_from_cookie

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.post("/book/{spot_id}")
def book_spot(
    spot_id: int,
    request: Request,
    hours: int = Form(...),
    db: Session = Depends(get_db)
):
    user = get_current_user_from_cookie(request, db)

    if not user:
        return RedirectResponse(url="/login", status_code=303)

    spot = db.query(ParkingSpot).filter(ParkingSpot.id == spot_id).first()

    if not spot or not spot.is_available:
        return RedirectResponse(url="/spots", status_code=303)

    if spot.owner_id == user.id:
        return RedirectResponse(url="/spots", status_code=303)

    total_price = spot.price_per_hour * hours

    booking = Booking(
        user_id=user.id,
        parking_spot_id=spot.id,
        hours=hours,
        total_price=total_price,
        status="confirmed"
    )

    spot.is_available = False

    db.add(booking)
    db.commit()

    return RedirectResponse(url="/bookings", status_code=303)


@router.get("/bookings", response_class=HTMLResponse)
def my_bookings(request: Request, db: Session = Depends(get_db)):
    user = get_current_user_from_cookie(request, db)

    if not user:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Please login to view bookings.", "user": None}
        )

    bookings = db.query(Booking).filter(Booking.user_id == user.id).order_by(Booking.created_at.desc()).all()

    return templates.TemplateResponse(
        "bookings.html",
        {"request": request, "user": user, "bookings": bookings}
    )


@router.post("/bookings/{booking_id}/cancel")
def cancel_booking(booking_id: int, request: Request, db: Session = Depends(get_db)):
    user = get_current_user_from_cookie(request, db)

    if not user:
        return RedirectResponse(url="/login", status_code=303)

    booking = db.query(Booking).filter(Booking.id == booking_id, Booking.user_id == user.id).first()

    if booking and booking.status == "confirmed":
        booking.status = "cancelled"

        spot = db.query(ParkingSpot).filter(ParkingSpot.id == booking.parking_spot_id).first()
        if spot:
            spot.is_available = True

        db.commit()

    return RedirectResponse(url="/bookings", status_code=303)
