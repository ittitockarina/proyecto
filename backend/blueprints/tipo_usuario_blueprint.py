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
from backend.models.tipo_usuario_model import TipoUsuarioModel
model = TipoUsuarioModel()

tipo_usuario_blueprint = Blueprint('tipo_usuario', __name__)

@tipo_usuario_blueprint.route('/tipo_usuario', methods=['PUT'])
@cross_origin()
def crear_tipo_usuario():
    content = model.crear_tipo_usuario(request.json['tipo_usuario'])    
    return jsonify(content)

@tipo_usuario_blueprint.route('/tipo_usuario', methods=['PATCH'])
@cross_origin()
def update_tipo_usuario():
    content = model.update_tipo_usuario(request.json['id_tipo_usuario'], request.json['tipo_usuario'])    
    return jsonify(content)

@tipo_usuario_blueprint.route('/tipo_usuario', methods=['DELETE'])
@cross_origin()
def delete_tipo_usuario():
    return jsonify(model.delete_tipo_usuario(int(request.json['id_tipo_usuario'])))

@tipo_usuario_blueprint.route('/tipo_usuario', methods=['POST'])
@cross_origin()
def get_tipo_usuario():
    return jsonify(model.get_tipo_usuario(int(request.json['id_tipo_usuario'])))

@tipo_usuario_blueprint.route('/tipo_usuarios', methods=['POST'])
@cross_origin()
def get_tipos_usuario():
    return jsonify(model.get_tipos_usuario())



