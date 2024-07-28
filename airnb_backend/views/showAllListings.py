from databaseconn.database import session
from models.listing import Listing
from models.user import User


class ShowAllListings:

    def show_all(self):
        response=[]
        all_listings=session.query(Listing).all()

        if all_listings:
            for listing in all_listings:
                listing={
                    "listing_id": listing.listing_id,
                    "title": listing.title,
                    "subtitle": listing.subtitle,
                    "image": listing.images,
                    "description": listing.description,
                    "location": listing.location,
                    "rate": listing.rate,
                    "day_discount": listing.day_discount,
                    "weekly_discount": listing.weekly_discount,
                    "cleaning_fee": listing.cleaning_fee,
                    "service_fee": listing.service_fee,
                    "occupancy": listing.occupancy,
                    "Cancellation": listing.cancellation
                }
                response.append(listing)
            return response
        
        return {"message":"Sorry there are currently no listings"}