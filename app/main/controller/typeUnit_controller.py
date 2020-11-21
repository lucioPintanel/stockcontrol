from flask import request
from flask_restx import Resource

from ..util.dto import TUnitDto

from ..service.type_unit_service import get_all_typeUnit, save_new_typeUnit, update_typeUnit, del_type_unit
from app.main.util.decorator import token_required


api = TUnitDto.api
_typeUnit = TUnitDto.type_unit


@api.route('/')
@api.route('/<id>')
class TypeUnitList(Resource):
    @api.doc('list_of_registered_type_units')
    @api.marshal_list_with(_typeUnit, envelope='data')
    def get(self):
        """ List all registered type units """
        return get_all_typeUnit()

    @api.expect(_typeUnit, validate=True)
    @token_required
    @api.response(201, 'Type Unit successfully created.')
    @api.doc('create a new type unit')
    def post(self):
        """Creates a new Type Unit """
        data = request.json
        return save_new_typeUnit(data=data)

   
    @api.expect(_typeUnit, validate=True)
    @token_required
    @api.response(201, 'Type Unit successfully updated.')
    @api.doc('Update a type unit')
    def put(self):
        data = request.json
        return update_typeUnit(data=data)

    @token_required
    @api.response(201, 'Type Unit successfully deleted.')
    @api.doc('Delete a type unit')
    def delete(self,id):
        return del_type_unit(__id=id)
