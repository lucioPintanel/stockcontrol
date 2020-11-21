from app.main import db
from app.main.model.productEntry import ProductEntry

from ..util.convert import StrToDate


def save_new_productEntry(data):
    productEntry = None
    if not productEntry:        
        new_productEntry = ProductEntry(
            id_product=data['id_product'],
            qtd=data['qtd'],
            value_unity=data['value_unity'],
            issuance_date=StrToDate(data['issuing_date'])
        )
        __save_changes(new_productEntry)
        return { "mensagem" : "Cadastrado com sucesso no data base!" }
    else:
        response_object = {
            'status': 'fail',
            'message': 'Type unit already exists. Please Log in.',
        }
        return response_object, 409


def update_productEntry(data):
    productEntry = ProductEntry.query.filter_by(id_product=data['id_product']).first()
    if productEntry:
        if "qtd" in data:
            productEntry.qtd = data['qtd']

        if "value_unity" in data:
            productEntry.value_unity = data['value_unity']

        if "issuance_date" in data:
            productEntry.issuance_date = data['issuance_date']
        
        db.session.commit()
        return {"mensagem": "Alterado com sucesso no data base!"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Product Entry already exists. Please Log in.',
        }
        return response_object, 409


def del_productEntry(data):
    productEntry = ProductEntry.query.filter_by(id_product=data['id_product']).first()
    if productEntry:
        delete_changes(productEntry)
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted.',
            'id_product': data['id_product']
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Product Entry not exists. Please Log in.',
        }
        return response_object, 404


def get_all_productEntry():
    return ProductEntry.query.all()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete_changes(data):
    db.session.delete(data)
    db.session.commit()
