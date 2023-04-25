from models.postgres_connection_pool import PostgreSQLPool

class DocenteModel:
    def __init__(self):        
        self.mysql_pool = PostgreSQLPool()

    def get_docente(self, id_docente):    
        params = {'id_docente' : id_docente}      
        rv = self.mysql_pool.execute("SELECT * from docente where id_docente=%(id_docente)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_docente': result[0], 'tipo_docente': result[1], 'curso_docente': result[2]}
            data.append(content)
            content = {}
        return data

    def get_docentes(self):  
        rv = self.mysql_pool.execute("SELECT * from docente")  
        data = []
        content = {}
        for result in rv:
            content = {'id_docente': result[0], 'tipo_docente': result[1], 'curso_docente': result[2]}
            data.append(content)
            content = {}
        return data

    def create_docente(self, tipo_docente, curso_docente):    
        data = {
            'tipo_docente' : tipo_docente,
            'curso_docente' : curso_docente
        }  
        query = """insert into docente (tipo_docente, curso_docente) 
            values (%(tipo_docente)s, %(curso_docente)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_docente'] = cursor.lastrowid
        return data

    def update_docente(self, id_docente, tipo_docente, curso_docente):    
        data = {
            'id_docente' : id_docente,
            'tipo_docente' : tipo_docente,
            'curso_docente' : curso_docente
        }  
        query = """update docente set tipo_docente = %(tipo_docente)s, curso_docente = %(curso_docente)s
                where id_docente = %(id_docente)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_docente(self, id_docente):    
        params = {'id_docente' : id_docente}      
        query = """delete from docente where id_docente = %(id_docente)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 

