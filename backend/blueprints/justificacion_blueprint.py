from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.justificacion_model import JustificacionModel
model = JustificacionModel()


justificacion_blueprint = Blueprint('justificacion_blueprint', __name__)


@justificacion_blueprint.route('/justificacion', methods=['PUT'])
@cross_origin()
def create_justificacion():
    content = model.create_justificacion(request.json['id_asist'], request.json['fecha'], request.json['descrip']) 
    return jsonify(content)

@justificacion_blueprint.route('/justificacion', methods=['PATCH'])
@cross_origin()
def update_justificacion():
    content = model.update_justificacion(request.json['id_justif'],request.json['id_asist'], request.json['fecha'], request.json['descrip']) 
    return jsonify(content)

@justificacion_blueprint.route('/justificacion', methods=['DELETE'])
@cross_origin()
def delete_justificacion():
    return jsonify(model.delete_justificacion(int(request.json['id_justif'])))

@justificacion_blueprint.route('/justificacion', methods=['POST'])
@cross_origin()
def get_justificacion():
    return jsonify(model.get_justificacion(int(request.json['id_justif'])))

@justificacion_blueprint.route('/justificaciones', methods=['POST'])
@cross_origin()
def get_justificaciones():
    return jsonify(model.get_justificaciones())