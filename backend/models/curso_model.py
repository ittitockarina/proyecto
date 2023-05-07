from backend.models.postgres_connection_pool2 import PostgreSQLPool

class CursoModel:
    def __init__(self):        
        self.PostgreSQL_Pool = PostgreSQLPool()

    def get_curso(self, id_curso):    
        params = {'id_curso' : id_curso}      
        rv = self.PostgreSQL_Pool.execute("SELECT * from curso where id_curso=%(id_curso)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_curso': result[0], 'nombre_curso': result[1]}
            data.append(content)
            content = {}
        return data

    def get_cursos(self):  
        rv = self.PostgreSQL_Pool.execute("SELECT * from curso")  
        data = []
        content = {}
        for result in rv:
            content = {'id_curso': result[0], 'nombre_curso': result[1]}
            data.append(content)
            content = {}
        return data

    def crear_curso(self, nombre_curso):    
        data = {
            'nombre_curso' : nombre_curso
        }  
        query = """insert into curso (nombre_curso) 
            values (%(nombre_curso)s)"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        data['id_curso'] = cursor.lastrowid
        return data

    def update_curso(self, id_curso, nombre_curso):    
        data = {
            'id_curso' : id_curso,
            'nombre_curso' : nombre_curso,
        }  
        query = """update curso set nombre_curso = %(nombre_curso)s where id_curso = %(id_curso)s"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_curso(self, id_curso):    
        params = {'id_curso' : id_curso}      
        query = """delete from curso where id_curso = %(id_curso)s"""    
        self.PostgreSQL_Pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 