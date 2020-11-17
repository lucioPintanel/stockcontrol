from flask import request
from flask_restx import Resource

from ..util.dto import ProviderDto

from ..service.provider_service import get_all_provider, save_new_provider, update_provider
from app.main.util.decorator import token_required

api = ProviderDto.api
_provider = ProviderDto.provider

@api.route('/')
class ProviderList(Resource):
    @api.doc('list_of_registered_provider')
    @api.marshal_list_with(_provider, envelope='data')
    def get(self):
        """ List all registered type units """
        return get_all_provider()

    @api.expect(_provider, validate=True)
    @token_required
    @api.response(201, 'Provider successfully created.')
    @api.doc('create a new provider')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_provider(data=data) 

    @api.expect(_provider, validate=True)
    @token_required
    @api.response(201, 'Provider successfully created.')
    @api.doc('create a new provider')
    def put(self):
        """Update a provider """
        data = request.json
        return update_provider(data=data) 