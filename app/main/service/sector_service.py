from app.main import db
from app.main.model.sector import Sector


def save_new_Sector(data):
    sector = Sector.query.filter_by(sector=data['sector']).first()
    if not sector:
        new_sector = Sector(
            sector=data['sector']
        )
        __save_changes(new_sector)
        return {"mensagem": "Cadastrado com sucesso no data base!"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Sector already exists. Please Log in.',
        }
        return response_object, 409


def update_sector(data):
    sector = Sector.query.filter_by(sector=data['sector']).first()
    if sector:
        sector.sector = data['sector_new']
        __save_changes(sector)
        return {"mensagem": "Alterado com sucesso no data base!"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Sector already exists. Please Log in.',
        }
        return response_object, 409


def del_type_unit(__id):
    sector = Sector.query.get(int(__id))
    if sector:
        delete_changes(sector)
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted.',
            'sector': sector.sector
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Sector not exists. Please Log in.',
        }
        return response_object, 404


def get_all_sector():
    return Sector.query.all()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete_changes(data):
    db.session.delete(data)
    db.session.commit()
