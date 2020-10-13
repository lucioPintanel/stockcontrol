from flask import Blueprint

movement_bp = Blueprint('movement_bp', __name__, url_prefix="/movement")

from . import notaFiscal, movement
