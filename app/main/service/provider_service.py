from app.main import db
from app.main.model.provider import Provider


def save_new_provider(data):
    provider = Provider.query.filter_by(cnpj=data['cnpj']).first()
    if not provider:
        new_provider = Provider(
            name=data['name'],
            cnpj=data['cnpj'],
            contact=data['contact'],
            email=data['email'],
            telephone=data['telephone']
        )
        __save_changes(new_provider)
        return {"mensagem": "Cadastrado com sucesso no data base!"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Type unit already exists. Please Log in.',
        }
        return response_object, 409


def update_provider(data):
    provider = Provider.query.filter_by(cnpj=data['cnpj']).first()
    if provider:
        if not provider.name == data['name']:
            provider.name = data['name']

        if not provider.contact == data['contact']:
            provider.contact = data['contact']

        if not provider.email == data['email']:
            provider.email = data['email']

        if not provider.telephone == data['telephone']:
            provider.telephone = data['telephone']

        db.session.commit()
        return {"mensagem": "Alterado com sucesso no data base!"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Type unit already exists. Please Log in.',
        }
        return response_object, 409


def del_provider(data):
    provider = Provider.query.filter_by(cnpj=data['cnpj']).first()
    if provider:
        delete_changes(provider)
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted.',
            'public_id': data['cnpj']
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Provider not exists. Please Log in.',
        }
        return response_object, 404


def get_all_provider():
    return Provider.query.all()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete_changes(data):
    db.session.delete(data)
    db.session.commit()
