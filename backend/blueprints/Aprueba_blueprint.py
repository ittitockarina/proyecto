from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 
import numpy as np
import requests
from metodos_temp import MetodosTemp
from backend.models.Aprueba_model import ApruebaModel
model = ApruebaModel()

Aprueba_blueprint = Blueprint('Aprueba_blueprint', __name__)

@Aprueba_blueprint.route('/usuario_bp', methods=['PUT'])
@cross_origin()
############################################
def crear_usuario():
    model = UsuarioModel(request, MetodosTemp())

    data_dni = json.loads(request.form.get('dni'))
    data_passw = json.loads(request.form.get('passw'))
    data_nombre = json.loads(request.form.get('nombre'))
    data_apellido = json.loads(request.form.get('apellido'))
    data_email = json.loads(request.form.get('email'))

    dni = data_dni
    passw = data_passw
    foto = request.files['file']
    nombre = data_nombre
    apellido = data_apellido
    email = data_email

    new_user = model.create_usuario(
        dni,
        passw,
        foto,
        vector,
        nombre,
        apellido,
        email
    )

    return "ok"
###########################################
def create_usuario():
    global model

    if request.method == 'PUT':
        # File and JSON data
        f    = request.files['file']
        data_dni = json.loads(request.form.get('dni'))
        data_passw = json.loads(request.form.get('passw'))
        data_nombre = json.loads(request.form.get('nombre'))
        data_apellido = json.loads(request.form.get('apellido'))
        data_email = json.loads(request.form.get('email'))

        # si queremos guardar la foto, return direccion de la foto   
        path = MetodosTemp.savePath(f)
        result = MetodosTemp.callOpenFaceAPI(path)

     
        dni         = data_dni
        passw       = data_passw
        foto        = path
        vector      = MetodosTemp.transformacion(result)
        nombre      = data_nombre
        apellido    = data_apellido 
        email       = data_email

        
        new_user = model.create_usuario(
                        dni,  
                        passw,
                        foto,
                        vector, 
                        nombre,
                        apellido, 
                        email
                        )

    return "ok"

@Aprueba_blueprint.route('/usuario', methods=['PATCH'])
@cross_origin()
def update_usuario():
    content = model.update_usuario(request.json['id_usuario'],request.json['dni'], request.json['passw'], request.json['foto'],request.json['vector'],request.json['nombre'], request.json['apellido'], request.json['email'])    
    return jsonify(content)

@Aprueba_blueprint.route('/usuario', methods=['DELETE'])
@cross_origin()
def delete_usuario():
    return jsonify(model.delete_usuario(int(request.json['id_usuario'])))

@Aprueba_blueprint.route('/usuario', methods=['POST'])
@cross_origin()
def get_usuario():
    return jsonify(model.get_usuario(int(request.json['id_usuario'])))

@Aprueba_blueprint.route('/usuarios', methods=['POST'])
@cross_origin()
def get_usuarios():
    return jsonify(model.get_usuarios())