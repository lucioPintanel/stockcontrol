from app.main import db
from app.main.model.typeunit import TypeUnit


def save_new_typeUnit(data):
    typeUnit = TypeUnit.query.filter_by(typeunit=data['typeunit']).first()
    if not typeUnit:
        new_typeUnit = TypeUnit(
            typeunit=data['typeunit']
        )
        __save_changes(new_typeUnit)
        return {"mensagem": "Cadastrado com sucesso no data base!"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Type unit already exists. Please Log in.',
        }
        return response_object, 409


def update_typeUnit(data):
    typeUnit = TypeUnit.query.filter_by(typeunit=data['typeunit']).first()
    if typeUnit:
        typeUnit.typeunit = data['typeunit_new']
        __save_changes(typeUnit)
        return {"mensagem": "Alterado com sucesso no data base!"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Type unit already exists. Please Log in.',
        }
        return response_object, 409


def del_type_unit(__id):
    typeUnit = TypeUnit.query.get(int(__id))
    if typeUnit:
        delete_changes(typeUnit)
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted.',
            'public_id': __id
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Type Unit not exists. Please Log in.',
        }
        return response_object, 404


def get_all_typeUnit():
    return TypeUnit.query.all()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete_changes(data):
    db.session.delete(data)
    db.session.commit()
