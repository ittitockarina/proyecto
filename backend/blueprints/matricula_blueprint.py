from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin
 
from backend.models.matricula_model import MatriculaModel
model=MatriculaModel()



matricula_blueprint = Blueprint('matricula_blueprint', __name__)


@matricula_blueprint.route('/matricula', methods=['PUT'])
@cross_origin()
def create_matricula():
    content = model.create_matricula(request.json['id_alumno'],request.json['id_grupo'], request.json['fecha_matricula'], request.json['estado_matricula'])    
    return jsonify(content)

@matricula_blueprint.route('/matricula', methods=['PATCH'])
@cross_origin()
def update_matricula():
    content = model.update_matricula(request.json['matricula_id'],request.json['id_alumno'],request.json['id_grupo'], request.json['fecha_matricula'], request.json['estado_matricula'])    
    return jsonify(content)

@matricula_blueprint.route('/matricula', methods=['DELETE'])
@cross_origin()
def delete_matricula():
    return jsonify(model.delete_matricula(int(request.json['matricula_id'])))

@matricula_blueprint.route('/matricula', methods=['POST'])
@cross_origin()
def get_matricula():
    return jsonify(model.get_matricula(int(request.json['matricula_id'])))

@matricula_blueprint.route('/matriculas', methods=['POST'])
@cross_origin()
def get_matriculas():
    return jsonify(model.get_matriculas())