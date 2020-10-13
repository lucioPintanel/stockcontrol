from . import movement_bp
from flask import request, jsonify

@movement_bp.route('/')
def getMovement_All():
    return {"msg":"Movement All!"}

@movement_bp.route('/<int:_id>',methods = ['POST', 'GET'])
def getMovement_ID(_id):
    if request.method == 'POST':
        id=_id
        data = request.get_json()
        return {"msg":data['name']}
    else:
        return {"msg":_id}

@movement_bp.route('/<int:_id>',methods = ['PUT'])
def putMovement_ID(_id):
    if request.method == 'PUT':
        id=_id
        data = request.get_json()
        return {"msg":data['name']}
    else:
        return {"msg":"Metodo Incorreto!"}

@movement_bp.route('/<int:_id>',methods = ['DELETE'])
def deleteMovement_ID(_id):
    if request.method == 'DELETE':
        id=_id
        data = request.get_json()
        return {"msg":data['name'],"msg1":"Movimentação apagado com sucesso"}
    else:
        return {"msg":"Metodo Incorreto!"}
