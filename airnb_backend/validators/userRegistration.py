from models.user import User
from databaseconn.database import session
from views.userTokens.userTokens import generate_Token
def validate(data):
    errors={}

    # username validations
    if 'username' not in data or not data['username']:
         errors['username']="Username cannot be blank"
    
    elif len(data['username'])<3 or len(data['username'])>10:
         errors['username']="Username cannot be less than 3 and more than 10 characters!"
      
    #email validations
    if 'email' not in data or not data['email']:
         errors['email']="Email cannot be blank"
    elif '@' not in data['email']:
         errors['email']="Invalid email"

    else:
         results=session.query(User).filter(User.email==data["email"])
         for result in results:
            print(result);
            if result:
                errors['email']="User already exists"
    
    #password validations
    if 'password' not in data or not data['password']:
         errors['password']="Kindly enter a password"
    elif len(data['password'])<8:
         errors['password']="Password length must be greater than 8"

    #user_type validations
    if 'user_type' in data and data['user_type'] not in ["Host","Guest"]:
         errors['user_type']="user_type should be either Guest or Host"

    if errors:
         return [False,errors]
    else:
         return [True,{  "status" : "Registration Successfull!!!" ,
                          "token" : generate_Token(data)}]  