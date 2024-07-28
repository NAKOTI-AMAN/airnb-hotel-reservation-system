from http.server import HTTPServer , BaseHTTPRequestHandler,SimpleHTTPRequestHandler
import json
import cgi
import os
import uuid
from views.users import Users
from views.listings import Listings
from views.logins import Logins
from views.bookings import Bookings
from views.approveBookings import ApproveBookings
from views.myListings import MyListings
from views.myBookings import MyBookings
from views.guestCancelBookings import GuestCancelBookings
from views.reviews import Reviews
from views.deleteListings import DeleteListings
from views.payments import Payments
from views.showAllListings import ShowAllListings
from views.seeReviews import SeeReviews
class AirnbServer(BaseHTTPRequestHandler):
    """
    A custom HTTP server for handling Airbnb-like services.

    Attributes:
        None
    """
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', 'http://127.0.0.1:5501')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Methods', 'GET, POST')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    def header_payload(self):
        """This function is used to extract the JSON data from the request body.
           It will return None if the request body is not valid JSON.
           If the request contains an authorization header, it will add the token to the data dictionary.
        """
        try:
            post_content=int(self.headers['Content-Length'])
            data=self.rfile.read(post_content).decode('utf-8')
            data_dict=json.loads(data)
            if self.authorization_header():
                data_dict['token'] = self.authorization_header()
            return data_dict
        except:
            return None

    def url_payload(self):
        """
        This function is used to extract the query parameters from the request URL.
        It will return a dictionary containing the query parameters. If the request contains an authorization header, it will add the token to the dictionary.

        Args:
            None

        Returns:
            A dictionary containing the query parameters, or None if the request URL does not contain any query parameters.

        Raises:
            None

        Example:
             >>> url_payload(request_object)
        {'param1': 'value1', 'param2': 'value2', 'token': 'auth_token'}
        """
        try:
            path_data=self.path.split("?")
            data_fields=path_data[1].split("&")
            data=dict(data_field.split("=") for data_field in data_fields)
            if self.authorization_header():
                data['token'] = self.authorization_header()
            return data
        except:
            return None
    
    def authorization_header(self):
        """
        This function is used to extract the authorization header from the request headers.
        It will return the token from the authorization header if it exists, otherwise it will return None.

        Args:
           None

        Returns:
           A string containing the token from the authorization header, or None if the header does not exist or is empty.

        Raises:
           None

        Example:
            >>> authorization_header(request_object)
            'auth_token'
        """
        try:
            auth_data=self.headers['Authorization']
            return auth_data
        except:
            return None
        

    def do_GET(self):
        """
        Handles GET requests to the server.

        Args:
           None

        Returns:
           None

        Raises:
           None

        Example:
            >>> do_GET(request_object)

        This function sends a 200 OK response with a Content-type header set to "application/json". It then checks if the URL payload contains any query parameters. If it does, it calls the appropriate method from the corresponding class based on the path. If the payload is empty, it sends a JSON response indicating that parameters were not found.
        """
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        print("GET request successful!!!")

        data=self.url_payload()
         
        if self.path.startswith("/API/V1/get-details"):
            if not data:
                self.wfile.write(json.dumps({"error":"parameters not found"}).encode())
            else:
                response = Logins()
                self.wfile.write(json.dumps(response.send_details(data)).encode())

        elif self.path.startswith ("/API/V1/my-listings"):
            """
            Retrieves listings associated with the user.

            Args:
              data (dict): JSON data containing user ID.

            Returns:
              str: JSON response containing the user's listings.

            Raises:
              None

            Example:
              >>> get_user_listings(data)
            """
            if not data:
                self.wfile.write(json.dumps({"error":"parameters not found"}).encode())
            
            else:
                response=MyListings()
                self.wfile.write(json.dumps(response.my_listings(data)).encode())
        
        elif self.path.startswith("/API/V1/my-bookings"):
            """
            Retrieves bookings associated with the user.

            Args:
              data (dict): JSON data containing user ID.

            Returns:
              str: JSON response containing the user's bookings.

            Raises:
             None

            Example:
              >>> get_user_bookings(data)
            """
            if not data:
                self.wfile.write(json.dumps({"error":"parameters not found"}).encode())
            
            else:
                response=MyBookings()
                self.wfile.write(json.dumps(response.my_bookings(data)).encode())

        elif self.path.startswith("/API/V1/show-all-listings"):
            """
            Retrieves all listings.

            Returns:
              str: JSON response containing all listings.

            Raises:
              None

            Example:
              >>> get_all_listings()
            """
            response=ShowAllListings()
            self.wfile.write(json.dumps(response.show_all()).encode())

        elif self.path.startswith("/API/V1/see-reviews"):
            """
            Retrieves reviews for a listing.

            Args:
              data (dict): JSON data containing listing ID.

            Returns:
              str: JSON response containing reviews for the listing.

            Raises:
              None

            Example:
              >>> get_listing_reviews(data)
            """
            if not data:
                self.wfile.write(json.dumps({"error":"parameters not found"}).encode())

            else:
                response=SeeReviews()
                self.wfile.write(json.dumps(response.show_reviews(data)).encode())
    def do_POST(self):
        """
        Handles POST requests to the server.

        Args:
           None

        Returns:
           None

        Raises:
           None

        Example:
           >>> do_POST(request_object)

        This function sends a 200 OK response with a Content-type header set to "application/json". It then checks if the payload contains any JSON data. If it does, it calls the appropriate method from the corresponding class based on the path. If the payload is empty, it sends a JSON response indicating that parameters were not found.
        """
        self.send_response(200)
        self.send_header("Content-type","application/json")
        self.end_headers()
        print("POST request successful!!!")

        
        if self.path=='/API/V1/register':
            """
            Registers a new user.
       
            Args:
               data (dict): JSON data containing user information.

            Returns:
               str: JSON response containing the user's ID and other details.

            Raises:
               None

            Example:
               >>> register_user(data)
            """
            data=self.header_payload()

            if not data:
               self.wfile.write(json.dumps({"error":"parameters not found"}).encode())    
            else:
               response=Users()
               self.wfile.write(json.dumps(response.store_data(data)).encode())
        
        elif self.path=="/API/V1/login":
            """
            Logs in a user.

            Args:
               data (dict): JSON data containing user credentials.

            Returns:
               str: JSON response containing the user's details.

            Raises:
               None

            Example:
               >>> login_user(data)
            """
            data=self.header_payload()

            if not data:
               self.wfile.write(json.dumps({"error":"parameters not found"}).encode())
            else:
               response=Logins()
               print(data)
               self.wfile.write(json.dumps(response.get_details(data)).encode())
        
        elif self.path=="/API/V1/create-listing":
            """
            Creates a new listing.

            Args:
               data (dict): JSON data containing listing information.

            Returns:
               str: JSON response containing the listing's ID and other details.

            Raises:
               None

            Example:
               >>> create_listing(data)
            """
            form=cgi.FieldStorage(fp=self.rfile,
                                  headers=self.headers,
                                  environ={'REQUEST_METHOD':'POST'})
            form_dict={}
            form_dict['host_id']=int(form['host_id'].value)
            form_dict['title']=form['title'].value
            form_dict['subtitle']=form['subtitle'].value
            form_dict['description']=form['description'].value
            form_dict['location']=form['location'].value
            form_dict['rate']=int(form['rate'].value)
            form_dict['day_discount']=int(form['dayDiscount'].value)
            form_dict['weekly_discount']=int(form['weekDiscount'].value)
            form_dict['cleaning_fee']=int(form['cleaningFee'].value)
            form_dict['service_fee']=int(form['serviceFee'].value)
            form_dict['occupancy']=int(form['occupancy'].value)
            form_dict['cancellation']=form['cancellation'].value
            form_dict['token']=self.headers['Authorization']
            
            image=form['images'].file.read()

            image_filename=str(uuid.uuid4())+'.jpg'
            image_path=os.path.join('resources', image_filename)
            os.makedirs('resources', exist_ok=True)
            
            with open(image_path,'wb') as f:
               f.write(image)
               
            print("successfully added image")
            form_dict['images']=image_path
            
            response=Listings()
            self.wfile.write(json.dumps(response.store_listing(form_dict)).encode())
        
        elif self.path=="/API/V1/book-place":
            """
            Books a place.

            Args:
               data (dict): JSON data containing booking information.

            Returns:
               str: JSON response containing the booking's ID and other details.

            Raises:
               None

            Example:
               >>> book_place(data)
            """
            data=self.header_payload()

            if not data:
               self.wfile.write(json.dumps({"error":"parameters not found"}).encode())
            else:
               response=Bookings()
               self.wfile.write(json.dumps(response.store_booking(data)).encode())

        elif self.path=='/API/V1/cancel-bookings':
            """
            Cancels a booking.

            Args:
               data (dict): JSON data containing booking information.

            Returns:
               str: JSON response indicating the success or failure of the cancellation.

            Raises:
               None
  
            Example:
               >>> cancel_bookings(data)
            """
            data=self.header_payload()

            if not data:
               self.wfile.write(json.dumps({"error":"parameters not found"}).encode())
            else:
               response=GuestCancelBookings()
               self.wfile.write(json.dumps(response.cancel_bookings(data)).encode())
        
        elif self.path=='/API/V1/create-review':
            """
            Creates a new review.

            Args:
               data (dict): JSON data containing review information.

            Returns:
               str: JSON response indicating the success or failure of the creation.
  
            Raises:
               None

            Example:
               >>> create_review(data)
            """
            data=self.header_payload()

            if not data:
               self.wfile.write(json.dumps({"error":"parameters not found"}).encode())
            else:
               response=Reviews()
               self.wfile.write(json.dumps(response.create_review(data)).encode())
        
        elif self.path=="/API/V1/payments":
            """
            Handles payments.

            Args:
               data (dict): JSON data containing payment information.

            Returns:
               str: JSON response indicating the success or failure of the payment.

            Raises:
               None

            Example:
               >>> handle_payments(data)
            """
            data=self.header_payload()

            if not data:
               self.wfile.write(json.dumps({"error":"parameters not found"}).encode())
            else:
               response=Payments()
               self.wfile.write(json.dumps(response.do_payment(data)).encode())

        elif self.path=="/API/V1/webhook":
            """
            Handles webhooks.

            Args:
               data (dict): JSON data containing webhook information.

            Returns:
               str: JSON response indicating the success or failure of the webhook processing.

            Raises:
               None

            Example:
               >>> handle_webhook(data)
            """
            data=self.header_payload()

            if not data:
               self.wfile.write(json.dumps({"error":"parameters not found"}).encode())
            else:
               response=Payments()
               self.wfile.write(json.dumps(response.webhook(data)).encode())
    def do_PUT(self):
        """
        Handles PUT requests to the server.

        Args:
           None

        Returns:
           None

        Raises:
           None

        Example:
           >>> do_PUT(request_object)

        This function sends a 200 OK response with a Content-type header set to "application/json". It then checks if the payload contains any JSON data. If it does, it calls the appropriate method from the corresponding class based on the path. If the payload is empty, it sends a JSON response indicating that parameters were not found.
        """
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        print("PUT request successfull!!!")

        data=self.header_payload()
        
        if not data:
            self.wfile.write(json.dumps({"error":"parameters not found"}).encode())
        
        elif self.path=='/API/V1/approve-booking':
            """
            Approves a booking.

            Args:
               data (dict): JSON data containing booking information.
     
            Returns:
              str: JSON response indicating the success or failure of the approval.

            Raises:
              None

            Example:
               >>> approve_booking(data)
           """
            response=ApproveBookings()
            self.wfile.write(json.dumps(response.approve(data)).encode())

    def do_DELETE(self):
        """
        Handles DELETE requests to the server.

        Args:
           None

        Returns:
           None

        Raises:
           None

        Example:
           >>> do_DELETE(request_object)

        This function sends a 200 OK response with a Content-Type header set to "application/json". It then checks if the payload contains any JSON data. If it does, it calls the appropriate method from the corresponding class based on the path. If the payload is empty, it sends a JSON response indicating that parameters were not found.
        """
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        print("DELETE request successful!!!")

        data=self.header_payload()

        if not data:
            self.wfile.write(json.dumps({"error":"parameters not found"}).encode())

        elif self.path == "/API/V1/delete-listing":
            """
            Deletes a listing.

            Args:
               data (dict): JSON data containing listing information.

            Returns:
               str: JSON response indicating the success or failure of the deletion.

            Raises:
               None

            Example:
               >>> delete_listing(data)
            """
            response=DeleteListings()
            self.wfile.write(json.dumps(response.delete_listing(data)).encode())

PORT=5500
HOST="0.0.0.0"
server=HTTPServer((HOST,PORT),AirnbServer)
print(f"Server running at {HOST}:{PORT}")
server.serve_forever()