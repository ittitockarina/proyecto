from backend.models.postgres_connection_pool2 import PostgreSQLPool
#PostgreSQL_Pool
class ParticipacionModel:
    def __init__(self):        
        self.PostgreSQL_Pool = PostgreSQLPool()

    def get_participacion(self, part_id):    
        params = {'part_id' : part_id}      
        rv = self.PostgreSQL_Pool.execute("SELECT * from participacion where part_id=%(part_id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'part_id': result[0], 'part_fecha': result[1], 'id_horario': result[2], 'id_alumno': result[3],'cantidad': result[4]}
            data.append(content)
            content = {}
        return data

    def get_participaciones(self):  
        rv = self.PostgreSQL_Pool.execute("SELECT * from participacion")  
        data = []
        content = {}
        for result in rv:
            content = {'part_id': result[0], 'part_fecha': result[1], 'id_horario': result[2], 'id_alumno': result[3],'cantidad': result[4]}
            data.append(content)
            content = {}
        return data

    def create_participacion(self, part_fecha, id_horario,id_alumno,cantidad):    
        data = {
            'part_fecha' : part_fecha,
            'id_horario' : id_horario,
            'id_alumno' : id_alumno,
            'cantidad' : cantidad
        }  
        query = """insert into participacion (part_fecha, id_horario,id_alumno,cantidad) 
            values (%(part_fecha)s, %(id_horario)s, %(id_alumno)s,%(cantidad)s)"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        data['part_id'] = cursor.lastrowid
        return data

    def update_participacion(self, part_id, part_fecha, id_horario,id_alumno,cantidad):
        data = {
            'part_id' : part_id,
            'part_fecha' : part_fecha,
            'id_horario' : id_horario,
            'id_alumno' : id_alumno,
            'cantidad' : cantidad
        }  
        query = """update participacion set part_fecha = %(part_fecha)s, id_horario = %(id_horario)s, id_alumno = %(id_alumno)s, cantidad = %(cantidad)s where part_id = %(part_id)s"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   
        result = {'result':1} 
        return result

    def delete_participacion(self, part_id):    
        params = {'part_id' : part_id}      
        query = """delete from participacion where part_id = %(part_id)s"""    
        self.PostgreSQL_Pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 