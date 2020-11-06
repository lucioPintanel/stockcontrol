from flask import request
from flask_restx import Resource

from ..util.dto import ProductDto

from ..service.product_service import get_all_product, save_new_product

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
    @api.response(201, 'Product successfully created.')
    @api.doc('create a new product')
    def post(self):
        """Creates a new Product """
        data = request.json
        return save_new_product(data=data) 