from flask import request
from flask_restx import Resource

from ..util.dto import ProductDto

from app.main.util.decorator import admin_token_required, token_required
from ..service.product_service import get_all_product, save_new_product, update_product, del_product

api = ProductDto.api
_product = ProductDto.product

@api.route('/')
class ProductList(Resource):
    @api.doc('list_of_registered_product')
    @api.marshal_list_with(_product, envelope='data')
    def get(self):
        """ List all registered product """
        return get_all_product()

    @api.expect(_product, validate=True)
    @token_required
    @api.response(201, 'Product successfully created.')
    @api.doc('create a new product')
    def post(self):
        """Creates a new Product """
        data = request.json
        return save_new_product(data=data) 

    @token_required
    @api.response(201, 'Product successfully updated.')
    @api.doc('Update a Product')
    def put(self):
        """Update a Product """
        data = request.json
        return update_product(data=data) 

    @admin_token_required
    @api.response(201, 'Product successfully deleted.')
    @api.doc('Delete a Product')
    def delete(self):
        """Delete a Product """
        data = request.json
        return del_product(data)