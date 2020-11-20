from flask import request
from flask_restx import Resource

from ..util.dto import ProviderDto

from app.main.util.decorator import admin_token_required
from ..service.provider_service import get_all_provider, save_new_provider, update_provider, del_provider
from app.main.util.decorator import token_required

api = ProviderDto.api
_provider = ProviderDto.provider

@api.route('/')
@api.route('/<item_id>')
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

    @token_required
    @api.response(201, 'Provider successfully created.')
    @api.doc('create a new provider')
    def put(self):
        """Update a provider """
        data = request.json
        return update_provider(data=data) 

    @admin_token_required
    @api.response(201, 'User successfully deleted.')
    @api.doc('delete a user')
    def delete(self):
        """Delete a User """
        data = request.json
        return del_provider(data)