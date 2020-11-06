from app.main import db
from app.main.model.product import Product


def save_new_product(data):
    product = Product.query.filter_by(name=data['name']).first()
    if not product:
        new_product = Product(
            name=data['name'],
            status=data['status'],
            manufacturers=data['manufacturers'],
            sector=data['sector'],
            measure=data['measure'],
            type_units_id=data['type_units_id']
        )
        __save_changes(new_product)
        return {"mensagem": "Cadastrado com sucesso no data base!"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Type unit already exists. Please Log in.',
        }
        return response_object, 409


def get_all_product():
    return Product.query.all()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()
