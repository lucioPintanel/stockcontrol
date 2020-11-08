from .. import db


class ProductEntry(db.Model):
    """
    Product Entry Model
    """
    __tablename__ = 'product_entries'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_product = db.Column(db.Integer, nullable=False)
    qtd = db.Column(db.Integer, nullable=False)
    value_unity = db.Column(db.Integer, nullable=False)
    issuing_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, id_product, qtd, value_unity, issuance_date):
        self.id_product = id_product
        self.qtd = qtd
        self.value_unity = value_unity
        self.issuance_date = issuance_date

    def __repr__(self):
        return '<Data: {}'.format(self.issuance_date)
