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

app = Flask(__name__)

app.register_blueprint(alumnos_blueprint)
app.register_blueprint(curso_blueprint)
app.register_blueprint(docente_blueprint)
app.register_blueprint(grupo_blueprint)
app.register_blueprint(usuario_blueprint)

cors = CORS(app)

if __name__ == "__main__":
    app.run(debug=True)