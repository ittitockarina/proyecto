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
CORS(asistencia_blueprint) 

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
        data_dni = request.form.get('dni')
        if data_dni is not None:
            data_dni = json.loads(data_dni)
        
        f = request.files['file']
        path = MetodosTemp.savePathAsis(f)
        file1 = MetodosTemp.callOpenFaceAPI(path)
        vector2 = MetodosTemp.transformacion(file1)
        vector1 = model.get_vector(data_dni)
        vector1 = MetodosTemp.transformacion2(vector1)
        comprobar = MetodosTemp.Euclides(vector1, vector2)
        print(comprobar)
        
        if comprobar < 0.85:
            return "La identidad es verdadera"
        else:
            return "El alumno no coincide"

    #################################################
@asistencia_blueprint.route('/asistencia_hoy', methods=['POST'])
@cross_origin()
def asistencia_hoy():
    id_horario = request.json['id_horario']
    id_alumno = request.json['id_alumno']

    result = model.asistencia_hoy(id_horario, id_alumno)

    if result is not None:
        return jsonify(result)
    else:
        return jsonify({'error': 'No se encontraron datos para los parámetros proporcionados.'})

@asistencia_blueprint.route('/asistencia_hoy', methods=['POST'])
@cross_origin()
def asistencia_hoy_route():
    dni_alumno = request.json['dni_alumno']
    hora = request.json['hora']

    result = model.asistencia_hoy(dni_alumno, hora)

    if result is not None:
        return jsonify(result)
    else:
        return jsonify({'error': 'No se encontraron datos para los parámetros proporcionados.'})

@asistencia_blueprint.route('/toma_asistencia', methods=['POST'])
@cross_origin()
def toma_asistencia():
    if request.method == 'POST':
        # File and JSON data
        data_dni = request.form.get('dni')
        if data_dni is not None:
            data_dni = json.loads(data_dni)
        
        f = request.files['file']
        path = MetodosTemp.savePathAsis(f)
        file1 = MetodosTemp.callOpenFaceAPI(path)
        vector2 = MetodosTemp.transformacion(file1)
        vector1 = model.get_vector(data_dni)
        vector1 = MetodosTemp.transformacion2(vector1)
        
        hora = request.form.get('hora')
        
        result = model.asistencia_valida(data_dni, hora)
        
        if result is not None:
            comprobar = MetodosTemp.Euclides(vector1, vector2)
            print(comprobar)

            if comprobar < 0.85:
                return "La identidad es verdadera"
            else:
                return "El alumno no coincide"
        else:
            return "Estás fuera del horario"


@asistencia_blueprint.route('/toma', methods=['POST'])
@cross_origin()
def toma():
    if request.method == 'POST':
        # File and JSON data
        data_dni = request.form.get('dni')
        if data_dni is not None:
            data_dni = json.loads(data_dni)

        f = request.files['file']
        path = MetodosTemp.savePathAsis(f)
        file1 = MetodosTemp.callOpenFaceAPI(path)
        vector2 = MetodosTemp.transformacion(file1)
        vector1 = model.get_vector(data_dni)
        vector1 = MetodosTemp.transformacion2(vector1)

        fecha = request.form.get('fecha')  # Agregar captura de la fecha
        hora = request.form.get('hora')  # Agregar captura de la hora

        result = model.asistencia_va(data_dni, fecha, hora)  # Actualizar nombre de la función

        if result is not None:
            comprobar = MetodosTemp.Euclides(vector1, vector2)
            print(comprobar)

            if comprobar < 0.85:
                return "La identidad es verdadera"
            else:
                return "El alumno no coincide"
        else:
            return "Estás fuera del horario"
