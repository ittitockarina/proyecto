from backend.models.postgres_connection_pool import PostgreSQLPool

class UsuarioModel:
    def __init__(self):
        self.mysql_pool = PostgreSQLPool()

    def login(self, DNI, password):
        query = """
            SELECT usuario.id_usuario, usuario.dni, usuario.passw, usuario.foto, usuario.vector,
                   usuario.nombre, usuario.apellido, usuario.email, tipo_usuario.tipo_usuario
            FROM usuario
            INNER JOIN tipo_usuario ON usuario.id_tipo_usuario = tipo_usuario.id_tipo_usuario
            WHERE usuario.dni = %(DNI)s AND usuario.passw = %(password)s
        """
        params = {
            'DNI': DNI,
            'password': password
        }
        rv = self.mysql_pool.execute(query, params)
        data = []
        content = {}
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
            content = {}
        return data

    def get_usuario(self, id_usuario):
        params = {'id_usuario': id_usuario}
        query = """
            SELECT usuario.id_usuario, usuario.dni, usuario.passw, usuario.foto, usuario.vector,
                   usuario.nombre, usuario.apellido, usuario.email, tipo_usuario.tipo_usuario
            FROM usuario
            INNER JOIN tipo_usuario ON usuario.id_tipo_usuario = tipo_usuario.id_tipo_usuario
            WHERE usuario.id_usuario = %(id_usuario)s
        """
        rv = self.mysql_pool.execute(query, params)
        data = []
        content = {}
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
            content = {}
        return data

    def get_usuarios(self):
        query = """
            SELECT usuario.id_usuario, usuario.dni, usuario.passw, usuario.foto, usuario.vector,
                   usuario.nombre, usuario.apellido, usuario.email, tipo_usuario.tipo_usuario
            FROM usuario
            INNER JOIN tipo_usuario ON usuario.id_tipo_usuario = tipo_usuario.id_tipo_usuario
        """
        rv = self.mysql_pool.execute(query)
        data = []
        content = {}
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
            content = {}
        return data

    def create_usuario(self, id_tipo_usuario, dni, passw, foto, vector, nombre, apellido, email):
        data = {
            'id_tipo_usuario': id_tipo_usuario,
            'dni': dni,
            'passw': passw,
            'foto': foto,
            'vector': vector,
            'nombre': nombre,
            'apellido': apellido,
            'email': email
        }
        query = """
            INSERT INTO usuario (id_tipo_usuario, dni, passw, foto, vector, nombre, apellido, email)
            VALUES (%(id_tipo_usuario)s, %(dni)s, %(passw)s, %(foto)s, %(vector)s, %(nombre)s, %(apellido)s, %(email)s)
        """
        cursor = self.mysql_pool.execute(query, data, commit=True)

        data['id_usuario'] = cursor.lastrowid
        return data

    def update_usuario(self, id_usuario, id_tipo_usuario, dni, passw, foto, vector, nombre, apellido, email):
        data = {
            'id_usuario': id_usuario,
            'id_tipo_usuario': id_tipo_usuario,
            'dni': dni,
            'passw': passw,
            'foto': foto,
            'vector': vector,
            'nombre': nombre,
            'apellido': apellido,
            'email': email
        }
        query = """
            UPDATE usuario
            SET id_tipo_usuario = %(id_tipo_usuario)s, dni = %(dni)s, passw = %(passw)s, foto = %(foto)s,
                vector = %(vector)s, nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s
            WHERE id_usuario = %(id_usuario)s
        """
        cursor = self.mysql_pool.execute(query, data, commit=True)

        result = {'result': 1}
        return result

    def delete_usuario(self, dni):    
        params = {'dni' : dni}      
        query = """DELETE FROM usuario WHERE dni = CAST(%(dni)s AS VARCHAR)"""   
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result
