from databaseconn.database import Base
from sqlalchemy import Column,Integer,ForeignKey,DateTime
from models.booking import Booking

class Review(Base):
    
    __tablename__="reviews"

    review_id=Column("review_id",Integer,autoincrement=True,primary_key=True)
    guesthouse_id=Column("guesthouse_id",Integer,ForeignKey(Booking.place_id),nullable=False)
    customer_id=Column("customer_id",Integer,ForeignKey(Booking.guest_id),nullable=False)
    booking_number=Column("booking_number",Integer,ForeignKey(Booking.booking_id),nullable=False)
    review_date=Column("review_date",DateTime,nullable=False)
    cleanliness=Column("cleanliness", Integer,nullable=False)
    accuracy=Column("accuracy", Integer,nullable=False)
    communication=Column("communication", Integer,nullable=False)
    location=Column("location", Integer,nullable=False)
    checkin=Column("checkin", Integer,nullable=False)
    value_for_money=Column("value_for_money", Integer,nullable=False)

    def __repr__(self):
        return f'''{{
        review_id: {self.review_id},
        guesthouse_id: {self.guesthouse_id},
        customer_id: {self.customer_id},
        booking_number: {self.booking_number},
        review_date: {self.review_date},
        cleanliness: {self.cleanliness},
        accuracy: {self.accuracy},
        communication: {self.communication},
        location: {self.location},
        checkin: {self.checkin},
        value_for_money: {self.value_for_money}
        }}'''