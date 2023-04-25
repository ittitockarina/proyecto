from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.usuario_model import UsuarioModel
model = UsuarioModel()


usuario_blueprint = Blueprint('usuario_blueprint', __name__)


@usuario_blueprint.route('/usuario', methods=['PUT'])
@cross_origin()
def create_usuario():
    content = model.create_usuario(request.json['dni'], request.json['passw'], request.json['nombre'], request.json['apellido'], request.json['email'])    
    return jsonify(content)

@usuario_blueprint.route('/usuario', methods=['PATCH'])
@cross_origin()
def update_usuario():
    content = model.update_usuario(request.json['id_usuario'],request.json['dni'], request.json['passw'], request.json['nombre'], request.json['apellido'], request.json['email'])    
    return jsonify(content)

@usuario_blueprint.route('/usuario', methods=['DELETE'])
@cross_origin()
def delete_usuario():
    return jsonify(model.delete_usuario(int(request.json['id_usuario'])))

@usuario_blueprint.route('/usuario', methods=['POST'])
@cross_origin()
def get_usuario():
    return jsonify(model.get_usuario(int(request.json['id_usuario'])))

@usuario_blueprint.route('/usuarios', methods=['POST'])
@cross_origin()
def get_usuarios():
    return jsonify(model.get_usuarios())