from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin 

from backend.blueprints.alumnos_blueprint import alumnos_blueprint
from backend.blueprints.curso_blueprint import curso_blueprint
from backend.blueprints.docente_blueprint import docente_blueprint
from backend.blueprints.grupo_blueprint import grupo_blueprint
from backend.blueprints.usuario_blueprint import usuario_blueprint
from backend.blueprints.asistencia_blueprint import asistencia_blueprint
from backend.blueprints.curso_docente_blueprint import curso_docente_blueprint
from backend.blueprints.grupo_docente_blueprint import grupo_docente_blueprint
from backend.blueprints.horario_blueprint import horario_blueprint
from backend.blueprints.justificacion_blueprint import justificacion_blueprint
from backend.blueprints.matricula_blueprint import matricula_blueprint
from backend.blueprints.participacion_blueprint import participacion_blueprint

app = Flask(__name__)

app.register_blueprint(alumnos_blueprint)
app.register_blueprint(curso_blueprint)
app.register_blueprint(docente_blueprint)
app.register_blueprint(grupo_blueprint)
app.register_blueprint(usuario_blueprint)
app.register_blueprint(asistencia_blueprint)
app.register_blueprint(curso_docente_blueprint)
app.register_blueprint(grupo_docente_blueprint)
app.register_blueprint(horario_blueprint)
app.register_blueprint(justificacion_blueprint)
app.register_blueprint(matricula_blueprint)
app.register_blueprint(participacion_blueprint)


cors = CORS(app)

if __name__ == "__main__":
    app.run(debug=True)