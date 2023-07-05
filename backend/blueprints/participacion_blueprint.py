from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin
 
app = Flask(__name__)
CORS(app, origins="http://localhost:8081")


from backend.models.participacion_model import ParticipacionModel
model=ParticipacionModel()



participacion_blueprint = Blueprint('participacion_blueprint', __name__)

CORS(participacion_blueprint, origins="http://localhost:8081") 

@participacion_blueprint.route('/participacion', methods=['OPTIONS'])
@cross_origin()
def handle_options():
    response = jsonify({'message': 'OK'})
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8081')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    return response

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

@participacion_blueprint.route('/datos_alumnos', methods=['POST'])
@cross_origin()
def datos_todos_alumnos():
    query = """
        SELECT a.id_alumno, u.nombre, u.apellido, c.nombre_curso, p.cantidad
        FROM alumno a
        JOIN usuario u ON a.id_usuario = u.id_usuario
        JOIN matricula m ON a.id_alumno = m.id_alumno
        JOIN grupo g ON m.id_grupo = g.id_grupo
        JOIN curso c ON g.id_curso = c.id_curso
        LEFT JOIN participacion p ON a.id_alumno = p.id_alumno
    """
    rv = model.PostgreSQL_Pool.execute(query)
    data = []
    for result in rv:
        content = {
            'id_alumno': result[0],
            'nombre': result[1],
            'apellido': result[2],
            'nombre_curso': result[3],
            'cantidad_participaciones': result[4]
        }
        data.append(content)
    return jsonify(data)


""" @participacion_blueprint.route('/agregar', methods=['PATCH'])
@cross_origin()
def aumentar_participaciones():
    content = model.aumentar_participaciones(request.json['id_alumno'],request.json['cantidad'])    
    return jsonify(content)

@participacion_blueprint.route('/quitar', methods=['PATCH'])
@cross_origin()
def quitar_participaciones():
    content = model.quitar_participaciones(request.json['id_alumno'],request.json['cantidad'])    
    return jsonify(content) """

@participacion_blueprint.route('/agregar', methods=['PATCH'])
@cross_origin()
def aumentar_participaciones():
    content = model.aumentar_participaciones(request.json['id_alumno'], request.json['cantidad'])
    return jsonify(content)

@participacion_blueprint.route('/quitar', methods=['PATCH'])
@cross_origin()
def quitar_participaciones():
    content = model.quitar_participaciones(request.json['id_alumno'], request.json['cantidad'])
    return jsonify(content)