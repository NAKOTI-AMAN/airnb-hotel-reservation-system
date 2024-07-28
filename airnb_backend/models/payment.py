from databaseconn.database import Base
from sqlalchemy import Column, Integer,String, ForeignKey,DateTime
from models.booking import Booking

class Payment(Base):
    __tablename__ = "payments"

    payment_id=Column("payment_id", Integer,autoincrement=True,primary_key=True)
    user_id=Column("user_id", Integer,nullable=False)
    booking_id=Column("booking_id", Integer,nullable=False)
    payment_date=Column("payment_date",DateTime,nullable=False)
    payment_amount=Column("payment_amount",Integer,nullable=False)
    payment_status=Column("payment_status",String,nullable=False)

    def __repr__(self):
        return f'''{{
        payment_id: {self.payment_id},
        user_id: {self.user_id},
        booking_id: {self.booking_id},
        payment_date: {self.payment_date},
        payment_amount: {self.payment_amount},
        payment_status: {self.payment_status}
        }}'''