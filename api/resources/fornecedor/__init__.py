from flask import Blueprint

fornecedor_bp = Blueprint('fornecedor_bp', __name__, url_prefix="/fornecedor")

from . import fornecedor
