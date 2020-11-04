from .. import db

class TypeUnit(db.Model):
    """
    Type Unit Model
    """
    __tablename__ = 'type_units'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    typeunit = db.Column(db.String(5), unique=True, nullable=False)
    product = db.relationship('Product', backref='products', lazy=True)

    def __repr__(self):
        return '<id: typeunit: {}'.format(self.typeunit)
