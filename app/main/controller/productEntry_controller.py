from flask import request
from flask_restx import Resource

from ..util.dto import ProEntryDto

from ..service.productEntry_service import get_all_productEntry, save_new_productEntry

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
    @api.response(201, 'Product entry successfully created.')
    @api.doc('create a new product entry')
    def post(self):
        """Creates a new Product Entry """
        data = request.json
        return save_new_productEntry(data=data) 
