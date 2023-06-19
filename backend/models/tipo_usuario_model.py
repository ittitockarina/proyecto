from backend.models.postgres_connection_pool import PostgreSQLPool

class TipoUserModel:
    def __init__(self):        
        self.PostgreSQL_Pool = PostgreSQLPool()

    def get_tipo_user(self, id_tipo_usuario):    
        params = {'id_tipo_usuario' : id_tipo_usuario}      
        rv = self.PostgreSQL_Pool.execute("SELECT * from tipo_usuario where id_tipo_usuario=%(id_tipo_usuario)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_tipo_usuario': result[0], 'tipo_usuario': result[1]}
            data.append(content)
            content = {}
        return data

    def get_tipo_users(self):  
        rv = self.PostgreSQL_Pool.execute("SELECT * from tipo_usuario")  
        data = []
        content = {}
        for result in rv:
            content = {'id_tipo_usuario': result[0], 'tipo_usuario': result[1]}
            data.append(content)
            content = {}
        return data

    def crear_tipo_user(self, tipo_usuario):    
        data = {
            'tipo_usuario' : tipo_usuario
        }  
        query = """insert into tipo_usuario (tipo_usuario) 
            values (%(tipo_usuario)s)"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        data['id_tipo_usuario'] = cursor.lastrowid
        return data

    def update_tipo_user(self, id_tipo_usuario, tipo_usuario):    
        data = {
            'id_tipo_usuario' : id_tipo_usuario,
            'tipo_usuario' : tipo_usuario,
        }  
        query = """update tipo_usuario set tipo_usuario = %(tipo_usuario)s where id_tipo_usuario = %(id_tipo_usuario)s"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_tipo_user(self, id_tipo_usuario):    
        params = {'id_tipo_usuario' : id_tipo_usuario}      
        query = """delete from tipo_usuario where id_tipo_usuario = %(id_tipo_usuario)s"""    
        self.PostgreSQL_Pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 