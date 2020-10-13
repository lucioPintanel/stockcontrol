from . import fornecedor_bp
from flask import request, jsonify

'''
Cadastro de fornecedores
'''

@fornecedor_bp.route('/')
def getFornecedor_All():
    return {"msg":"Fornecedor All!"}

@fornecedor_bp.route('/<username>')
def getFornecedor_Name(username):
    # show the user profile for that user
    return {"msg":username}

@fornecedor_bp.route('/<int:_id>',methods = ['POST', 'GET'])
def getProduct_ID(_id):
    if request.method == 'POST':
        id=_id
        data = request.get_json()
        return {"msg":data['name']}
    else:
        return {"msg":_id}

@fornecedor_bp.route('/<int:_id>',methods = ['PUT'])
def putProduct_ID(_id):
    if request.method == 'PUT':
        id=_id
        data = request.get_json()
        return {"msg":data['name']}
    else:
        return {"msg":"Metodo Incorreto!"}

@fornecedor_bp.route('/<int:_id>',methods = ['DELETE'])
def deleteProduct_ID(_id):
    if request.method == 'DELETE':
        id=_id
        data = request.get_json()
        return {"msg":data['name'],"msg1":"Fornecedor apagado com sucesso"}
    else:
        return {"msg":"Metodo Incorreto!"}
