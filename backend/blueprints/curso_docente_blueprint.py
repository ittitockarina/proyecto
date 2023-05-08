from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin
 
from backend.models.curso_docente_model import Curso_Docente_Model
model=Curso_Docente_Model()



curso_docente_blueprint = Blueprint('curso_docente_blueprint', __name__)


@curso_docente_blueprint.route('/curso_docente', methods=['PUT'])
@cross_origin()
def crear_curso_docente():
    content = model.crear_curso_docente(request.json['id_docente'],request.json['id_curso'])    
    return jsonify(content)

@curso_docente_blueprint.route('/curso_docente', methods=['PATCH'])
@cross_origin()
def update_curso_docente():
    content = model.update_curso_docente(request.json['id_docente'],request.json['id_curso'])    
    return jsonify(content)

@curso_docente_blueprint.route('/curso_docente', methods=['DELETE'])
@cross_origin()
def delete_curso_docente():
    return jsonify(model.delete_curso_docente(request.json['id_docente'],request.json['id_curso']))

@curso_docente_blueprint.route('/curso_docente', methods=['POST'])
@cross_origin()
def get_curso_docente():
    return jsonify(model.get_curso_docente(request.json['id_docente'],request.json['id_curso']))

@curso_docente_blueprint.route('/cursos_docentes', methods=['POST'])
@cross_origin()
def get_cursos_docentes():
    return jsonify(model.get_cursos_docentes())