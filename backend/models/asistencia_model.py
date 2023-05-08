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
            content = {'id_asist': result[0], 'fecha': result[1], 'id_horario': result[2], 'id_alumno': result[3],'presente': result[4]}
            data.append(content)
            content = {}
        return data

    def get_asistencias(self):  
        rv = self.PostgreSQL_Pool.execute("SELECT * from asistencia")  
        data = []
        content = {}
        for result in rv:
            content = {'id_asist': result[0], 'fecha': result[1], 'id_horario': result[2], 'id_alumno': result[3],'presente': result[4]}
            data.append(content)
            content = {}
        return data

    def create_asistencia(self, fecha, id_horario,id_alumno,presente):    
        data = {
            'fecha' : fecha,
            'id_horario' : id_horario,
            'id_alumno' : id_alumno,
            'presente' : presente
        }  
        query = """insert into asistencia (fecha, id_horario,id_alumno,presente) 
            values (%(fecha)s, %(id_horario)s, %(id_alumno)s,%(presente)s)"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        data['id_asist'] = cursor.lastrowid
        return data

    def update_asistencia(self, id_asist, fecha, id_horario,id_alumno,presente):    
        data = {
            'id_asist' : id_asist,
            'fecha' : fecha,
            'id_horario' : id_horario,
            'id_alumno' : id_alumno,
            'presente' : presente
        }  
        query = """update asistencia set fecha = %(fecha)s, id_horario = %(id_horario)s, id_alumno = %(id_alumno)s, presente = %(presente)s where id_asist = %(id_asist)s"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_asistencia(self, id_asist):    
        params = {'id_asist' : id_asist}      
        query = """delete from asistencia where id_asist = %(id_asist)s"""    
        self.PostgreSQL_Pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 
 
    def get_vector(self, dni):
        params = {'dni': str(dni)}
        rv = self.PostgreSQL_Pool.execute("SELECT vector FROM usuario WHERE dni = %(dni)s", params)
        data = []
        for result in rv:
            data.append(result[0])
        return data