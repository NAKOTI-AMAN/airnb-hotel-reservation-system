from databaseconn.database import session
from models.user import User
from validators.userRegistration import validate
import bcrypt 


class Users:
    def store_data(self,data):
        print(data)
        status=validate(data)
        if status[0]==True:
            password= bytes(data['password'],'utf-8')
            hashed_password=bcrypt.hashpw(password, bcrypt.gensalt())
            
            if 'user_type' in data:
                self.user=User(user_name=data['username'],email=data['email'],password=hashed_password,user_type=data['user_type'])

                session.add(self.user) 

                session.commit()
            else:
                self.user=User(user_name=data['username'],email=data['email'],password=hashed_password)
                session.add(self.user) 

                session.commit()
            return status[1]
        else:
            return status[1]