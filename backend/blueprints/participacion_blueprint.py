from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin
 
from backend.models.participacion_model import ParticipacionModel
model=ParticipacionModel()



participacion_blueprint = Blueprint('participacion_blueprint', __name__)


@participacion_blueprint.route('/participacion', methods=['PUT'])
@cross_origin()
def create_participacion():
    content = model.create_participacion(request.json['part_fecha'],request.json['id_horario'], request.json['id_alumno'], request.json['cantidad'])    
    return jsonify(content)

@participacion_blueprint.route('/participacion', methods=['PATCH'])
@cross_origin()
def update_participacion():
    content = model.update_participacion(request.json['part_id'],request.json['part_fecha'],request.json['id_horario'], request.json['id_alumno'], request.json['cantidad'])    
    return jsonify(content)

@participacion_blueprint.route('/participacion', methods=['DELETE'])
@cross_origin()
def delete_participacion():
    return jsonify(model.delete_participacion(int(request.json['part_id'])))

@participacion_blueprint.route('/participacion', methods=['POST'])
@cross_origin()
def get_participacion():
    return jsonify(model.get_participacion(int(request.json['part_id'])))

@participacion_blueprint.route('/participaciones', methods=['POST'])
@cross_origin()
def get_participaciones():
    return jsonify(model.get_participaciones())