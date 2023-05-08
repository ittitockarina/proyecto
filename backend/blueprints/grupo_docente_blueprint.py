from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin
 
from backend.models.grupo_docente_model import Grupo_Docente_Model
model=Grupo_Docente_Model()



grupo_docente_blueprint = Blueprint('grupo_docente_blueprint', __name__)


@grupo_docente_blueprint.route('/grupo_docente', methods=['PUT'])
@cross_origin()
def crear_grupo_docente():
    content = model.crear_grupo_docente(request.json['id_docente'],request.json['id_grupo'])    
    return jsonify(content)

@grupo_docente_blueprint.route('/grupo_docente', methods=['PATCH'])
@cross_origin()
def update_grupo_docente():
    content = model.update_grupo_docente(request.json['id_docente'],request.json['id_grupo'])    
    return jsonify(content)

@grupo_docente_blueprint.route('/grupo_docente', methods=['DELETE'])
@cross_origin()
def delete_grupo_docente():
    return jsonify(model.delete_grupo_docente(request.json['id_docente'],request.json['id_grupo']))

@grupo_docente_blueprint.route('/grupo_docente', methods=['POST'])
@cross_origin()
def get_grupo_docente():
    return jsonify(model.get_grupo_docente(request.json['id_docente'],request.json['id_grupo']))

@grupo_docente_blueprint.route('/grupos_docentes', methods=['POST'])
@cross_origin()
def get_grupos_docentes():
    return jsonify(model.get_grupos_docentes())