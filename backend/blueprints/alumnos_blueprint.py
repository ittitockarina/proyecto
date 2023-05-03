from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin
 
from backend.models.alumnos_model import AlumnoModel
model=AlumnoModel()



alumnos_blueprint = Blueprint('alumnos_blueprint', __name__)


@alumnos_blueprint.route('/alumno', methods=['PUT'])
@cross_origin()
def crear_alumno():
    content = model.crear_alumno(request.json['alumno_regular'], request.json['alumno_year'])    
    return jsonify(content)

@alumnos_blueprint.route('/alumno', methods=['PATCH'])
@cross_origin()
def update_alumno():
    content = model.update_alumno(request.json['id_alumno'], request.json['alumno_regular'], request.json['alumno_year'])    
    return jsonify(content)

@alumnos_blueprint.route('/alumno', methods=['DELETE'])
@cross_origin()
def delete_alumno():
    return jsonify(model.delete_alumno(int(request.json['id_alumno'])))

@alumnos_blueprint.route('/alumno', methods=['POST'])
@cross_origin()
def get_alumno():
    return jsonify(model.get_alumno(int(request.json['id_alumno'])))

@alumnos_blueprint.route('/alumnos', methods=['POST'])
@cross_origin()
def get_alumnos():
    return jsonify(model.get_alumnos())