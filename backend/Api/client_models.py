from unittest.mock import Base

from pydantic import BaseModel

class Booking(BaseModel):
    customer_name: str
    phone: str
    event_type: str
    booking_date: str
    mehendi_type: str
    price: int
    status: str

    #if basemodel then no need to write init method because it is already defined in basemodel and it will automatically create init method for us and we can directly create object of client class without writing init method