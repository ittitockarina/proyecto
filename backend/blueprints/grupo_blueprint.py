from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.grupo_model import GrupoModel
model = GrupoModel()


grupo_blueprint = Blueprint('grupo_blueprint', __name__)


@grupo_blueprint.route('/grupo', methods=['PUT'])
@cross_origin()
def create_grupo():
    content = model.create_grupo(request.json['id_curso'], request.json['nombre_grupo'], request.json['aula'])    
    return jsonify(content)

@grupo_blueprint.route('/grupo', methods=['PATCH'])
@cross_origin()
def update_grupo():
    content = model.update_grupo(request.json['id_grupo'], request.json['id_curso'], request.json['nombre_grupo'], request.json['aula'])    
    return jsonify(content)

@grupo_blueprint.route('/grupo', methods=['DELETE'])
@cross_origin()
def delete_grupo():
    return jsonify(model.delete_grupo(int(request.json['id_grupo'])))

@grupo_blueprint.route('/grupo', methods=['POST'])
@cross_origin()
def get_grupo():
    return jsonify(model.get_grupo(int(request.json['id_grupo'])))

@grupo_blueprint.route('/grupos', methods=['POST'])
@cross_origin()
def get_grupos():
    return jsonify(model.get_grupos())