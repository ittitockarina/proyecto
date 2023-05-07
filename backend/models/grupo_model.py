from backend.models.postgres_connection_pool2 import PostgreSQLPool

class GrupoModel:
    def __init__(self):        
        self.mysql_pool = PostgreSQLPool()

    def get_grupo(self, id_grupo):    
        params = {'id_grupo' : id_grupo}      
        rv = self.mysql_pool.execute("SELECT * from grupo where id_grupo=%(id_grupo)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_grupo': result[0], 'id_curso': result[1], 'nombre_grupo': result[2], 'aula': result[3]}
            data.append(content)
            content = {}
        return data

    def get_grupos(self):  
        rv = self.mysql_pool.execute("SELECT * from grupo")  
        data = []
        content = {}
        for result in rv:
            content = {'id_grupo': result[0], 'id_curso': result[1], 'nombre_grupo': result[2], 'aula': result[3]}
            data.append(content)
            content = {}
        return data

    def create_grupo(self, id_curso, nombre_grupo,aula):    
        data = {
            'id_curso' : id_curso,
            'nombre_grupo' : nombre_grupo,
            'aula' : aula
        }  
        query = """insert into grupo (id_curso, nombre_grupo,aula) 
            values (%(id_curso)s, %(nombre_grupo)s, %(aula)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_grupo'] = cursor.lastrowid
        return data

    def update_grupo(self, id_grupo, id_curso, nombre_grupo,aula):    
        data = {
            'id_grupo' : id_grupo,
            'id_curso' : id_curso,
            'nombre_grupo' : nombre_grupo,
            'aula' : aula
        }  
        query = """update grupo set id_curso = %(id_curso)s, nombre_grupo = %(nombre_grupo)s, aula = %(aula)s
                where id_grupo = %(id_grupo)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_grupo(self, id_grupo):    
        params = {'id_grupo' : id_grupo}      
        query = """delete from grupo where id_grupo = %(id_grupo)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 


