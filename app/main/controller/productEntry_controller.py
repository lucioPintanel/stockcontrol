from flask import request
from flask_restx import Resource

from ..util.dto import ProEntryDto

from app.main.util.decorator import admin_token_required, token_required
from ..service.productEntry_service import get_all_productEntry, save_new_productEntry, update_productEntry, del_productEntry

api = ProEntryDto.api
_prodEntry = ProEntryDto.prodEntry

@api.route('/')
class ProductOutList(Resource):
    @api.doc('list_of_registered_product_entry')
    @api.marshal_list_with(_prodEntry, envelope='data')
    def get(self):
        """ List all registered product entry """
        return get_all_productEntry()

    @api.expect(_prodEntry, validate=True)
    @token_required
    @api.response(201, 'Product entry successfully created.')
    @api.doc('create a new product entry')
    def post(self):
        """Creates a new Product Entry """
        data = request.json
        return save_new_productEntry(data=data) 

    @token_required
    @api.response(201, 'Product entry successfully updated.')
    @api.doc('Update a Product entry')
    def put(self):
        """Update a Product entry """
        data = request.json
        return update_productEntry(data=data) 

    @admin_token_required
    @api.response(201, 'Product entry successfully deleted.')
    @api.doc('Delete a Product entry')
    def delete(self):
        """Delete a Product entry """
        data = request.json
        return del_productEntry(data)
