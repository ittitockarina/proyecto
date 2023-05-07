from backend.models.postgres_connection_pool2 import PostgreSQLPool
#PostgreSQL_Pool
class MatriculaModel:
    def __init__(self):        
        self.PostgreSQL_Pool = PostgreSQLPool()

    def get_matricula(self, matricula_id):    
        params = {'matricula_id' : matricula_id}      
        rv = self.PostgreSQL_Pool.execute("SELECT * from matricula where matricula_id=%(matricula_id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'matricula_id': result[0], 'id_alumno': result[1], 'id_grupo': result[2], 'fecha_matricula': result[3],'estado_matricula': result[4]}
            data.append(content)
            content = {}
        return data

    def get_matriculas(self):  
        rv = self.PostgreSQL_Pool.execute("SELECT * from matricula")  
        data = []
        content = {}
        for result in rv:
            content = {'matricula_id': result[0], 'id_alumno': result[1], 'id_grupo': result[2], 'fecha_matricula': result[3],'estado_matricula': result[4]}
            data.append(content)
            content = {}
        return data

    def create_matricula(self, id_alumno, id_grupo,fecha_matricula,estado_matricula):    
        data = {
            'id_alumno' : id_alumno,
            'id_grupo' : id_grupo,
            'fecha_matricula' : fecha_matricula,
            'estado_matricula' : estado_matricula
        }  
        query = """insert into matricula (id_alumno, id_grupo,fecha_matricula,estado_matricula) 
            values (%(id_alumno)s, %(id_grupo)s, %(fecha_matricula)s,%(estado_matricula)s)"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        data['matricula_id'] = cursor.lastrowid
        return data

    def update_matricula(self, matricula_id, id_alumno, id_grupo,fecha_matricula,estado_matricula): 
        data = {
            'matricula_id' : matricula_id,
            'id_alumno' : id_alumno,
            'id_grupo' : id_grupo,
            'fecha_matricula' : fecha_matricula,
            'estado_matricula' : estado_matricula
        }  
        query = """update matricula set id_alumno = %(id_alumno)s, id_grupo = %(id_grupo)s, fecha_matricula = %(fecha_matricula)s, estado_matricula = %(estado_matricula)s where matricula_id = %(matricula_id)s"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_matricula(self, matricula_id):    
        params = {'matricula_id' : matricula_id}      
        query = """delete from matricula where matricula_id = %(matricula_id)s"""    
        self.PostgreSQL_Pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 