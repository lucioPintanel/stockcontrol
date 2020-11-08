from .. import db


class ProductOut(db.Model):
    """
    Product Out Model
    """
    __tablename__ = 'product_outs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_product = db.Column(db.Integer, nullable=False)
    qtd = db.Column(db.Integer, nullable=False)
    value_unity = db.Column(db.Integer, nullable=False)
    departure_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, id_product, qtd, value_unity, departure_date):
        self.id_product = id_product
        self.qtd = qtd
        self.value_unity = value_unity
        self.departure_date = departure_date

    def __repr__(self):
        return '<Data: {}'.format(self.departure_date)
