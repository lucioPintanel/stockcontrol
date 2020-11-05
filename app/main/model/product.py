from .. import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Product(db.Model):
    """
    Product Model
    """
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=False)
    manufacturers = db.Column(db.String(80), unique=False, nullable=True)
    sector = db.Column(db.String(80), unique=False, nullable=True)
    measure = db.Column(db.String(80), unique=False, nullable=True)
    type_units_id = db.Column(db.Integer, db.ForeignKey('type_units.id'),
                              nullable=False)

    def __init__(self, name, status, manufacturers, sector, measure, type_units_id):
        self.name = name
        self.status = status
        self.manufacturers = manufacturers
        self.sector = sector
        self.measure = measure
        self.type_units_id = type_units_id

    def __repr__(self):
        return '<name: {}'.format(self.name)
