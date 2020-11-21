from flask import request
from flask_restx import Resource

from ..util.dto import PayCondDto

from app.main.util.decorator import token_required
from ..service.paymentCondt_service import save_new_pay_condit, get_all_pay_condit, update_pay_condit, del_pay_condit

api = PayCondDto.api
_pay_condit = PayCondDto.pay_cond

@api.route('/')
class PayConditList(Resource):
    @api.doc('list_of_registered_pay_condit')
    @api.marshal_list_with(_pay_condit, envelope='data')
    def get(self):
        """ List all registered Payment Condition """
        return get_all_pay_condit()

    @api.expect(_pay_condit, validate=True)
    @api.response(201, 'Payment Condition successfully created.')
    @api.doc('create a new payment condition')
    def post(self):
        """Creates a new Payment Condition """
        data = request.json
        return save_new_pay_condit(data=data) 

    @token_required
    @api.response(201, 'Payment Condition successfully updated.')
    @api.doc('Update a Payment Condition')
    def put(self):
        data = request.json
        return update_pay_condit(data=data)

    @token_required
    @api.response(201, 'Payment Condition successfully deleted.')
    @api.doc('Delete a Payment Condition')
    def delete(self,id):
        return del_pay_condit(__id=id)