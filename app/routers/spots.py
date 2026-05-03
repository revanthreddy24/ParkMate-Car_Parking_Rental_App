from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import ParkingSpot
from app.auth_utils import get_current_user_from_cookie

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/spots", response_class=HTMLResponse)
def view_spots(
    request: Request,
    city: str = "",
    max_price: str = "",
    db: Session = Depends(get_db)
):
    user = get_current_user_from_cookie(request, db)

    query = db.query(ParkingSpot).filter(ParkingSpot.is_available == True)

    if city:
        query = query.filter(ParkingSpot.city.ilike(f"%{city}%"))

    if max_price:
        try:
            query = query.filter(ParkingSpot.price_per_hour <= float(max_price))
        except ValueError:
            pass

    spots = query.order_by(ParkingSpot.created_at.desc()).all()

    return templates.TemplateResponse(
        "spots.html",
        {
            "request": request,
            "user": user,
            "spots": spots,
            "city": city,
            "max_price": max_price
        }
    )


@router.get("/spots/add", response_class=HTMLResponse)
def add_spot_page(request: Request, db: Session = Depends(get_db)):
    user = get_current_user_from_cookie(request, db)

    if not user:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Please login to add a parking spot.", "user": None}
        )

    return templates.TemplateResponse("add_spot.html", {"request": request, "user": user})


@router.post("/spots/add")
def add_spot(
    request: Request,
    title: str = Form(...),
    address: str = Form(...),
    city: str = Form(...),
    price_per_hour: float = Form(...),
    description: str = Form(""),
    db: Session = Depends(get_db)
):
    user = get_current_user_from_cookie(request, db)

    if not user:
        return RedirectResponse(url="/login", status_code=303)

    spot = ParkingSpot(
        title=title,
        address=address,
        city=city,
        price_per_hour=price_per_hour,
        description=description,
        owner_id=user.id,
        is_available=True
    )

    db.add(spot)
    db.commit()

    return RedirectResponse(url="/dashboard", status_code=303)


@router.post("/spots/{spot_id}/toggle")
def toggle_spot_availability(spot_id: int, request: Request, db: Session = Depends(get_db)):
    user = get_current_user_from_cookie(request, db)

    if not user:
        return RedirectResponse(url="/login", status_code=303)

    spot = db.query(ParkingSpot).filter(ParkingSpot.id == spot_id).first()

    if spot and spot.owner_id == user.id:
        spot.is_available = not spot.is_available
        db.commit()

    return RedirectResponse(url="/dashboard", status_code=303)


@router.post("/spots/{spot_id}/delete")
def delete_spot(spot_id: int, request: Request, db: Session = Depends(get_db)):
    user = get_current_user_from_cookie(request, db)

    if not user:
        return RedirectResponse(url="/login", status_code=303)

    spot = db.query(ParkingSpot).filter(ParkingSpot.id == spot_id).first()

    if spot and spot.owner_id == user.id:
        db.delete(spot)
        db.commit()

    return RedirectResponse(url="/dashboard", status_code=303)
