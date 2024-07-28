from databaseconn.database import session
from models.listing import Listing
from views.userTokens.userTokens import validate_Token


class MyListings:
    def my_listings(self,data):
        response=[]

        if 'token' not in data or not data['token']:
             return {"token" : "token is required"}
        elif type(data['token'])!=str:
             return {"token" : "token is not in correct format"}
        
        if 'token' in data:
            token_status = validate_Token(data['token'])
            if token_status[0] == False:
                return {"token" : token_status[1]}


        try:
            self.listings=session.query(Listing).filter(Listing.host_id==data['host_id']).all()
        except:
            return {"message":"host_id not found"}
        if self.listings:
            for listing in self.listings:
                lists={
                    "listing_id": listing.listing_id,
                    "title": listing.title,
                    "subtitle": listing.subtitle,
                    "description": listing.description,
                    "location": listing.location,
                    "rate": listing.rate,
                    "day_discount": listing.day_discount,
                    "weekly_discount": listing.weekly_discount,
                    "cleaning_fee": listing.cleaning_fee,
                    "service_fee": listing.service_fee,
                    "occupancy": listing.occupancy,
                    "Cancellation": listing.cancellation,
                    "images":listing.images
                }
                response.append(lists)
            return response
        else:
            return {"message" : "Invalid host"}