from databaseconn.database import Base,engine,session
from models.payment import Payment
from models.booking import Booking
from models.user import User
from validators.checkPayments import validate
from views.userTokens.userTokens import validate_Token
import stripe
from datetime import datetime
import pytz

Base.metadata.create_all(bind=engine)

stripe.api_key="sk_test_51P92pUSErSrXvWzdLuqLggBXbQr5H1FOvHkTtiyzhllG6s2U1Z9xEmEKYU3DCx49WmTwsbsbvOseweIjnCQrOF4o008TeWRC6v"

class Payments:
    def do_payment(self,data):
        status= validate(data)
        if status[0]==True:
            detail=status[1]
            place_details=stripe.Product.create(
                name= detail['place_title'],
            )
            stay_amount=stripe.Price.create(
                unit_amount=(detail['total_amount'])*100,
                currency='inr',
                product=place_details['id']
            )
            payment_gateway=stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        'price': stay_amount.id,
                        'quantity':1
                    }
                ],
               
                metadata=data,
                mode='payment',
                success_url="https://support.arbor-education.com/hc/article_attachments/360043573953",
                cancel_url="https://miro.medium.com/v2/resize:fit:810/1*OkeqV425CNZUQT2HSkTnJA.png"
            )
            print(payment_gateway.url,"hello world")
            return {
                "status": "Payment link proceeded",
                "payment_url":payment_gateway.url 
                    }
        
        elif status[0]==False:

            return status[1]
    
    def webhook(self,data):
        
        if data['type']=="checkout.session.completed" and data['data']['object']['payment_status']=="paid":
            india_timezone=pytz.timezone('Asia/Kolkata')
            india_time=datetime.now(india_timezone)
      
            
            try:
                payload=validate_Token(data['data']['object']['metadata']['token'])[1]
                user=session.query(User).filter(User.email==payload['email']).first()
                self.payment=Payment(user_id=user.id,
                                 booking_id=int(data['data']['object']['metadata']['booking_id']),
                                 payment_date=india_time,
                                 payment_amount=int(data['data']['object']['amount_total']/100),
                                 payment_status=data['data']['object']['payment_status'])
                
                session.add(self.payment)
                self.booking=session.query(Booking).filter(Booking.booking_id==int(data['data']['object']['metadata']['booking_id'])).first()
                self.booking.status="Booked"
                session.commit()
            
                return {"status": "Payment successful"}
            except:
                return {"error": "Payment failed"}
