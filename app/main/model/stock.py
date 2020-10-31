from .. import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Stock(db.Model):
    """
    Stock Model
    """
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_product = db.Column(db.Integer, nullable=False)
    qtd = db.Column(db.Integer, nullable=False)
    value_unity = db.Column(db.Integer, nullable=False)

    def __init__(self, id_product, qtd, value_unity):
        self.id_product = id_product
        self.qtd = qtd
        self.value_unity = value_unity

    def __repr__(self):
        return '<Quantidade: {}'.format(self.qtd)
