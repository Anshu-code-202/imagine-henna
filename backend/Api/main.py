from fastapi import Depends, FastAPI
from backend.Api import database_models
from backend.Api.client_models import Booking

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session as DBSession


app = FastAPI(
    title="Imagine Henna API",
    description="Backend API for Mehendi Booking System",
    version="1.0.0"
)

engine = create_engine('postgresql://postgres:12345@localhost:5432/postgres')
SessionLocal = sessionmaker(bind=engine)
db_session = SessionLocal()

database_models.Base.metadata.create_all(bind=engine)

bookings = [
    Booking(
        id=1,
        customer_name="Priya",
        phone="9876543210",
        event_type="Wedding",
        booking_date="2026-06-20",
        mehendi_type="Bridal",
        price=5000,
        status="Confirmed"
    ),
    Booking(
        id=2,
        customer_name="Neha",
        phone="9876543211",
        event_type="Engagement",
        booking_date="2026-06-25",
        mehendi_type="Arabic",
        price=2000,
        status="Pending"
    )
]
def get_db(): # run endpoint
# So yield pauses the function and gives control to FastAPI.
# run code after yield #Used During API Requests:Provide a database session for each API request.
    db = db_session
    try:
        yield db
    finally:
        db.commit()


def init_db():#- Used Once at Startup
    db = db_session

    count = db.query(database_models.Booking).count()

    if count == 0:
        for booking in bookings:
            db.add(database_models.Booking(**booking.model_dump()))
        db.commit()


init_db()


"""Why Use yield in get_db but not init_db?
Because FastAPI's dependency system understands:

yield as:

Before yield → setup
After yield → cleanup"""

@app.get("/")
def greet():
    return "Hello welcome to Imagine Henna API"


@app.get("/bookings")
def get_all_bookings(db: DBSession = Depends(get_db)):
    db_bookings = db.query(database_models.Booking).all()
    return bookings


@app.get("/bookings/{id}")
def get_booking_by_id(id: int,db: DBSession = Depends(get_db)):
    db_bookings = db.query(database_models.Booking).filter(database_models.Booking.id == id).first()
    if db_bookings:
        return db_bookings

    return "Booking not found"


@app.post("/bookings")
def add_booking(booking: Booking,db: DBSession = Depends(get_db)):
    db.add(database_models.Booking(**booking.model_dump()))
    db.commit()
    return booking


@app.put("/bookings/{id}")
def update_booking(id: int, booking: Booking,db: DBSession = Depends(get_db)):
    db_bookings = db.query(database_models.Booking).filter(database_models.Booking.id == id).first()
    if db_bookings:
        db_bookings.customer_name=booking.customer_name
        db_bookings.booking_date=booking.booking_date
        db_bookings.event_type=booking.event_type
        db_bookings.id=booking.id
        db_bookings.mehendi_type=booking.mehendi_type
        db_bookings.price=booking.price
        db_bookings.status=booking.status
        db.commit()
        return "Booking updated"
    else:
        return "Booking not found"


@app.delete("/bookings/{id}")
def delete_booking(id: int,db: DBSession = Depends(get_db)):
    
    db_bookings = db.query(database_models.Booking).filter(database_models.Booking.id == id).first()
    if db_bookings:
        db.delete(db_bookings)
        db.commit()

    else:
        return "Booking not found"