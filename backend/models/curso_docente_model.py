from backend.models.postgres_connection_pool2 import PostgreSQLPool

class Curso_Docente_Model:
    def __init__(self):        
        self.PostgreSQL_Pool = PostgreSQLPool()

    def get_curso_docente(self,id_docente, id_curso):    
        params = {'id_docente' : id_docente,'id_curso' : id_curso}      
        rv = self.PostgreSQL_Pool.execute("SELECT * from curso_docente where id_docente=%(id_docente)s and id_curso=%(id_curso)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_docente': result[0], 'id_curso': result[1]}
            data.append(content)
            content = {}
        return data

    def get_cursos_docentes(self):  
        rv = self.PostgreSQL_Pool.execute("SELECT * from curso_docente")  
        data = []
        content = {}
        for result in rv:
            content = {'id_docente': result[0], 'id_curso': result[1]}
            data.append(content)
            content = {}
        return data

    def crear_curso_docente(self,id_docente, id_curso):    
        data = {
            'id_docente' : id_docente,
            'id_curso' : id_curso
        }  
        query = """insert into curso_docente (id_docente, id_curso ) 
            values (%(id_docente)s, %(id_curso)s)"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        data['id_docente.id_curso'] = cursor.lastrowid
        return data

    def update_curso_docente(self,id_docente, id_curso):    
        data = {
            'id_docente' : id_docente,
            'id_curso' : id_curso
        }  
        query = """update curso_docente set id_docente=%(id_docente)s ,id_curso=%(id_curso)s where id_docente=%(id_docente)s and id_curso=%(id_curso)s"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_curso_docente(self, id_docente, id_curso):    
        params = {'id_docente' : id_docente,
                  'id_curso' : id_curso}      
        query = """delete from curso_docente where id_docente=%(id_docente)s and id_curso=%(id_curso)s"""    
        self.PostgreSQL_Pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 