from .. import db

class Product(db.Model):
    """
    Product Model
    """
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    fabricante = db.Column(db.String(80), unique=False, nullable=True)
    setor = db.Column(db.String(80), unique=False, nullable=True)
    medida = db.Column(db.String(80), unique=False, nullable=True)
    type_units_id = db.Column(db.Integer, db.ForeignKey('type_units.id'),
        nullable=False)

    def __init__(self, name,fabricante, setor, medida):
        self.name= name
        self.fabricante= fabricante
        self.setor= setor
        self.medida= medida

    def __repr__(self):
        return '<name: {}'.format(self.name)
