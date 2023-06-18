from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
import os  
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, origins="http://localhost:8080")
#cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

# Configuración de la carpeta de carga de archivos
# app.config['UPLOAD_FOLDER'] = '/home/karolyto/Documentos/2023/softare_construction/proyecto/backend/img'

import numpy as np
import requests

from metodos_temp import MetodosTemp
from backend.models.usuario_model import UsuarioModel
model=UsuarioModel()

model = UsuarioModel()

usuario_blueprint = Blueprint('usuario_blueprint', __name__)
CORS(usuario_blueprint, origins="http://localhost:8080") 
@usuario_blueprint.route('/create_usuario', methods=['POST'])
@cross_origin()
def create_usuario():
    global model

    if request.method == 'POST':
        # File and JSON data
        f = request.files['file']
        data_dni = json.loads(request.form.get('dni'))
        data_passw = json.loads(request.form.get('passw'))
        data_nombre = json.loads(request.form.get('nombre'))
        data_apellido = json.loads(request.form.get('apellido'))
        data_email = json.loads(request.form.get('email'))
        data_id_tipo_usuario = json.loads(request.form.get('id_tipo_usuario'))  # New field
        
        # si queremos guardar la foto, return direccion de la foto
        path = MetodosTemp.savePath(f)
        result = MetodosTemp.callOpenFaceAPI(path)

        dni = data_dni
        passw = data_passw
        foto = path
        vector = MetodosTemp.transformacion(result)
        nombre = data_nombre
        apellido = data_apellido
        email = data_email
        id_tipo_usuario = data_id_tipo_usuario  # New field

        new_user = model.create_usuario(
            id_tipo_usuario,  # Pass the new field
            dni,
            passw,
            foto,
            vector,
            nombre,
            apellido,
            email
        )

    return "ok"

@usuario_blueprint.route('/update_usuario', methods=['PATCH'])
@cross_origin()
def update_usuario():
    global model

    if request.method == 'PATCH':
        # File and JSON data
        f = request.files['file']
        data_dni = json.loads(request.form.get('dni'))
        data_passw = json.loads(request.form.get('passw'))
        data_nombre = json.loads(request.form.get('nombre'))
        data_apellido = json.loads(request.form.get('apellido'))
        data_email = json.loads(request.form.get('email'))
        data_id_tipo_usuario = json.loads(request.form.get('id_tipo_usuario'))

        # If you want to save the photo, return the photo's path
        path = MetodosTemp.savePath(f)
        result = MetodosTemp.callOpenFaceAPI(path)

        id_usuario = int(request.form.get('id_usuario'))  # Fix this line
        dni = data_dni
        passw = data_passw
        foto = path
        vector = MetodosTemp.transformacion(result)
        nombre = data_nombre
        apellido = data_apellido
        email = data_email
        id_tipo_usuario = data_id_tipo_usuario

        new_user = model.update_usuario(
            id_usuario,
            id_tipo_usuario,
            dni,
            passw,
            foto,
            vector,
            nombre,
            apellido,
            email
        )

    return "Usuario actualizado"



@usuario_blueprint.route('/delete_usuario', methods=['DELETE'])
@cross_origin()
def delete_usuario():
    return jsonify(model.delete_usuario(request.json['dni']))

@usuario_blueprint.route('/usuario', methods=['POST'])
@cross_origin()
def get_usuario():
    return jsonify(model.get_usuario(int(request.json['id_usuario'])))

@usuario_blueprint.route('/usuarios', methods=['POST'])
@cross_origin()
def get_usuarios():
    return jsonify(model.get_usuarios())
##############################
@usuario_blueprint.route('/login', methods=['POST'])
@cross_origin()
def login():
    global model
    data_dni = request.json['DNI']
    data_passw = request.json['password']
    usuario=model.login(data_dni,data_passw)
    return jsonify(usuario)
  
app.register_blueprint(usuario_blueprint, url_prefix='/usuarios')