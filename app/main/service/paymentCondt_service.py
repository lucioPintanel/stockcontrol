from app.main import db
from app.main.model.paymentConditions import PaymentConditions


def save_new_pay_condit(data):
    paymentConditions = PaymentConditions.query.filter_by(id=data['id']).first()
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


def update_pay_condit(data):
    pay_condit = PaymentConditions.query.filter_by(id=data['id']).first()
    if pay_condit:
        if "typePayment" in data:
            pay_condit.typePayment = data['typePayment']

        if "qtd" in data:
            pay_condit.typePayment = data['qtd']

        if "qtd" in data:
            pay_condit.typePayment = data['payday']

        db.session.commit()
        return {"mensagem": "Alterado com sucesso no data base!"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Payment Conditions already exists. Please Log in.',
        }
        return response_object, 409


def del_pay_condit(__id):
    pay_condit = PaymentConditions.query.get(int(__id))
    if pay_condit:
        delete_changes(pay_condit)
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted.',
            'public_id': __id
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Payment Conditions not exists. Please Log in.',
        }
        return response_object, 404


def get_all_pay_condit():
    return PaymentConditions.query.all()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete_changes(data):
    db.session.delete(data)
    db.session.commit()