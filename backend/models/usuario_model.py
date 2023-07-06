from backend.models.postgres_connection_pool import PostgreSQLPool
from collections.abc import Mapping, Sequence
from jwt import encode, decode
from jwt import exceptions
from os import getenv
from datetime import datetime, timedelta
from flask import jsonify

class UsuarioModel:
    def __init__(self):        
        self.mysql_pool = PostgreSQLPool()

    def get_usuario(self, id_usuario):    
        params = {'id_usuario' : id_usuario}      
        rv = self.mysql_pool.execute("SELECT * from usuario where id_usuario=%(id_usuario)s", params)
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0], 'id_tipo_usuario': result[1], 'dni': result[2], 'passw': result[3],'foto': result[4],'vector': result[5],'nombre': result[6], 'apellido': result[7], 'email': result[8]}
            data.append(content)
            content = {}
        return data

    def get_usuarios(self):  
        rv = self.mysql_pool.execute("SELECT * from usuario")  
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0], 'id_tipo_usuario': result[1], 'dni': result[2], 'passw': result[3],'foto': result[4],'vector': result[5],'nombre': result[6], 'apellido': result[7], 'email': result[8]}
            data.append(content)
            content = {}
        return data

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




    def update_usuario(self,id_usuario,id_tipo_usuario, dni, passw,nombre,apellido,email):    
        data = {
            'id_usuario' : id_usuario,
            'id_tipo_usuario' : id_tipo_usuario,
            'dni' : dni,
            'passw' : passw,
            'nombre' : nombre,
            'apellido' : apellido,
            'email' : email
        }  
        query = """update usuario set id_tipo_usuario = %(id_tipo_usuario)s, dni = %(dni)s, passw = %(passw)s, nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s
                where id_usuario = %(id_usuario)s """    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_usuario(self, id_usuario):    
        params = {'id_usuario' : id_usuario}      
        query = """delete from usuario where id_usuario = %(id_usuario)s"""   
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 
    
    
    def login(self, DNI, password):
        query = """
            SELECT usuario.id_usuario, usuario.dni, usuario.passw, usuario.foto, usuario.vector,
                usuario.nombre, usuario.apellido, usuario.email, tipo_usuario.tipo_usuario
            FROM usuario
            INNER JOIN tipo_usuario ON usuario.id_tipo_usuario = tipo_usuario.id_tipo_usuario
            WHERE usuario.dni = %(DNI)s AND usuario.passw = %(password)s
        """

        params = {
            'DNI': str(DNI),
            'password': str(password)
        }
        rv = self.mysql_pool.execute(query, params)
        data = []
        for result in rv:
            content = {
                'id_usuario': result[0],
                'dni': result[1],
                'passw': result[2],
                'foto': result[3],
                'vector': result[4],
                'nombre': result[5],
                'apellido': result[6],
                'email': result[7],
                'tipo_usuario': result[8]
            }
            data.append(content)
        return data
    
    def agregar_participacion_alumno(self, id_alumno, cantidad_participaciones):
        query = """
            UPDATE participacion
            SET cantidad = cantidad + %(cantidad_participaciones)s
            WHERE id_alumno = %(id_alumno)s
        """
        data = {
            'id_alumno': id_alumno,
            'cantidad_participaciones': cantidad_participaciones
        }
        self.mysql_pool.execute(query, data, commit=True)
    
   

    def expire_dato(days: int):
            now = datetime.now()
            new_date = now + timedelta(days)
            return new_date
    
    def write_token(data: dict):
            token = encode(payload={**data, "exp": expire_dato(2)},
                        key=getenv("SECRET"), algorithm="HS256")
            return token.encode("UTF-8")


    def generate_token(id_usuario):
        data = {
            "id_usuario": id_usuario
        }
        token = write_token(data)
        return token

    def validate_token(token, output=False):
        try:
            if output:
                return decode(token, key=getenv("SECRET"), algorithms=["HS256"])
            decode(token, key=getenv("SECRET"), algorithms=["HS256"])
        except exceptions.DecodeError:
            response = jsonify({"message": "Invalid Token"})
            response.status_code = 401
            return response
        except exceptions.ExpiredSignatureError:
            response = jsonify({"message": "Token Expired"})
            response.status_code = 401
            return response