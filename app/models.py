from . import db

class realestate(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),  unique=True)
    description = db.Column(db.String(255))
    num_rooms = db.Column(db.Integer)
    num_brooms = db.Column(db.Integer)
    price = db.Column(db.String(255))
    ptype =  db.Column(db.String(255))
    location = db.Column(db.String(255))
    pname = db.Column(db.String(255))


    def __init__(self, title, desc, nroom, nbroom, precio, tipo, local, pnombre ):
        self.title= title
        self.description = desc
        self.num_rooms = nroom
        self.num_brooms = nbroom
        self.price = precio
        self.tpype = tipo
        self.location = local
        self.pname = pnombre    

