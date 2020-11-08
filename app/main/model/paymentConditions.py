from .. import db


class PaymentConditions(db.Model):
    """
    Payment Conditions Model
    """
    __tablename__ = 'payment_conditions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # debito, cartao, à vista,...
    typePayment = db.Column(db.String(64), nullable=False)
    # Numero de parcelas
    qtd = db.Column(db.Integer, nullable=True)
    # Dia de vencimento
    dayPayment = db.Column(db.Integer, nullable=True)
    order = db.relationship("Order")

    def __init__(self, typePayment, qtd, dayPayment):
        self.typePayment = typePayment
        self.qtd = qtd
        self.dayPayment = dayPayment

    def __repr__(self):
        return '<Tipo de Pagamento: {}'.format(self.typePayment)
