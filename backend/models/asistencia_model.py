from backend.models.postgres_connection_pool import PostgreSQLPool

model=AsistenciaModel()
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
            content = {'id_asist': result[0], 'fecha': result[1], 'id_horario': result[2], 'id_alumno': result[3], 'presente': result[4]}
            data.append(content)
            content = {}
        return data

    def get_asistencias(self):  
        rv = self.PostgreSQL_Pool.execute("SELECT * from asistencia")  
        data = []
        content = {}
        for result in rv:
            content = {'id_asist': result[0], 'fecha': result[1], 'id_horario': result[2], 'id_alumno': result[3], 'presente': result[4]}
            data.append(content)
            content = {}
        return data

    def crear_asistencia(self, fecha, id_horario):    
        data = {
            'fecha' : fecha,
            'id_horario' : id_horario,
        }  
        query = """insert into asistencia (fecha, id_horario) 
            values (%(fecha)s, %(id_horario)s)"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        data['id_asist'] = cursor.lastrowid
        return data

    def update_asistencia(self, id_asist, fecha, id_horario):    
        data = {
            'id_asist' : id_asist,
            'fecha' : fecha,
            'id_horario' : id_horario,
        }  
        query = """update asistencia set fecha = %(fecha)s, id_horario = %(id_horario)s where id_asist = %(id_asist)s"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_asistencia(self, id_asist):    
        params = {'id_asist' : id_asist}      
        query = """delete from asistencia where id_asist = %(id_asist)s"""    
        self.PostgreSQL_Pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 


    ####################
    #logica para implementar marcado de easistencia
    ######################

    def asistencia_marcar():
        f = request.files['file']
        usuario=model.get_usuario(int(request.json['dni']))
        path=usuario.path
        path_compare = savePath(f)
        result_usuarioBD = callOpenFaceAPI(path)
        result_comparacion = callOpenFaceAPI(path_compare)

        #para limpiar 
        clean=toString(result_usuarioBD)
        clean2=toString(result_comparacion)

        result_compare=distanciaEuclidiana(toFloat(clean),toFloat(clean2))
        if result_compare<=1:
            model.crear_asistencia("","")
            return "asistencia creada"
        else 
            return"mensaje no son iguales"

        
