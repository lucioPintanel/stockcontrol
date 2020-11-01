from .. import db


class Order(db.Model):
    """
    Order Model
    """
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    provider_id = db.Column(db.Integer, db.ForeignKey('providers.id'))
    payment_conditions_id = db.Column(
        db.Integer, db.ForeignKey('payment_conditions.id'))
    qtd = db.Column(db.Integer, nullable=False)
    issuance_date = db.Column(db.DateTime, nullable=False)
    expected_date = db.Column(db.DateTime, nullable=False)
    issuing_date = db.Column(db.DateTime, nullable=False)
    devolution = db.Column(db.Boolean, nullable=False, default=False)
    value_total = db.Column(db.Integer, nullable=False)
    percentage_value = db.Column(db.Integer, nullable=False)

    def __init__(self, product_id, provider_id, payment_conditions_id, qtd, issuance_date, expected_date, issuing_date, devolution, value_total, percentage_value):
        self.product_id = product_id
        self.provider_id = provider_id
        self.payment_conditions_id = payment_conditions_id
        self.qtd = qtd
        self.issuance_date = issuance_date
        self.expected_date = expected_date
        self.issuing_date = issuing_date
        self.devolution = devolution
        self.value_total = value_total
        self.percentage_value = percentage_value

    def __repr__(self):
        return '<Data: {}'.format(self.issuance_date)
