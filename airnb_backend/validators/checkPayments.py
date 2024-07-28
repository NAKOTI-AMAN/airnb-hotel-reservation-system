from databaseconn.database import session
from views.userTokens.userTokens import validate_Token
from models.booking import Booking
from models.listing import Listing

def validate(data):

    errors={}

    #booking_id validations
    if "booking_id" not in data or not data['booking_id']:
         errors['booking_id'] ="Please enter a booking_id"
    elif type(data['booking_id'])!=int:
         errors['booking_id'] ="booking_id must be an integer"
    
    #booking_data validations
    try:
         booking_data = session.query(Booking).filter(Booking.booking_id==data['booking_id']).first()
    except:
         errors['message']="No such booking exists"
    try:
         place_data=session.query(Listing).filter(Listing.listing_id==booking_data.place_id).first()
    except:
         errors['message']="No such listing exists for corresponding booking_id" 

    if not booking_data:
         errors['booking_id']="Invalid booking_id"

    elif booking_data.status == "Booked":
         errors['status']="Payment already done"

    elif booking_data.status == "Cancelled":
         errors['status']="Booking was cancelled"
    
    #token validations
    if 'token' not in data or not data['token']:
         errors['token']="token is required"
    elif type(data['token'])!=str:
         errors['token']="token is not in correct format"
    
    if 'token' in data:
         token_status = validate_Token(data['token'])
         if token_status[0] == False:
              errors['token']=token_status[1]
    
    if errors:
         return [False, errors]

    return [True,{ 
         "place_title": place_data.title,
         "total_amount": booking_data.amount_sum
                  }]