from flask import Blueprint

product_bp = Blueprint('product_bp', __name__, url_prefix="/product")
unit_bp = Blueprint('unit_bp', __name__, url_prefix="/unit")

from . import product, unitMeas
