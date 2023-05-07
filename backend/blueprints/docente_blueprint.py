from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.docente_model import DocenteModel
model = DocenteModel()


docente_blueprint = Blueprint('docente_blueprint', __name__)


@docente_blueprint.route('/docente', methods=['PUT'])
@cross_origin()
def create_docente():
    content = model.create_docente(request.json['tipo_docente'],request.json['id_usuario'])    
    return jsonify(content)

@docente_blueprint.route('/docente', methods=['PATCH'])
@cross_origin()
def update_docente():
    content = model.update_docente(request.json['id_docente'], request.json['tipo_docente'],request.json['id_usuario'])    
    return jsonify(content)

@docente_blueprint.route('/docente', methods=['DELETE'])
@cross_origin()
def delete_docente():
    return jsonify(model.delete_docente(int(request.json['id_docente'])))

@docente_blueprint.route('/docente', methods=['POST'])
@cross_origin()
def get_docente():
    return jsonify(model.get_docente(int(request.json['id_docente'])))

@docente_blueprint.route('/docentes', methods=['POST'])
@cross_origin()
def get_docentes():
    return jsonify(model.get_docentes())