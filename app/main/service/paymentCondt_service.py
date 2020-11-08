from app.main import db
from app.main.model.paymentConditions import PaymentConditions


def save_new_pay_condit(data):
    paymentConditions = PaymentConditions.query.filter_by(typePayment=data['typePayment']).first()
    if not paymentConditions:
        new_pay_condit = PaymentConditions(
            typePayment=data['typePayment'],
            qtd=data['qtd'],
            payday=data['payday']
        )
        __save_changes(new_pay_condit)
        return {"mensagem": "Cadastrado com sucesso no data base!"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Type unit already exists. Please Log in.',
        }
        return response_object, 409


def get_all_pay_condit():
    return PaymentConditions.query.all()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()
