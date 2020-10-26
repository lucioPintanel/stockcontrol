from .. import db

class Stock(db.Model):
    """
    Stock Model
    """
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # id product
    qtd = db.Column(db.Integer, nullable=False)
    value_unity = db.Column(db.Integer, nullable=False)
    
    def __init__(self, ''' id product''', qtd, value_unity):
		# id product
		self.qtd = qtd
		self.value_unity = value_unity

    def __repr__(self):
        return '<Quantidade: {}'.format(self.qtd)
