from flask import request
from flask_restx import Resource

from ..util.dto import ProviderDto

from app.main.util.decorator import admin_token_required, token_required
from ..service.provider_service import get_all_provider, save_new_provider, update_provider, del_provider

api = ProviderDto.api
_provider = ProviderDto.provider

@api.route('/')
@api.route('/<item_id>')
class ProviderList(Resource):
    @api.doc('list_of_registered_provider')
    @api.marshal_list_with(_provider, envelope='data')
    def get(self):
        """ List all registered providers """
        return get_all_provider()

    @api.expect(_provider, validate=True)
    @token_required
    @api.response(201, 'Provider successfully created.')
    @api.doc('create a new provider')
    def post(self):
        """Creates a new Provider """
        data = request.json
        return save_new_provider(data=data) 

    @token_required
    @api.response(201, 'Provider successfully created.')
    @api.doc('create a new provider')
    def put(self):
        """Update a provider """
        data = request.json
        return update_provider(data=data) 

    @admin_token_required
    @api.response(201, 'Provider successfully deleted.')
    @api.doc('delete a provider')
    def delete(self):
        """Delete a Provider """
        data = request.json
        return del_provider(data)