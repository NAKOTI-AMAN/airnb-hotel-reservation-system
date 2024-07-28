from databaseconn.database import session
import jwt
from models.user import User
from datetime import datetime,timedelta,timezone

SECRET_KEY = "Hello_World"
def generate_Token(data):
    now=datetime.now(timezone.utc)
    payload = {
        "email": data['email'],
        "iat": now.timestamp(),
        "exp": (now + timedelta(hours=1)).timestamp()
    }
    token=jwt.encode(payload=payload,key=SECRET_KEY,algorithm='HS256')
    return token

def verify_token(data):
    user_check=session.query(User).filter(User.email==data).first()
    if user_check:
        return True
    else:
        return False
def validate_Token(data):
    token=data
    try:
        unverified_headers=jwt.get_unverified_header(token)
        payload=jwt.decode(token,key=SECRET_KEY,algorithms=unverified_headers['alg'])
        if verify_token(payload['email'])==True:
            return [True,payload]
        else:
            return [False,{"status" : "Invalid user"}]
    except Exception as e:
        return [False,{"error" : str(e)}]