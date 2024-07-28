from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

engine=create_engine("sqlite:///AirnbReservation.db", echo =True)
Base.metadata.create_all(bind=engine)
Session=sessionmaker(bind=engine)
session=Session()