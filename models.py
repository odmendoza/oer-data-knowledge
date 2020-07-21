from database import Base


class Triplete(Base):
    __tablename__ = 'triplete'
    __table_args__ = {'autoload': True}


    '''
    id = Column(Integer, primary_key=True)
    subject = Column(String)
    predicate = Column(String)
    object = Column(String)
    repository = Column(String)

    def __init__(self, subject=None, predicate=None, repository=None, object=None):
        self.subject = subject
        self.predicate = predicate
        self.object = object
        self.repository = repository

    def __repr__(self):
        return '<Triplete %r>' % (self.subject)
    '''
