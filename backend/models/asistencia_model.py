from backend.models.postgres_connection_pool import PostgreSQLPool

#PostgreSQL_Pool
class AsistenciaModel:
    def __init__(self):        
        self.PostgreSQL_Pool = PostgreSQLPool()

    def get_asistencia(self, id_asist):    
        params = {'id_asist' : id_asist}      
        rv = self.PostgreSQL_Pool.execute("SELECT * from asistencia where id_asist=%(id_asist)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_asist': result[0], 'asistencia_regular': result[1], 'asistencia_year': result[2]}
            data.append(content)
            content = {}
        return data

    def get_asistencias(self):  
        rv = self.PostgreSQL_Pool.execute("SELECT * from asistencia")  
        data = []
        content = {}
        for result in rv:
            content = {'id_asist': result[0], 'asistencia_regular': result[1], 'asistencia_year': result[2]}
            data.append(content)
            content = {}
        return data

    def crear_asistencia(self, asistencia_regular, asistencia_year):    
        data = {
            'asistencia_regular' : asistencia_regular,
            'asistencia_year' : asistencia_year,
        }  
        query = """insert into asistencia (asistencia_regular, asistencia_year) 
            values (%(asistencia_regular)s, %(asistencia_year)s)"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        data['id_asist'] = cursor.lastrowid
        return data

    def update_asistencia(self, id_asist, asistencia_regular, asistencia_year):    
        data = {
            'id_asist' : id_asist,
            'asistencia_regular' : asistencia_regular,
            'asistencia_year' : asistencia_year,
        }  
        query = """update asistencia set asistencia_regular = %(asistencia_regular)s, asistencia_year = %(asistencia_year)s where id_asist = %(id_asist)s"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_asistencia(self, id_asist):    
        params = {'id_asist' : id_asist}      
        query = """delete from asistencia where id_asist = %(id_asist)s"""    
        self.PostgreSQL_Pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 


