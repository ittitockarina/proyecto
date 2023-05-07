from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 
import numpy as np
import requests
#from .blueprints.functions import *

from backend.models.usuario_model import UsuarioModel
model = UsuarioModel()

######################
''' call openfaceAPI, return vector de   caracteristicas '''
def callOpenFaceAPI(path):
    url = 'http://0.0.0.0:81/openfaceAPI'
    files = {'file': open(path, 'rb')}

    result = requests.post(url, files=files) # abriendo un archivo binario
    result = result.json()
    #print(result)

    return result

######################

def savePath(f):
    # Para guardar momentaneamente la foto para ser procesada
    filename = f.filename
    path  = '/home/karolyto/Documentos/2023/softare_construction/proyecto/backend/img/' + filename
    f.save(path)
    return path

#########################

def toString(string):
    result = string.replace('{','').replace('}','')
    result = list(result.split(','))
    return result

def toFloat(arr):
    vector = []
    for i in arr:
        vector.append(float(i))
    return vector

########################

usuario_blueprint = Blueprint('usuario_blueprint', __name__)
@usuario_blueprint.route('/crear_usuario', methods=['POST'])
@cross_origin()

def crear_usuario():
    global model

    if request.method == 'POST':
        # File and JSON data
        f    = request.files['file']
        data_dni = json.loads(request.form.get('dni'))
        data_passw = json.loads(request.form.get('passw'))
        data_nombre = json.loads(request.form.get('nombre'))
        data_apellido = json.loads(request.form.get('apellido'))
        data_email = json.loads(request.form.get('email'))
       
        ####################################################

        # si queremos guardar la foto, return direccion de la foto   
        path = savePath(f)
        #print(path)

        # callOpenFaceAPI, return vector de caracteristicas ##################################
        result = callOpenFaceAPI(path)
        #print (result)
     
        dni         = data_dni
        passw       = data_passw
        foto        = path
        vector      = toString(result["result"])
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
    
        #db.session.add(new_user)
        #db.session.commit()

    return "ok" #user_schema.jsonify(new_user)

'''
@usuario_blueprint.route('/usuario', methods=['PUT'])
@cross_origin()
def create_usuario():
    content = model.create_usuario(request.json['dni'], request.json['passw'], request.json['foto'],request.json['vector'],request.json['nombre'], request.json['apellido'], request.json['email'])    
    return jsonify(content)
'''

@usuario_blueprint.route('/usuario', methods=['PATCH'])
@cross_origin()
def update_usuario():
    content = model.update_usuario(request.json['id_usuario'],request.json['dni'], request.json['passw'], request.json['foto'],request.json['vector'],request.json['nombre'], request.json['apellido'], request.json['email'])    
    return jsonify(content)

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





