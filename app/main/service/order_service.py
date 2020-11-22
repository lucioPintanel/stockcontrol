from app.main import db
from app.main.model.order import Order

from ..util.convert import StrToDate

def save_new_order(data):
    order = None
    if not order:
        new_order = Order(
            product_id=data['product_id'],
            provider_id=data['provider_id'],
            payment_conditions_id=data['payment_conditions_id'],
            qtd=data['qtd'],
            issuance_date=StrToDate(data['issuance_date']),
            expected_date=StrToDate(data['expected_date']),
            issuing_date=StrToDate(data['issuing_date']),
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


def update_order(data):
    order = Order.query.filter_by(id=data['id']).first()
    if order:
        if "provider_id" in data:
            order.provider_id = data['provider_id']
        
        if "payment_conditions_id" in data:
            order.payment_conditions_id = data['payment_conditions_id']

        if "qtd" in data:
            order.qtd = data['qtd']

        if "issuance_date" in data:
            order.issuance_date = data['issuance_date']

        if "expected_date" in data:
            order.expected_date = data['expected_date']

        if "issuing_date" in data:
            order.issuing_date = data['issuing_date']

        if "devolution" in data:
            order.devolution = data['devolution']

        if "value_total" in data:
            order.value_total = data['value_total']

        if "percentage_value" in data:
            order.percentage_value = data['percentage_value']
        
        db.session.commit()
        return {"mensagem": "Alterado com sucesso no data base!"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Order already exists. Please Log in.',
        }
        return response_object, 409


def del_order(data):
    order = Order.query.filter_by(id=data['id']).first()
    if order:
        delete_changes(order)
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted.',
            'id': data['id']
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Order not exists. Please Log in.',
        }
        return response_object, 404


def get_all_order():
    return Order.query.all()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete_changes(data):
    db.session.delete(data)
    db.session.commit()