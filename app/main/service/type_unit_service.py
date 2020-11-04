import uuid
import datetime

from app.main import db
from app.main.model.typeunit import TypeUnit


def save_new_typeUnit(data):
    typeUnit = TypeUnit.query.filter_by(typeunit=data['typeunit']).first()
    if not typeUnit:        
        new_typeUnit = TypeUnit(
            typeunit=data['typeunit']
        )
        __save_changes(new_typeUnit)
        return { "mensagem" : "Cadastrado com sucesso no data base!" }
    else:
        response_object = {
            'status': 'fail',
            'message': 'Type unit already exists. Please Log in.',
        }
        return response_object, 409


def get_all_typeUnit():
    return TypeUnit.query.all()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()
