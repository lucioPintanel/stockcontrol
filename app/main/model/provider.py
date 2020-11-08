from .. import db


class Provider(db.Model):
    """
    provider Model
    """
    __tablename__ = 'provider'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    cnpj = db.Column(db.String(18), unique=True, nullable=False)
    contact = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    telephone = db.Column(db.String(20), unique=False, nullable=True)
    order = db.relationship("Order")

    def __init__(self, name, cnpj, contact, email, telephone):
        self.name = name
        self.cnpj = cnpj
        self.contact = contact
        self.email = email
        self.telephone = telephone

    def __repr__(self):
        return '<name: {}'.format(self.name)
