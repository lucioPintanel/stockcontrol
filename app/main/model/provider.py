from .. import db

class Provider(db.Model):
    """
    provider Model
    """
    __tablename__ = 'provider'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    cnpj = db.Column(db.String(14), unique=True, nullable=False)
    contato = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    telefone = db.Column(db.String(20), unique=False, nullable=True)

    def __init__(self, name,cnpj, contato, email, telefone):
        self.name= name
        self.cnpj= cnpj
        self.contato= contato
        self.email= email
        self.telefone=telefone

    def __repr__(self):
        return '<name: {}'.format(self.name)
