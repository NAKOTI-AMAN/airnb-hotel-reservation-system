from databaseconn.database import Base,engine,session
from models.review import Review
from validators.guestReviews import validate
from datetime import datetime

Base.metadata.create_all(bind=engine)

class Reviews:
    def create_review(self,data):
        status=validate(data)
        if status[0]==True:
            previous_review=session.query(Review).filter(Review.guesthouse_id==data['guesthouse_id'],Review.customer_id==data['customer_id'],Review.booking_number==data['booking_number']).first()
            if previous_review:
                previous_review.cleanliness=data['cleanliness']
                previous_review.accuracy=data['accuracy']
                previous_review.communication=data['communication']
                previous_review.location=data['location']
                previous_review.checkin=data['checkin']
                previous_review.value_for_money=data['value_for_money']
                
                session.commit()

            else:
                self.user=Review(guesthouse_id=data['guesthouse_id'],
                                 customer_id=data['customer_id'],
                                 booking_number=data['booking_number'],
                                 review_date=datetime.strptime(data['review_date'],"%Y-%m-%d"),
                                 cleanliness=data['cleanliness'],
                                 accuracy=data['accuracy'],
                                 communication=data['communication'],
                                 location=data['location'],
                                 checkin=data['checkin'],
                                 value_for_money=data['value_for_money'])
                
                session.add(self.user)
                session.commit()                
            
            return status[1]
        
        else:
            return status[1]

          