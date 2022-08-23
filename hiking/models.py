from hiking import db

class Entrance(db.Model):
    __tablename__ = "entrances"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    driving_time = db.Column(db.Integer)
    trails = db.relationship('Trail', backref="entrance", lazy='dynamic')

    def __init__(self, name, driving_time):
        self.name = name
        self.driving_time = driving_time

    def __repr__(self):
        path = []
        for trail in self.trails:
            #pass
            path.append(trail)
        if len(path) > 0:
            object_string = ', '.join([str(x) for x in path])
            return f"The hiking place is at {self.name} and the id is {self.id} and the trails are {object_string}. The place is {self.driving_time} minutes away."
        else:
            return f"The hikinh place is at {self.name} and the id is {self.id}. The place is {self.driving_time} minutes away."

class Trail(db.Model):
    __tablename__ = "trails"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    entrance_id = db.Column(db.Integer, db.ForeignKey("entrances.id"))

    def __init__(self,name,entrance_id):
        self.name = name
        self.entrance_id = entrance_id

    def __repr__(self):
        return f"{self.name}"
        #return "OK"
