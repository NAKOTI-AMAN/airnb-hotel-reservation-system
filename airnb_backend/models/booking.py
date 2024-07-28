from databaseconn.database import Base,engine
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from models.user import User
from models.listing import Listing

class Booking(Base):
    __tablename__="bookings"

    booking_id=Column("booking_id",Integer,autoincrement=True,primary_key=True)
    guest_id=Column("guest_id",Integer,ForeignKey(User.id),nullable=False)
    place_id=Column("place_id",Integer,ForeignKey(Listing.listing_id),nullable=False)
    check_in=Column("check_in",DateTime,nullable=False)
    check_out=Column("check_out",DateTime,nullable=False)
    guests=Column("guests",Integer,nullable=False)
    amount_sum=Column("amount_sum",Integer,nullable=False)
    status=Column("status",String,default="Pending",nullable=False)

    def __repr__(self):
        return f'''{{
        booking_id= {self.booking_id},
        guest_id= {self.guest_id},
        place_id= {self.place_id},
        check_in= {self.check_in},
        check_out= {self.check_out},
        guests= {self.guests},
        amount_sum= {self.amount_sum},
        status= {self.status}
        }}'''