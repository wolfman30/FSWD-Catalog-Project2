from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    name = Column(String(60), nullable = False)
    email = Column(String(100))
    picture = Column(String(500))

    @property 
    def serialize(self):
        #returns the data as a dictionary which is easier to serialize and analyze 
        return {"id": self.id, 
                "name": self.name, 
                "email": self.email, 
                "picture": self.picture}

class AgingHallmark(Base):
    
    __tablename__ = 'aging_hallmark'

    id = Column(Integer, primary_key=True)
    name = Column(String(300), nullable=False)
    summary = Column(String(300))
    treatment = Column(String(300))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property 
    def serialize(self):
        #returns the data as a dictionary which is easier to serialize and analyze 
        return {"id": self.id, 
                "name": self.name, 
                "summary": self.summary, 
                "treatment": self.treatment}

class HallmarkDetails(Base):
    
    __tablename__ = 'hallmark_details'

    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    references = Column(String(250))
    hallmark_id = Column(Integer, ForeignKey('aging_hallmark.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    aging_hallmark = relationship(AgingHallmark)
    user = relationship(User)

    @property 
    def serialize(self):
        #returns the data as a dictionary which is easier to serialize and analyze 
        return {"id": self.id, 
                "name": self.name, 
                "description": self.description, 
                "references": self.references 
               }

class GlossaryofTerms(Base):

    __tablename__ = 'glossary'

    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    definition = Column(String(500))

    @property 
    def serialize(self):
        return {"id": self.id, 
                "name":self.name, 
                "definition": self.definition}

class References(Base):

    __tablename__ = "references"
    
    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)

    @property 
    def serialize(self): 
        return {"id": self.id, 
                "name": self.name}

engine = create_engine('sqlite:///aginghallmarks.db', 
            connect_args = {'check_same_thread': False})
            #connect_args: courtesy of John S from:
            # https://knowledge.udacity.com/questions/7834

Base.metadata.create_all(engine)