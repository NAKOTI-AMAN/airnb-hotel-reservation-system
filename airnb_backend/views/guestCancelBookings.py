from databaseconn.database import session,Base,engine
from models.booking import Booking
from models.listing import Listing
from views.userTokens.userTokens import validate_Token

Base.metadata.create_all(bind=engine)

class GuestCancelBookings:
    def cancel_bookings(self,data):
        self.guestBooking=session.query(Booking).filter(Booking.booking_id==data['booking_id']).first()
        self.cancel_allowed=session.query(Listing).filter(Listing.listing_id==data['booking_id']).first()
        
        if 'token' not in data or not data['token']:
             return {"token" : "token is required"}
        elif type(data['token'])!=str:
             return {"token" : "token is not in correct format"}
        
        if 'token' in data:
            token_status = validate_Token(data['token'])
            if token_status[0] == False:
                return {"token" : token_status[1]}
        
        if self.guestBooking:
            if self.guestBooking.guest_id!=data['guest_id']:
                return {"message": "Invalid guest"}
            elif self.cancel_allowed.cancellation=="Allowed":
                if self.guestBooking.status=="Pending" and data['status']=="Cancelled":
                    self.guestBooking.status="Cancelled"
                    session.commit()
                    return {"message": "Booking cancelled"}
                elif self.guestBooking.status=="Cancelled":
                    return {"message": "Already cancelled"}
                else:
                    return {"message":"Can't cancel the booking"}
            else:
                return {"message":"Cancellation not allowed"}

        else:
            return {"message": "Booking does not exist"}