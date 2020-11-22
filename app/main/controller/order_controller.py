from flask import request
from flask_restx import Resource

from ..util.dto import OrderDto

from app.main.util.decorator import admin_token_required, token_required
from ..service.order_service import get_all_order, save_new_order, update_order, del_order

api = OrderDto.api
_order = OrderDto.order

@api.route('/')
class Order(Resource):
    @api.doc('list_of_registered_order')
    @api.marshal_list_with(_order, envelope='data')
    def get(self):
        """ List all registered order """
        return get_all_order()

    @api.expect(_order, validate=True)
    @api.response(201, 'Order successfully created.')
    @api.doc('create a new order')
    def post(self):
        """Creates a new Order"""
        data = request.json
        return save_new_order(data=data)

    @token_required
    @api.response(201, 'Order successfully updated.')
    @api.doc('Update a order')
    def put(self):
        """Update a order """
        data = request.json
        return update_order(data=data) 

    @admin_token_required
    @api.response(201, 'Order successfully deleted.')
    @api.doc('delete a order')
    def delete(self):
        """Delete a Order """
        data = request.json
        return del_order(data=data)