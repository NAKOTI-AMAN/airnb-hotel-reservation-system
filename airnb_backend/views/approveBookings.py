from databaseconn.database import Base,engine,session
from models.booking import Booking
from models.listing import Listing
from views.userTokens.userTokens import validate_Token

Base.metadata.create_all(bind=engine)

class ApproveBookings:
    def approve(self,data):
        self.booking=session.query(Booking).filter(Booking.booking_id == data['booking_id']).first()
        
        if 'token' not in data or not data['token']:
             return {"token" : "token is required"}
        elif type(data['token'])!=str:
             return {"token" : "token is not in correct format"}
        
        if 'token' in data:
            token_status = validate_Token(data['token'])
            if token_status[0] == False:
                return {"token" : token_status[1]}
        
        if self.booking:
            self.user=session.query(Listing).filter(Listing.listing_id==self.booking.place_id).first()
        
        else:
            return {"message": "Booking not found"}
        
        if self.user and self.user.host_id==data['host_id']:

            if self.booking and self.booking.status=="Pending":
                
                if data['status']=="Booked":
                    self.booking.status=data['status']
                    session.commit()
                    return {"message":"Booking approved", "status":data['status']}
                
                elif data['status']=="Cancelled":
                    self.booking.status=data['status']
                    session.commit()
                    return {"message":"Booking Cancelled", "status":data['status']}
            
            elif self.booking and self.booking.status=="Cancelled":
                return {"message": "Already cancelled"}
            
            else:
                return {"message": "Already approved"}
        
        else:
            return {"message" : "Host not found"}