from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
import os  
from flask_cors import CORS, cross_origin

# Configuración de la carpeta de carga de archivos
# app.config['UPLOAD_FOLDER'] = '/home/karolyto/Documentos/2023/softare_construction/proyecto/backend/img'

import numpy as np
import requests

from metodos_temp import MetodosTemp
from backend.models.tipo_usuario_model import TipoUserModel
model = TipoUserModel()

tipo_usuario_blueprint  = Blueprint('tipo_usuario_blueprint', __name__)


@tipo_usuario_blueprint.route('/tipouser', methods=['PUT'])
@cross_origin()
def crear_tipo_user():
    content = model.crear_tipo_user(request.json['tipo_usuario'])    
    return jsonify(content)

@tipo_usuario_blueprint.route('/tipouser', methods=['PATCH'])
@cross_origin()
def update_tipo_user():
    content = model.update_tipo_user(request.json['id_tipo_usuario'], request.json['tipo_usuario'])    
    return jsonify(content)

@tipo_usuario_blueprint.route('/tipouser', methods=['DELETE'])
@cross_origin()
def delete_tipo_user():
    return jsonify(model.delete_tipo_user(int(request.json['id_tipo_usuario'])))

@tipo_usuario_blueprint.route('/tipouser', methods=['POST'])
@cross_origin()
def get_tipo_user():
    return jsonify(model.get_tipo_user(int(request.json['id_tipo_usuario'])))

@tipo_usuario_blueprint.route('/tipousers', methods=['POST'])
@cross_origin()
def get_tipo_users():
    return jsonify(model.get_tipo_users())



