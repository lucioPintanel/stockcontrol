from app.main import db
from app.main.model.productOut import ProductOut

from ..util.convert import StrToDate


def save_new_productOut(data):
    productOut = None
    if not productOut:        
        new_productOut = ProductOut(
            id_product=data['id_product'],
            qtd=data['qtd'],
            value_unity=data['value_unity'],
            departure_date=StrToDate(data['departure_date'])
        )
        __save_changes(new_productOut)
        return { "mensagem" : "Cadastrado com sucesso no data base!" }
    else:
        response_object = {
            'status': 'fail',
            'message': 'Type unit already exists. Please Log in.',
        }
        return response_object, 409


def update_productOut(data):
    productOut = ProductOut.query.filter_by(id_product=data['id_product']).first()
    if productOut:
        if "qtd" in data:
            productOut.qtd = data['qtd']

        if "value_unity" in data:
            productOut.value_unity = data['value_unity']

        if "departure_date" in data:
            productOut.departure_date = data['departure_date']
        
        db.session.commit()
        return {"mensagem": "Alterado com sucesso no data base!"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Product Out already exists. Please Log in.',
        }
        return response_object, 409


def del_productOut(data):
    productOut = ProductOut.query.filter_by(id_product=data['id_product']).first()
    if productOut:
        delete_changes(productOut)
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted.',
            'id_product': data['id_product']
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Product Out not exists. Please Log in.',
        }
        return response_object, 404


def get_all_productOut():
    return ProductOut.query.all()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete_changes(data):
    db.session.delete(data)
    db.session.commit()