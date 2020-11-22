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


def update_product(data):
    product = Product.query.filter_by(id=data['id']).first()
    if product:
        if "name" in data:
            product.name = data['name']

        if "status" in data:
            product.status = data['status']

        if "manufacturers" in data:
            product.manufacturers = data['manufacturers']

        if "sector" in data:
            product.sector = data['sector']

        if "measure" in data:
            product.measure = data['measure']

        if "type_units_id" in data:
            product.type_units_id = data['type_units_id']
        
        db.session.commit()
        return {"mensagem": "Alterado com sucesso no data base!"}
    else:
        response_object = {
            'status': 'fail',
            'message': 'Product already exists. Please Log in.',
        }
        return response_object, 409


def del_product(data):
    product = Product.query.filter_by(id=data['id']).first()
    if product:
        delete_changes(product)
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted.',
            'id_product': data['id_product']
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Product not exists. Please Log in.',
        }
        return response_object, 404


def get_all_product():
    return Product.query.all()


def __save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete_changes(data):
    db.session.delete(data)
    db.session.commit()