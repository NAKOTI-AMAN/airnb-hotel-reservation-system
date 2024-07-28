from models.user import User
from models.listing import Listing
from views.userTokens.userTokens import validate_Token
from databaseconn.database import session
from datetime import datetime


def validate(data):
    errors={}

    # guest_id validations
    if 'guest_id' not in data or not data['guest_id']:
         errors['guest_id']="Enter the id of guest"
    elif type(data['guest_id'])!=int:
         errors['guest_id']="id is not is correct format"
    else:
         check_guest=session.query(User).filter(User.id==data['guest_id'],User.user_type=="Guest").first()
         if not check_guest:
              errors['guest_id']="guest does not exists"
         else:
              print(check_guest)
    

    #place_id validations
    if 'place_id' not in data or not data['place_id']:
         errors['place_id']="place_id cannot be blank"
    elif type(data['place_id'])!=int:
         errors['place_id']="place_id is not is correct format"
    else:
         check_place=session.query(Listing).filter(Listing.listing_id==data['place_id'])
         if not check_place:
              errors['place_id']="Place does not exists"
         else:
              print(check_place)

    #check_in validations
    if 'check_in' not in data or not data['check_in']:
         errors['check_in']="check_in cannot be blank"
    else: 
         try:
              datetime.strptime(data['check_in'],"%Y-%m-%d")
         except:
              errors['check_in']="check_in date is not is correct format(yyyy-mm-dd)"
    
    #check_out validations
    if 'check_out' not in data or not data['check_out']:
         errors['check_out']="check_out cannot be blank"
    else: 
         try:
              datetime.strptime(data['check_out'],"%Y-%m-%d")
         except:
              errors['check_out']="check_out date is not is correct format(yyyy-mm-dd)"
    
    # date validateion
    if datetime.strptime(data['check_in'],"%Y-%m-%d")>datetime.strptime(data['check_out'],"%Y-%m-%d"):
         errors['date']="check_in date should not be greater than check_out date"

    #guests validations
    if 'guests' not in data or not data['guests']:
         errors['guests']="Kindly enter number of guests"
    elif type(data['guests'])!=int or data['guests']<=0:
         errors['guests']="number of guests is not is correct format"
    else:
         space=session.query(Listing).filter(Listing.listing_id==data['place_id']).first()
         if space and data['guests']>space.occupancy:
              errors['guests']="Number of guests is more than occupancy"

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
         return [False,errors]
    else:
         return [True,{  "status" : "Booking Created!!!" }]  