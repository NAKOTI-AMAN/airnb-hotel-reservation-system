from models.user import User
from models.listing import Listing
from databaseconn.database import session
from views.userTokens.userTokens import validate_Token
def validate(data):
    errors={}

    # host_id validations
    if 'host_id' not in data or not data['host_id']:
         errors['host_id']="Enter the id of host"
    elif type(data['host_id'])!=int:
         errors['host_id']="id is not is correct format"
    else:
         check_host=session.query(User).filter(User.id==data['host_id'],User.user_type=="Host").first()
         if not check_host:
              errors['host_id']="host does not exists"
         else:
              print(check_host)
    

    #title validations
    if 'title' not in data or not data['title']:
         errors['title']="title cannot be blank"
    elif type(data['title'])!=str:
         errors['title']="title is not is correct format"

    #subtitle validations
    if 'subtitle' not in data or not data['subtitle']:
         errors['subtitle']="subtitle cannot be blank"
    elif type(data['subtitle'])!=str:
         errors['subtitle']="subtitle is not is correct format"

    #description validations
    if 'description' not in data or not data['description']:
         errors['description']="Kindly enter a description"
    elif type(data['description'])!=str:
         errors['description']="description is not is correct format"
    
    #location validations
    if 'location' not in data or not data['location']:
         errors['location']="location cannot be blank"
    elif type(data['location'])!=str:
         errors['location']="location is not is correct format"
    
    #rate validations
    if 'rate' not in data or not data['rate']:
         errors['rate']="rate cannot be blank"
    elif type(data['rate'])!=int:
         errors['rate']="rate is not is correct format"

    #day_discount validations
    if 'day_discount' not in data or not data['day_discount']:
         errors['day_discount']="day_discount cannot be blank"
    elif type(data['day_discount'])!=int:
         errors['day_discount']="day_discount is not is correct format"

    #weekly_discount validations
    if 'weekly_discount' not in data or not data['weekly_discount']:
         errors['weekly_discount']="weekly_discount cannot be blank"
    elif type(data['weekly_discount'])!=int:
         errors['weekly_discount']="weekly_discount is not is correct format"
    elif data['weekly_discount']<data['day_discount']:
         errors['weekly_discount']="weekly_discount can't be less than day_discount"
    #cleaning_fee validations
    if 'cleaning_fee' not in data or not data['cleaning_fee']:
         errors['cleaning_fee']="cleaning_fee cannot be blank"
    elif type(data['cleaning_fee'])!=int:
         errors['cleaning_fee']="cleaning_fee is not is correct format"
    
    #service_fee validations
    if 'service_fee' not in data or not data['service_fee']:
         errors['service_fee']="service_fee cannot be blank"
    elif type(data['service_fee'])!=int:
         errors['service_fee']="service_fee is not is correct format"

    #image validations
    if 'images' not in data or not data['images']:
         errors['image']="image is required"
    

    #occupancy validations
    if 'occupancy' not in data or not data['occupancy']:
         errors['occupancy']="occupancy cannot be blank"
    elif type(data['occupancy'])!=int:
         errors['occupancy']="occupancy is not is correct format"

    #cancellation validations
    if 'cancellation' not in data or not data['cancellation']:
         errors['cancellation']="cancellation cannot be blank"
    elif type(data['cancellation'])!=str:
         errors['cancellation']="cancellation is not is correct format"
     
    #token validations
    if 'token' not in data or not data['token']:
         errors['token']="token is required"
    elif type(data['token'])!=str:
         errors['token']="token is not in correct format"
    
    if 'token' in data:
         token_status = validate_Token(data['token'])
         if token_status[0] == False:
              errors['token']=token_status[1]

    #number of listings one host can make validations
    places=session.query(Listing).filter(Listing.host_id==data['host_id']).all()
    if places:
         if len(places)>9:
              errors["listing"]="Listing creating capacity exceeded, you can try our premium service and become a superhost"
              

    if errors:
         return [False,errors]
    else:
         return [True,{  "status" : "Listing Created!!!" }]  