from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user, del_a_user, put_a_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @admin_token_required
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        print("Get a user")
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)

    @admin_token_required
    @api.response(201, 'User successfully deleted.')
    @api.doc('delete a user')
    def delete(self):
        """Delete a User """
        data = request.json
        return del_a_user(public_id=data['public_id'])


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @token_required
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id=public_id)
        if not user:
            api.abort(404)
        else:
            return user

    @api.doc('get a user')
    @token_required
    @api.marshal_with(_user)
    def put(self, public_id):
        """get a user given its identifier"""
        data = request.json
        user = put_a_user(public_id=public_id, data=data)
        if not user:
            api.abort(404)
        else:
            return user
