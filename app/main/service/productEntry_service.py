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


def get_all_productEntry():
    return ProductEntry.query.all()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()
