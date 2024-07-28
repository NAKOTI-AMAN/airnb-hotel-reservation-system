from databaseconn.database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,JSON
from models.user import User

class Listing(Base):
    __tablename__="listings"

    listing_id=Column("listing_id",Integer,autoincrement=True,primary_key=True)
    host_id=Column("host_id",Integer,ForeignKey(User.id))
    title=Column("title",String,nullable=False)
    subtitle=Column("subtitle",String)
    description=Column("description",String,nullable=False)
    location=Column("location",String,nullable=False)
    rate=Column("rate",Integer)
    day_discount=Column("day_discount",Integer,nullable=False)
    weekly_discount=Column("weekly_discount",Integer,nullable=False)
    cleaning_fee=Column("cleaning_fee",Integer,nullable=False)
    service_fee=Column("service_fee",Integer,nullable=False)
    images=Column("images",JSON,nullable=False)
    occupancy=Column("occupancy",Integer,nullable=False)
    cancellation=Column("cancellation",String,default="Not Allowed",nullable=False)
    def __repr__(self):
        return (f'''{{
                listing_id : {self.listing_id},
                host_id : {self.host_id},
                title : {self.title},
                subtitle : {self.subtitle},
                description : {self.description},
                location : {self.location},
                rate : {self.rate},
                day_discount : {self.day_discount},
                weekly_discount : {self.weekly_discount},
                cleaning_fee : {self.cleaning_fee},
                service_fee : {self.service_fee}
                images : {self.images},
                occupancy : {self.occupancy},
                cancellation : {self.cancellation}
                }}''')
