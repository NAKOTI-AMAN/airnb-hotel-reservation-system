from databaseconn.database import Base, engine, session
from models.user import User
import bcrypt
from views.userTokens.userTokens import generate_Token
from views.userTokens.userTokens import validate_Token

Base.metadata.create_all(bind=engine)

class Logins:
    def get_details(self,data):
        details=session.query(User).filter(User.email==data['email']).first()
        if details:
            password_bytes=bytes(data['password'],'utf-8')
            if bcrypt.checkpw(password_bytes,details.password):
                return {"status":"Login successful",
                        "token":generate_Token(data)}
            else:
                return {"status":"incorrect password"}
        
        else:
            return { "status" : "invalid email"}
        
    def send_details(self, data):
        status=validate_Token(bytes(data['token'],'utf-8'))
        if status[0]==True:
            mail=status[1]
            user_data=session.query(User).filter(User.email==mail['email']).first()
            user={"user_id":user_data.id,
                  "username":user_data.user_name,
                  "email":user_data.email,
                  "user_type":user_data.user_type}
            return user
        else:
            return status[1]