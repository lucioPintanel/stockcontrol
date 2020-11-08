from app.main import db
from app.main.model.order import Order


def save_new_order(data):
    order = None
    if not order:
        new_order = Order(
            product_id=data['product_id'],
            provider_id=data['provider_id'],
            payment_conditions_id=data['payment_conditions_id'],
            qtd=data['qtd'],
            issuance_date=data['issuance_date'],
            expected_date=data['expected_date'],
            issuing_date=data['issuing_date'],
            devolution=data['devolution'],
            value_total=data['value_total'],
            percentage_value=data['percentage_value']
        )
        __save_changes(new_order)
        return {"mensagem": "Cadastrado com sucesso no data base!"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Type unit already exists. Please Log in.',
        }
        return response_object, 409


def get_all_order():
    return Order.query.all()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()
