from flask import request
from flask_restx import Resource

from ..util.dto import ProOutDto

from ..service.productOut_service import get_all_productOut, save_new_productOut

api = ProOutDto.api
_prodOut = ProOutDto.prodOut

@api.route('/')
class ProductOutList(Resource):
    @api.doc('list_of_registered_product_out')
    @api.marshal_list_with(_prodOut, envelope='data')
    def get(self):
        """ List all registered product out """
        return get_all_productOut()

    @api.expect(_prodOut, validate=True)
    @api.response(201, 'Product out successfully created.')
    @api.doc('create a new product out')
    def post(self):
        """Creates a new Product Out """
        data = request.json
        return save_new_productOut(data=data) 
