from backend.models.postgres_connection_pool import PostgreSQLPool

class UsuarioModel:
    def __init__(self):        
        self.mysql_pool = PostgreSQLPool()

    def get_usuario(self, id_usuario):    
        params = {'id_usuario' : id_usuario}      
        rv = self.mysql_pool.execute("SELECT * from usuario where id_usuario=%(id_usuario)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0], 'dni': result[1], 'passw': result[2],'nombre': result[3], 'apellido': result[4], 'email': result[5]}
            data.append(content)
            content = {}
        return data

    def get_usuarios(self):  
        rv = self.mysql_pool.execute("SELECT * from usuario")  
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0], 'dni': result[1], 'passw': result[2],'nombre': result[3], 'apellido': result[4], 'email': result[5]}
            data.append(content)
            content = {}
        return data

    def create_usuario(self, dni, passw,nombre,apellido,email):    
        data = {
            'dni' : dni,
            'passw' : passw,
            'nombre' : nombre,
            'apellido' : apellido,
            'email' : email
        }  
        query = """insert into usuario (dni, passw,nombre,apellido,email) 
            values (%(dni)s, %(passw)s, %(nombre)s, %(apellido)s, %(email)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_usuario'] = cursor.lastrowid
        return data

    def update_usuario(self, id_usuario, dni, passw,nombre,apellido,email):    
        data = {
            'id_usuario' : id_usuario,
            'dni' : dni,
            'passw' : passw,
            'nombre' : nombre,
            'apellido' : apellido,
            'email' : email
        }  
        query = """update usuario set dni = %(dni)s, passw = %(passw)s, nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s
                where id_usuario = %(id_usuario)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_usuario(self, id_usuario):    
        params = {'id_usuario' : id_usuario}      
        query = """delete from usuario where id_usuario = %(id_usuario)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 

