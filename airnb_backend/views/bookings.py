from databaseconn.database import session,Base,engine
from models.booking import Booking
from models.listing import Listing
from models.date import Date
from validators.placeBooking import validate
from datetime import datetime

Base.metadata.create_all(bind=engine)

class Bookings:
    def store_booking(self,data):
        status=validate(data)
        if status[0]==True:
            listing_data=session.query(Listing).filter(Listing.listing_id==data['place_id']).first()
            checkin_date=datetime.strptime(data['check_in'],'%Y-%m-%d')
            checkout_date=datetime.strptime(data['check_out'],'%Y-%m-%d')
            booked_days=(checkout_date-checkin_date).days
            if (booked_days+1)>7:
                rate_week_discount=(listing_data.rate*(booked_days+1))+listing_data.cleaning_fee+listing_data.service_fee-listing_data.weekly_discount
                
                self.user=Booking(guest_id=data['guest_id'],
                              place_id=data['place_id'],
                              check_in=checkin_date,
                              check_out=checkout_date,
                              guests=data['guests'],
                              amount_sum=(rate_week_discount + (0.2*rate_week_discount))*data['guests']
                              )
            else:
                rate_day_discount=(listing_data.rate*(booked_days+1))+(listing_data.cleaning_fee)+(listing_data.service_fee)-(listing_data.day_discount)
                
                self.user=Booking(guest_id=data['guest_id'],
                              place_id=data['place_id'],
                              check_in=checkin_date,
                              check_out=checkout_date,
                              guests=data['guests'],
                              amount_sum=(rate_day_discount + (0.2*rate_day_discount))*data['guests']
                              )

            
            session.add(self.user)
            session.commit()

            total=session.query(Booking).filter(Booking.place_id==data['place_id']).all()
            total.reverse()
            response={**status[1],"booking_id":self.user.booking_id,**{"total_amount": total[0].amount_sum}}
            
            dates=session.query(Date).filter(Date.hotel_id==data['place_id']).all()
            if not dates:
                place=session.query(Listing).filter(Listing.listing_id==data['place_id']).first()
                self.date_entry=Date(hotel_id=data['place_id'],checkin_date=checkin_date,checkout_date=checkout_date,occupancy_left=place.occupancy-data['guests'])
                session.add(self.date_entry)
                session.commit()
            else:
                dates.reverse()
                if dates[0].checkin_date<=checkin_date and dates[0].checkout_date>=checkout_date:
                    if data['guests']<=dates[0].occupancy_left:
                        self.date_entry=Date(hotel_id=data['place_id'],checkin_date=checkin_date,checkout_date=checkout_date,occupancy_left=dates[0].occupancy_left-data['guests'])
                        session.add(self.date_entry)
                        session.commit()
                    else:
                        return {"status": "Place is fully occupied"}
                
                elif dates[-1].checkout_date<checkin_date and dates[-1].checkout_date<checkout_date:
                    place=session.query(Listing).filter(Listing.listing_id==data['place_id']).first()
                    self.date_entry=Date(hotel_id=data['place_id'],checkin_date=checkin_date,checkout_date=checkout_date,occupancy_left=place.occupancy-data['guests'])
                    session.add(self.date_entry)
                    session.commit()
            

            return response
        
        else:
            return status[1]