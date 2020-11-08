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


def get_all_productOut():
    return ProductOut.query.all()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()
