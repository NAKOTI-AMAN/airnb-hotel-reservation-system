from databaseconn.database import Base,session,engine
from models.listing import Listing
from validators.removeListings import validate

Base.metadata.create_all(bind=engine)

class DeleteListings:
    def delete_listing(self,data):
        status=validate(data)

        if status[0]==True:
            self.listing=session.query(Listing).filter(Listing.listing_id==data['listing_id']).first()
            
            session.delete(self.listing)
            session.commit()
            
            return status[1]
        
        else:
            return status[1]