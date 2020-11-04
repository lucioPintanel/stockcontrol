from flask import request
from flask_restx import Resource

from ..util.dto import TUnitDto

from ..service.type_unit_service import get_all_typeUnit, save_new_typeUnit

api = TUnitDto.api
_typeUnit = TUnitDto.type_unit

@api.route('/', methods = ['POST', 'GET'])
class TypeUnitList(Resource):
    @api.doc('list_of_registered_type_units')
    @api.marshal_list_with(_typeUnit, envelope='data')
    def get(self):
        """ List all registered type units """
        return get_all_typeUnit()

    @api.expect(_typeUnit, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new type unit')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_typeUnit(data=data)