from databaseconn.database import Base
from sqlalchemy import Column,Integer,String

class User(Base):
    __tablename__="users"

    id=Column(Integer,autoincrement=True,primary_key=True)
    user_name=Column("username",String)
    email=Column("email",String,unique=True)
    password=Column("password",String)
    user_type=Column("user_type",String,default="Guest")
  
    def __repr__(self):
        return f'''{{
            id : {self.id}, 
            username : {self.user_name}, 
            email : {self.email}, 
            password : {self.password}, 
            user_type : {self.user_type}
            }}'''
    