from models.user import User
from models.listing import Listing
from views.userTokens.userTokens import validate_Token
from databaseconn.database import session

def validate(data):
    errors={}
    host_data=session.query(User).filter(User.id==data['host_id']).first()
    host_listing=session.query(Listing).filter(Listing.listing_id==data['listing_id'],Listing.host_id==data['host_id']).first()
    
    #host_id validations
    if 'host_id' not in data or not data['host_id']:
        errors['host_id'] ="Enter the host_id"
    elif type(data['host_id'])!=int:
        errors['host_id'] ="host_id is not in correct format"
    
    #password validations
    if 'password' not in data or not data['password']:
        errors['password'] ="Enter the password"
    elif type(data['password'])!=str:
        errors['password'] ="password is not in correct format"
    
    #listing_id validations
    if 'listing_id' not in data or not data['listing_id']:
        errors['listing_id'] ="Enter the listing_id"
    elif type(data['listing_id'])!=int:
        errors['listing_id'] ="listing_id is not in correct format"
    
    #validation for authentication of host
    if host_data:
        if host_data.password!=data['password']:
            errors['message']="Incorrect password"
    else:
        errors['message']="host_id does not exists"
    
    #validation for valid listing
    if not host_listing:
        errors['message']="listing does not exists"
    
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
    
    return [True, {"status": "Listing deleted successfully!!!"}]