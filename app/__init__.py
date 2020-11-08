from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.typeUnit_controller import api as tUnit_ns
from .main.controller.product_controller import api as product_ns
from .main.controller.provider_controller import api as provider_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS(RESTX) API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus (restx) web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(tUnit_ns, path='/type_unit')
api.add_namespace(product_ns, path='/product')
api.add_namespace(provider_ns, path='/provider')