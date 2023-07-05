from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
import os  
import numpy as np
import requests
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)
CORS(app, origins="http://localhost:8081")


from metodos_temp import MetodosTemp
from backend.models.usuario_model import UsuarioModel
model=UsuarioModel()

model = UsuarioModel()

usuario_blueprint = Blueprint('usuario_blueprint', __name__)
CORS(usuario_blueprint, origins="http://localhost:8081") 
def create_usuario(self, id_tipo_usuario, dni,passw,foto,vector,nombre,apellido,email):    
        data = {
            'id_tipo_usuario' : id_tipo_usuario,
            'dni' : dni,
            'passw' : passw,
            'foto' : foto,
            'vector' : vector,
            'nombre' : nombre,
            'apellido' : apellido,
            'email' : email
        }  
        query = """insert into usuario (id_tipo_usuario,dni, passw,foto,vector,nombre,apellido,email) 
            values (%(id_tipo_usuario)s,%(dni)s, %(passw)s,%(foto)s,%(vector)s, %(nombre)s, %(apellido)s, %(email)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_usuario'] = cursor.lastrowid
        return data


@usuario_blueprint.route('/usuario', methods=['PUT'])
@cross_origin()
def create_usuario():
    global model

    if request.method == 'PUT':
        # File and JSON data
        f    = request.files['file']
        data_id_tipo_usuario = json.loads(request.form.get('id_tipo_usuario'))
        data_dni = json.loads(request.form.get('dni'))
        data_passw = json.loads(request.form.get('passw'))
        data_nombre = json.loads(request.form.get('nombre'))
        data_apellido = json.loads(request.form.get('apellido'))
        data_email = json.loads(request.form.get('email'))

        # si queremos guardar la foto, return direccion de la foto   
        path = MetodosTemp.savePath(f)
        result = MetodosTemp.callOpenFaceAPI(path)

        id_tipo_usuario = data_id_tipo_usuario
        dni         = data_dni
        passw       = data_passw
        foto        = path
        vector      = MetodosTemp.transformacion(result)
        nombre      = data_nombre
        apellido    = data_apellido 
        email       = data_email

        
        new_user = model.create_usuario(
                        id_tipo_usuario,
                        dni,  
                        passw,
                        foto,
                        vector, 
                        nombre,
                        apellido, 
                        email
                        )

    return "usuario creado"

@usuario_blueprint.route('/usuario', methods=['PATCH'])
@cross_origin()
def update_usuario():
    global model

    if request.method == 'PATCH':
        # File and JSON data
        data_id_usuario = json.loads(request.form.get('id_usuario'))
        data_id_tipo_usuario = json.loads(request.form.get('id_tipo_usuario'))
        data_dni = json.loads(request.form.get('dni'))
        data_passw = json.loads(request.form.get('passw'))
        data_nombre = json.loads(request.form.get('nombre'))
        data_apellido = json.loads(request.form.get('apellido'))
        data_email = json.loads(request.form.get('email'))

        # si queremos guardar la foto, return direccion de la foto   

        id_usuario = data_id_usuario
        id_tipo_usuario = data_id_tipo_usuario
        dni         = data_dni
        passw       = data_passw
        nombre      = data_nombre
        apellido    = data_apellido 
        email       = data_email

        
        new_user = model.update_usuario(
                        id_usuario,
                        id_tipo_usuario,
                        dni,  
                        passw,
                        nombre,
                        apellido, 
                        email
                        )

    return "usuario actualizado"

@usuario_blueprint.route('/usuario', methods=['DELETE'])
@cross_origin()
def delete_usuario():
    return jsonify(model.delete_usuario(int(request.json['id_usuario'])))

@usuario_blueprint.route('/usuario', methods=['POST'])
@cross_origin()
def get_usuario():
    return jsonify(model.get_usuario(int(request.json['id_usuario'])))

@usuario_blueprint.route('/usuarios', methods=['POST'])
@cross_origin()
def get_usuarios():
    return jsonify(model.get_usuarios())

""" @usuario_blueprint.route('/login', methods=['POST'])
@cross_origin()
def login():
    global model
    data_dni = request.json['DNI']
    data_passw = request.json['password']
    usuario=model.login(data_dni,data_passw)
    return jsonify(usuario)
 """
@usuario_blueprint.route('/login', methods=['POST'])
@cross_origin()
def login():
    global model
    data_dni = request.json['DNI']
    data_passw = request.json['password']
    usuario = model.login(data_dni, data_passw)
    return jsonify(usuario)


app.register_blueprint(usuario_blueprint, url_prefix='/usuarios')