from . import product_bp
from flask import request, jsonify

@product_bp.route('/')
def getProduct_All():
    return {"msg":"Product All!"}

@product_bp.route('/<username>')
def getProduct_Name(username):
    # show the user profile for that user
    return {"msg":username}

@product_bp.route('/<int:_id>',methods = ['POST', 'GET'])
def getProduct_ID(_id):
    if request.method == 'POST':
        id=_id
        data = request.get_json()
        return {"msg":data['name']}
    else:
        return {"msg":_id}

@product_bp.route('/<int:_id>',methods = ['PUT'])
def putProduct_ID(_id):
    if request.method == 'PUT':
        id=_id
        data = request.get_json()
        return {"msg":data['name']}
    else:
        return {"msg":"Metodo Incorreto!"}

@product_bp.route('/<int:_id>',methods = ['DELETE'])
def deleteProduct_ID(_id):
    if request.method == 'DELETE':
        id=_id
        data = request.get_json()
        return {"msg":data['name'],"msg1":"Product apagado com sucesso"}
    else:
        return {"msg":"Metodo Incorreto!"}
