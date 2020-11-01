from flask import request
from flask_restx import Resource

from ..util.dto import TUnitDto

api = TUnitDto.api
_typeUnit = TUnitDto.typeunit

@api.route('/')
class TypeUnitList(Resource):
    @api.doc('list_of_registered_type_units')
    #@api.marshal_list_with(_typeUnit, envelope='data')
    def get(self):
        """List all registered type units"""
        #return get_all_type_unit()
        return { "menssagem" : "Lista os tipos de unidades registradas!" }