from databaseconn.database import Base
from sqlalchemy import Column,Integer,DateTime,ForeignKey
from models.booking import Booking


class Date(Base):
    __tablename__ ="dates"
    date_id=Column("date_id", Integer,autoincrement=True,primary_key=True)
    hotel_id=Column("hotel_id", Integer,ForeignKey(Booking.place_id),nullable=False)
    checkin_date=Column("checkin_date",DateTime,ForeignKey(Booking.check_in),nullable=False)
    checkout_date=Column("checkout_date",DateTime,ForeignKey(Booking.check_out),nullable=False)
    occupancy_left=Column("occupancy_left",Integer,nullable=False)

    def __repr__(self):
        return f'''{{
        date_id: {self.date_id},
        checkin_date: {self.checkin_date},
        checkout_date: {self.checkout_date},
        occupancy_left: {self.occupancy_left}
        }}'''