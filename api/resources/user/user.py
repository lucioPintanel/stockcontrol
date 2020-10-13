from . import user_bp
from flask import request, jsonify

@user_bp.route('/',methods = ['GET'])
def getUser_All():
    return {"msg":"User All!"}

@user_bp.route('/<username>',methods = ['GET'])
def getUser_Name(username):
    # show the user profile for that user
    return {"msg":username}

@user_bp.route('/<int:_id>',methods = ['POST', 'GET'])
def getUser_ID(_id):
    if request.method == 'POST':
        id=_id
        data = request.get_json()
        return {"msg":data['name']}
    else:
        return {"msg":_id}

@user_bp.route('/<int:_id>',methods = ['PUT'])
def putUser_ID(_id):
    if request.method == 'PUT':
        id=_id
        data = request.get_json()
        return {"msg":data['name']}
    else:
        return {"msg":"Metodo Incorreto!"}

@user_bp.route('/<int:_id>',methods = ['DELETE'])
def deleteUser_ID(_id):
    if request.method == 'DELETE':
        id=_id
        data = request.get_json()
        return {"msg":data['name'],"msg1":"Usuario apagado com sucesso"}
    else:
        return {"msg":"Metodo Incorreto!"}
