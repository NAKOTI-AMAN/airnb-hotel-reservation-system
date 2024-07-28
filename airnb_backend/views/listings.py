from databaseconn.database import session,Base,engine
from models.listing import Listing
from validators.hostListings import validate

Base.metadata.create_all(bind=engine)
class Listings:
    def store_listing(self,data):
        status=validate(data)
        if status[0]==True:
            self.user=Listing(host_id=data['host_id'],
                              title=data['title'],
                              subtitle=data['subtitle'],
                              description=data['description'],
                              location=data['location'],
                              rate=data['rate'],
                              day_discount=data['day_discount'],
                              weekly_discount=data['weekly_discount'],
                              cleaning_fee=data['cleaning_fee'],
                              service_fee=data['service_fee'],
                              images=data['images'],
                              occupancy=data['occupancy'],
                              cancellation=data['cancellation']
                              )

            session.add(self.user) 

            session.commit()
            return status[1]
        else:
            return status[1]
        