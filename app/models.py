from . import db

class Element(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable=False)
    sp_heat = db.Column(db.float, nullable=False)
    heat_vp = db.Column(db.float, nullable=False)
    boiling_pt = db.Column(db.float, nullable=False)

def __init__(self, name, sp_heat, heat_vp, boiling_pt):
    self.name = name
    self.sp_heat = sp_heat
    self.heat_vp = heat_vp
    self.boiling_pt = boiling_pt