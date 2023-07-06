from backend.models.postgres_connection_pool import PostgreSQLPool
from datetime import datetime
from dateutil import parser
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


    def asistencia_hoy(self, id_horario, id_alumno):
        query = """
            SELECT c.nombre_curso, h.hora_inicio, h.hora_fin, g.nombre_grupo, u.nombre, u.apellido, a.presente
            FROM horario h
            JOIN asistencia a ON h.id_horario = a.id_horario
            JOIN alumno al ON a.id_alumno = al.id_alumno
            JOIN grupo g ON h.id_grupo = g.id_grupo
            JOIN curso c ON g.id_curso = c.id_curso
            JOIN usuario u ON al.id_usuario = u.id_usuario
            WHERE h.id_horario = %(id_horario)s
            AND a.id_alumno = %(id_alumno)s
        """

        cursor = self.PostgreSQL_Pool.execute(query, {'id_horario': id_horario, 'id_alumno': id_alumno})
        result = cursor.fetchone()

        if result:
            return {
                'nombre_curso': result[0],
                'hora_inicio': result[1],
                'hora_fin': result[2],
                'nombre_grupo': result[3],
                'nombre': result[4],
                'apellido': result[5],
                'presente': result[6]
            }
        else:
            return None
        
    def asistencia_valida(self, dni_alumno, hora):
        query = """
            SELECT u.nombre, u.apellido, c.nombre_curso, g.aula, h.hora_inicio, h.hora_fin
            FROM horario h
            JOIN asistencia a ON h.id_horario = a.id_horario
            JOIN alumno al ON a.id_alumno = al.id_alumno
            JOIN grupo g ON h.id_grupo = g.id_grupo
            JOIN curso c ON g.id_curso = c.id_curso
            JOIN usuario u ON al.id_usuario = u.id_usuario
            WHERE u.dni = %(dni_alumno)s
            AND h.hora_inicio <= %(hora)s
            AND h.hora_fin >= %(hora)s
        """

        cursor = self.PostgreSQL_Pool.execute(query, {'dni_alumno': dni_alumno, 'hora': hora})
        result = cursor.fetchone()

        if result:
            return {
                'nombre': result[0],
                'apellido': result[1],
                'nombre_curso': result[2],
                'aula': result[3],
                'hora_inicio': result[4].strftime("%H:%M:%S"),
                'hora_fin': result[5].strftime("%H:%M:%S")
            }
        else:
            return None

    


    def asistencia_validas(self, dni_alumno, hora):
        if hora is None:
            return None

        # Eliminar offset de tiempo y zona horaria de la cadena
        hora_sin_offset = hora.split(" GMT")[0]

        formatted_hora = parser.parse(hora_sin_offset).strftime("%Y-%m-%d %H:%M:%S")

        query = """
            SELECT u.nombre, u.apellido, c.nombre_curso, g.aula, h.hora_inicio, h.hora_fin
            FROM horario h
            JOIN asistencia a ON h.id_horario = a.id_horario
            JOIN alumno al ON a.id_alumno = al.id_alumno
            JOIN grupo g ON h.id_grupo = g.id_grupo
            JOIN curso c ON g.id_curso = c.id_curso
            JOIN usuario u ON al.id_usuario = u.id_usuario
            WHERE u.dni = %(dni_alumno)s
                AND h.hora_inicio <= %(hora)s
                AND h.hora_fin >= %(hora)s
        """
        cursor = self.PostgreSQL_Pool.execute(query, {'dni_alumno': dni_alumno, 'hora': formatted_hora})

        result = cursor.fetchone()

        if result:
            return {
                'nombre': result[0],
                'apellido': result[1],
                'nombre_curso': result[2],
                'aula': result[3],
                'hora_inicio': result[4].strftime("%H:%M:%S"),
                'hora_fin': result[5].strftime("%H:%M:%S")
            }
        else:
            return None


    def todas_asistencias(self, id_horario):
        query = """
            SELECT c.nombre_curso, h.hora_inicio, h.hora_fin, g.nombre_grupo, u.nombre, u.apellido, a.presente
            FROM horario h
            JOIN grupo g ON h.id_grupo = g.id_grupo
            JOIN curso c ON g.id_curso = c.id_curso
            JOIN asistencia a ON h.id_horario = a.id_horario
            JOIN alumno al ON a.id_alumno = al.id_alumno
            JOIN usuario u ON al.id_usuario = u.id_usuario
            WHERE h.id_horario = %(id_horario)s
        """
        cursor = self.PostgreSQL_Pool.execute(query, {'id_horario': id_horario})

        results = cursor.fetchall()

        asistencias = []
        for result in results:
            asistencias.append({
                'nombre_curso': result[0],
                'hora_inicio': result[1].strftime("%H:%M:%S"),
                'hora_fin': result[2].strftime("%H:%M:%S"),
                'nombre_grupo': result[3],
                'nombre_alumno': result[4],
                'apellido_alumno': result[5],
                'presente': result[6]
            })

        return asistencias
      