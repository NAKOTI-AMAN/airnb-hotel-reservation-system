from databaseconn.database import session
from models.booking import Booking
from models.listing import Listing
from views.userTokens.userTokens import validate_Token

class MyBookings:
    def my_bookings(self,data):
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
            self.bookings=session.query(Booking).filter(Booking.guest_id==data['guest_id']).all()
        except:
            return {"message":"guest_id not found"}
        if self.bookings:
            for booking in self.bookings:
                listing=session.query(Listing).filter(Listing.listing_id==booking.place_id).first()
                booking={
                    "booking_id" : booking.booking_id,
                    "guest_id" : booking.guest_id,
                    "place_title" : listing.title,
                    "check_in" : booking.check_in.strftime("%Y-%m-%d"),
                    "check_out" : booking.check_out.strftime("%Y-%m-%d"),
                    "guests" : booking.guests,
                    "amount_sum" : booking.amount_sum,
                    "status" : booking.status
                }
                response.append(booking)
            return response
        else:
            return {"message" : "Invalid guest"}