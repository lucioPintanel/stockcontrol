from flask import request
from flask_restx import Resource

from ..util.dto import ProviderDto

from ..service.provider_service import get_all_provider, save_new_provider

api = ProviderDto.api
_provider = ProviderDto.provider

@api.route('/')
class ProviderList(Resource):
    @api.doc('list_of_registered_type_units')
    @api.marshal_list_with(_provider, envelope='data')
    def get(self):
        """ List all registered type units """
        return get_all_provider()

    @api.expect(_provider, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new type unit')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_provider(data=data) 