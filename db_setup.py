from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class AgingHallmark(Base):
    __tablename__ = 'aging_hallmark'

    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)


engine = create_engine('sqlite:///aginghallmarks.db', 
            connect_args = {'check_same_thread': False})
            #connect_args: courtesy of John S from:
            # https://knowledge.udacity.com/questions/7834

Base.metadata.create_all(engine)