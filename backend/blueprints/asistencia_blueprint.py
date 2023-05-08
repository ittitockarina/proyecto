from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin
import requests
from metodos_temp import MetodosTemp
from backend.models.asistencia_model import AsistenciaModel
model=AsistenciaModel()


asistencia_blueprint = Blueprint('asistencia_blueprint', __name__)


@asistencia_blueprint.route('/asistencia', methods=['PUT'])
@cross_origin()
def create_asistencia():
    content = model.create_asistencia(request.json['fecha'],request.json['id_horario'], request.json['id_alumno'], request.json['presente'])    
    return jsonify(content)

@asistencia_blueprint.route('/asistencia', methods=['PATCH'])
@cross_origin()
def update_asistencia():
    content = model.update_asistencia(request.json['id_asist'],request.json['fecha'],request.json['id_horario'], request.json['id_alumno'], request.json['presente'])    
    return jsonify(content)

@asistencia_blueprint.route('/asistencia', methods=['DELETE'])
@cross_origin()
def delete_asistencia():
    return jsonify(model.delete_asistencia(int(request.json['id_asist'])))

@asistencia_blueprint.route('/asistencia', methods=['POST'])
@cross_origin()
def get_asistencia():
    return jsonify(model.get_asistencia(int(request.json['id_asist'])))

@asistencia_blueprint.route('/asistencias', methods=['POST'])
@cross_origin()
def get_asistencias():
    return jsonify(model.get_asistencias())

@asistencia_blueprint.route('/tomar_asistencia', methods=['POST'])
@cross_origin()
def tomar_asistencia():
    if request.method == 'POST':
        # File and JSON data
        data_dni = json.loads(request.form.get('dni'))
        f    = request.files['file']
        path = MetodosTemp.savePathAsis(f)
        file1 = MetodosTemp.callOpenFaceAPI(path)
        vector2 = MetodosTemp.transformacion(file1)
        vector1 = model.get_vector(data_dni)
        vector1 = MetodosTemp.transformacion2(vector1)
        comprobar = MetodosTemp.Euclides(vector1,vector2)
        if comprobar < 0.5 :
            return "la identidad es verdadera"
        else:
            return "alumno no coincide"
