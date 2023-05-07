from backend.models.postgres_connection_pool2 import PostgreSQLPool

class Grupo_Docente_Model:
    def __init__(self):        
        self.PostgreSQL_Pool = PostgreSQLPool()

    def get_grupo_docente(self,id_docente, id_grupo):    
        params = {'id_docente' : id_docente,'id_grupo' : id_grupo}      
        rv = self.PostgreSQL_Pool.execute("SELECT * from grupo_docente where id_docente=%(id_docente)s and id_grupo=%(id_grupo)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_docente': result[0], 'id_grupo': result[1]}
            data.append(content)
            content = {}
        return data

    def get_grupos_docentes(self):  
        rv = self.PostgreSQL_Pool.execute("SELECT * from grupo_docente")  
        data = []
        content = {}
        for result in rv:
            content = {'id_docente': result[0], 'id_grupo': result[1]}
            data.append(content)
            content = {}
        return data

    def crear_grupo_docente(self,id_docente, id_grupo):    
        data = {
            'id_docente' : id_docente,
            'id_grupo' : id_grupo
        }  
        query = """insert into grupo_docente (id_docente, id_grupo ) 
            values (%(id_docente)s, %(id_grupo)s)"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   
        data['id_docente.id_grupo'] = cursor.lastrowid
        return data

    def update_grupo_docente(self,id_docente, id_grupo):    
        data = {
            'id_docente' : id_docente,
            'id_grupo' : id_grupo
        }  
        query = """update grupo_docente set id_docente=%(id_docente)s ,id_grupo=%(id_grupo)s where id_docente=%(id_docente)s and id_grupo=%(id_grupo)s"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_grupo_docente(self, id_docente, id_grupo):    
        params = {'id_docente' : id_docente,
                  'id_grupo' : id_grupo}      
        query = """delete from grupo_docente where id_docente=%(id_docente)s and id_grupo=%(id_grupo)s"""    
        self.PostgreSQL_Pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 