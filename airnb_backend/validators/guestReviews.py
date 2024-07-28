from databaseconn.database import session
from models.booking import Booking
from datetime import datetime
from views.userTokens.userTokens import validate_Token
def validate(data):
    errors={}
    place=session.query(Booking).filter(Booking.guest_id==data['customer_id'],Booking.place_id==data['guesthouse_id'],Booking.booking_id==data['booking_number']).first()
    
    #guesthouse_id validations
    if 'guesthouse_id' not in data or not data['guesthouse_id']:
        errors['guesthouse_id'] ="Enter the id of hotel"
    elif type(data['guesthouse_id'])!=int:
        errors['guesthouse_id'] = "Id not in correct format"
    
    #booking exist validation
    if not place:
        errors['message']="Booking does not exists"
    
    #customer_id validations
    if 'customer_id' not in data or not data['customer_id']:
        errors['customer_id']="Enter the id of guest"
    elif type(data['customer_id'])!=int:
        errors['customer_id']="Id not in correct format"

    #review_date validations
    if 'review_date' not in data or not data['review_date']:
        errors['review_date']="Enter the review_date"
    else:
        try:
            review_date=datetime.strptime(data['review_date'],"%Y-%m-%d")
        except:
            errors['review_date']="review_date is not is correct format(yyyy-mm-dd)"

    #cleanliness validations
    if 'cleanliness' not in data or not data['cleanliness']:
        errors['cleanliness']="Kindly rate this field out of 5"
    elif type(data['cleanliness'])!=int:
        errors['cleanliness']="rating not in correct format"
    elif data['cleanliness']>5:
        errors['cleanliness']="Maximum rating exceeded (must be between 1 and 5)"

    #accuracy validations
    if 'accuracy' not in data or not data['accuracy']:
        errors['accuracy']="Kindly rate this field out of 5"
    elif type(data['accuracy'])!=int:
        errors['accuracy']="rating not in correct format"
    elif data['accuracy']>5:
        errors['accuracy']="Maximum rating exceeded (must be between 1 and 5)"

    #communication validations
    if 'communication' not in data or not data['communication']:
        errors['communication']="Kindly rate this field out of 5"
    elif type(data['communication'])!=int:
        errors['communication']="rating not in correct format"
    elif data['communication']>5:
        errors['communication']="Maximum rating exceeded (must be between 1 and 5)"

    #location validations
    if 'location' not in data or not data['location']:
        errors['location']="Kindly rate this field out of 5"
    elif type(data['location'])!=int:
        errors['location']="rating not in correct format"
    elif data['location']>5:
        errors['location']="Maximum rating exceeded (must be between 1 and 5)"

    #checkin validations
    if 'checkin' not in data or not data['checkin']:
        errors['checkin']="Kindly rate this field out of 5"
    elif type(data['checkin'])!=int:
        errors['checkin']="rating not in correct format"
    elif data['checkin']>5:
        errors['checkin']="Maximum rating exceeded (must be between 1 and 5)"

    #value_for_money validations
    if 'value_for_money' not in data or not data['value_for_money']:
        errors['value_for_money']="Kindly rate this field out of 5"
    elif type(data['value_for_money'])!=int:
        errors['value_for_money']="rating not in correct format"
    elif data['value_for_money']>5:
        errors['value_for_money']="Maximum rating exceeded (must be between 1 and 5)"
    
    #validation for whether guest can create review
    if place and place.status == "Booked":
        if place and review_date >= place.check_in and review_date <= place.check_out:
            errors['message']="Can't leave a review during stay duration"
        elif place and review_date <= place.check_in:
            errors['message']="Can't leave a review before visit date"
    
    elif place and place.status=="Cancelled":
        errors['message']="Your booking was cancelled, can't leave a review"

    elif place and place.status=="Pending":
        errors['message']="Can't leave a review unless booking is approved by the host"

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
    
    return [True,{  "status" : "Review created!!!" }]