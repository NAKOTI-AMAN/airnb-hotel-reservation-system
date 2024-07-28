from databaseconn.database import session
from views.userTokens.userTokens import validate_Token
from models.review import Review
from models.listing import Listing


class SeeReviews:
    def show_reviews(self,data):
        response=[]

        if 'token' not in data or not data['token']:
             return {"token" : "token is required"}
        elif type(data['token'])!=str:
             return {"token" : "token is not in correct format"}
        
        if 'token' in data:
            token_status = validate_Token(data['token'])
            if token_status[0] == False:
                return {"token" : token_status[1]}
            
        if 'host_id' not in data and not data['host_id']:
            return{"host_id" : "host_id not found"}
        
        try:
            data['host_id'] =int(data['host_id'])
        except:
            return {"host_id" : "host_id not in correct format"}
            
        
        if 'place_id' not in data and not data['place_id']:
            return{"place_id" : "place_id not found"}
        
        try:
            data['place_id'] =int(data['place_id'])
        except:
            return {"place_id" : "place_id not in correct format"}
        
        place=session.query(Listing).filter(Listing.listing_id==data['place_id'],Listing.host_id==data['host_id']).first()
        
        if not place:
            return {"error": "No place found"}
        
        reviews=session.query(Review).filter(Review.guesthouse_id==place.listing_id).all()
        
        if not reviews:
            return {"error": "No reviews created yet"}
        
        for review in reviews:
            review_dict={
                    "guesthouse_id": review.guesthouse_id,
                    "customer_id": review.customer_id,
                    "booking_number": review.booking_number,
                    "review_date": review.review_date.strftime("%Y-%m-%d"),
                    "cleanliness": review.cleanliness,
                    "accuracy": review.accuracy,
                    "communication": review.communication,
                    "location": review.location,
                    "checkin": review.checkin,
                    "value_for_money": review.value_for_money
                }
            response.append(review_dict)
        
        return response
