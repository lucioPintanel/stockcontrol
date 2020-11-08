from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class TUnitDto:
    api = Namespace('type_unit', description='type unit related operations')
    type_unit = api.model('type_unit', {
        'typeunit': fields.String(required=True, description='tipo de unidades')
    })


class ProductDto:
    api = Namespace('product', description='product related operations')
    product = api.model('product', {
        'name': fields.String(required=True, description='product name'),
        'status': fields.Boolean(required=True, description='status product', default=True),
        'manufacturers': fields.String(required=False, description='manufacturers name'),
        'sector': fields.String(required=False, description='sector name'),
        'measure': fields.Integer(required=True, description='measure name'),
        'type_units_id': fields.Integer(required=True, description='type unit id')
    })


class ProviderDto:
    api = Namespace('provider', description='provider related operations')
    provider = api.model('provider', {
        'name': fields.String(required=True, description='provider name'),
        'cnpj': fields.String(required=True, description='cnpj'),
        'contact': fields.String(required=True, description='supplier contact'),
        'email': fields.String(required=True, description='supplier contact email'),
        'telephone': fields.String(required=True, description='supplier contact telephone'),
    })

class PayCondDto:
    api = Namespace('pay_cond', description='payment conditions related operations')
    pay_cond = api.model('pay_cond', {
        'typePayment': fields.String(required=True, description='payment type'),
        'qtd': fields.Integer(required=True, description='number of times'),
        'payday':fields.Integer(required=True, description='payment of day'),
    })

class OrderDto:
    api = Namespace('order', description='payment conditions related operations')
    order = api.model('order', {
        'product_id': fields.Integer(required=True, description='ID of product'),
        'provider_id': fields.Integer(required=True, description='ID of provider'),
        'payment_conditions_id': fields.Integer(required=True, description='ID of payment condition'),
        'qtd': fields.Integer(required=True, description='number of times'),
        'issuance_date': fields.DateTime(required=True, description='issuance date'),
        'expected_date': fields.DateTime(required=True, description='expected date'),
        'issuing_date': fields.DateTime(required=True, description='issuing date'),
        'devolution': fields.Boolean(required=True, description='status devolution', default=False),
        'value_total': fields.Integer(required=True, description='value total'),
        'percentage_value': fields.Integer(required=True, description='percentage value'),
    })
