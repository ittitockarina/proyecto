from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin
 
from backend.models.alumnos_model import AlumnosModel
model=AlumnosModel()

alumnos_blueprint = Blueprint('alumnos_blueprint', __name__)

@alumnos_blueprint.route('/alumno', methods=['PUT'])
@cross_origin()
def crear_alumno():
    content = model.crear_alumno(request.json['alumno_regular'], request.json['alumno_year'], request.json['id_usuario'])    
    return jsonify(content)

@alumnos_blueprint.route('/alumno', methods=['PATCH'])
@cross_origin()
def update_alumno():
    content = model.update_alumno(request.json['id_alumno'], request.json['alumno_regular'], request.json['alumno_year'], request.json['id_usuario'])    
    return jsonify(content)

@alumnos_blueprint.route('/alumno', methods=['DELETE'])
@cross_origin()
def delete_alumno():
    return jsonify(model.delete_alumno(int(request.json['id_alumno'])))

@alumnos_blueprint.route('/alumno', methods=['POST'])
@cross_origin()
def get_alumno():
    return jsonify(model.get_alumno(int(request.json['id_alumno'])))

@alumnos_blueprint.route('/alumnos', methods=['POST'])
@cross_origin()
def get_alumnos():
    return jsonify(model.get_alumnos())


@alumnos_blueprint.route('/datos', methods=['POST'])
@cross_origin()
def datos_alumnos():
    id_alumno = int(request.json['id_alumno'])
    datos_alumno = model.datos_alumno(id_alumno)
    return jsonify(datos_alumno)


@alumnos_blueprint.route('/todos', methods=['POST'])
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

@alumnos_blueprint.route('/ver_hora', methods=['POST'])
@cross_origin()
def datos():
    query = """
        SELECT a.id_alumno, u.nombre, u.apellido, h.hora_inicio, h.hora_fin, h.dia
        FROM alumno a
        JOIN usuario u ON a.id_usuario = u.id_usuario
        JOIN matricula m ON a.id_alumno = m.id_alumno
        JOIN grupo g ON m.id_grupo = g.id_grupo
        JOIN horario h ON g.id_grupo = h.id_grupo
    """
    rv = model.PostgreSQL_Pool.execute(query)
    data = []
    for result in rv:
        content = {
            'id_alumno': result[0],
            'nombre': result[1],
            'apellido': result[2],
            'hora_inicio': result[3],
            'hora_fin': result[4],
            'dia': result[5]
        }
        data.append(content)
    return jsonify(data)

@alumnos_blueprint.route('/listado', methods=['GET'])
@cross_origin()
def listado():
    query = """
        SELECT h.hora_inicio, h.hora_fin, g.nombre_grupo, c.nombre_curso
        FROM horario h
        JOIN grupo g ON h.id_grupo = g.id_grupo
        JOIN curso c ON g.id_curso = c.id_curso
    """
    rv = model.PostgreSQL_Pool.execute(query)
    data = []
    for result in rv:
        content = {
            'hora_inicio': result[0],
            'hora_fin': result[1],
            'nombre_grupo': result[2],
            'nombre_curso': result[3]
        }
        data.append(content)
    return jsonify(data)

@alumnos_blueprint.route('/aula', methods=['GET'])
@cross_origin()
def obtener_aula():
    query = """
        SELECT c.nombre_curso, g.nombre_grupo, g.aula
        FROM curso c
        JOIN grupo g ON c.id_curso = g.id_curso
    """
    rv = model.PostgreSQL_Pool.execute(query)
    data = []
    for result in rv:
        content = {
            'nombre_curso': result[0],
            'nombre_grupo': result[1],
            'aula': result[2]
        }
        data.append(content)
    return jsonify(data)
