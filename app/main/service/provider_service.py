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


def get_all_provider():
    return Provider.query.all()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()
