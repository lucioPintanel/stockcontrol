from flask import request
from flask_restx import Resource

from ..util.dto import OrderDto

from ..service.order_service import get_all_order, save_new_order

api = OrderDto.api
_order = OrderDto.order

@api.route('/')
class TypeUnitList(Resource):
    @api.doc('list_of_registered_order')
    @api.marshal_list_with(_order, envelope='data')
    def get(self):
        """ List all registered type units """
        return get_all_order()

    @api.expect(_order, validate=True)
    @api.response(201, 'Order successfully created.')
    @api.doc('create a new order')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_order(data=data) 
