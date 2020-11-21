from flask import request
from flask_restx import Resource

from ..util.dto import TSectorDto

from ..service.sector_service import get_all_sector, save_new_sector, update_sector, del_sector
from app.main.util.decorator import token_required


api = TSectorDto.api
_sector = TSectorDto.sector


@api.route('/')
class SectorList(Resource):
    @api.doc('list_of_registered_sector')
    @api.marshal_list_with(_sector, envelope='data')
    def get(self):
        """ List all registered sectors """
        return get_all_sector()

    @api.expect(_sector, validate=True)
    @token_required
    @api.response(201, 'Sector successfully created.')
    @api.doc('create a new sector')
    def post(self):
        """Creates a new Sector """
        data = request.json
        return save_new_sector(data=data)

   
    @api.expect(_sector, validate=True)
    @token_required
    @api.response(201, 'Sector successfully updated.')
    @api.doc('Update a sector')
    def put(self):
        data = request.json
        return update_sector(data=data)

    @token_required
    @api.response(201, 'Sector successfully deleted.')
    @api.doc('Delete a sector')
    def delete(self,id):
        return del_sector(__id=id)
