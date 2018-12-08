from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class AgingHallmark(Base):
    
    __tablename__ = 'aging_hallmark'

    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    summary = Column(String(300))

class HallmarkDetails(Base):
    
    __tablename__ = 'hallmark_details'

    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    treatment = Column(String(300))
    hallmark_id = Column(Integer, ForeignKey('aging_hallmark.id'))
    aging_hallmark = relationship(AgingHallmark)

engine = create_engine('sqlite:///aginghallmarks.db', 
            connect_args = {'check_same_thread': False})
            #connect_args: courtesy of John S from:
            # https://knowledge.udacity.com/questions/7834

Base.metadata.create_all(engine)