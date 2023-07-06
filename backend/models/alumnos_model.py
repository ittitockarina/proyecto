from backend.models.postgres_connection_pool import PostgreSQLPool


#PostgreSQL_Pool
class AlumnosModel:
    def __init__(self):        
        self.PostgreSQL_Pool = PostgreSQLPool()

    def get_alumno(self, id_alumno):    
        params = {'id_alumno' : id_alumno}      
        rv = self.PostgreSQL_Pool.execute("SELECT * from alumno where id_alumno=%(id_alumno)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_alumno': result[0], 'alumno_regular': result[1], 'alumno_year': result[2], 'id_usuario': result[3]}
            data.append(content)
            content = {}
        return data

    def get_alumnos(self):  
        rv = self.PostgreSQL_Pool.execute("SELECT * from alumno")  
        data = []
        content = {}
        for result in rv:
            content = {'id_alumno': result[0], 'alumno_regular': result[1], 'alumno_year': result[2], 'id_usuario': result[3]}
            data.append(content)
            content = {}
        return data

    def crear_alumno(self, alumno_regular, alumno_year,id_usuario):    
        data = {
            'alumno_regular' : alumno_regular,
            'alumno_year' : alumno_year,
            'id_usuario' : id_usuario
        }  
        query = """insert into alumno (alumno_regular, alumno_year,id_usuario) 
            values (%(alumno_regular)s, %(alumno_year)s, %(id_usuario)s)"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        data['id_alumno'] = cursor.lastrowid
        return data

    def update_alumno(self, id_alumno, alumno_regular, alumno_year,id_usuario):    
        data = {
            'id_alumno' : id_alumno,
            'alumno_regular' : alumno_regular,
            'alumno_year' : alumno_year,
            'id_usuario' : id_usuario
        }  
        query = """update alumno set alumno_regular = %(alumno_regular)s, alumno_year = %(alumno_year)s, id_usuario = %(id_usuario)s where id_alumno = %(id_alumno)s"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_alumno(self, id_alumno):    
        params = {'id_alumno' : id_alumno}      
        query = """delete from alumno where id_alumno = %(id_alumno)s"""    
        self.PostgreSQL_Pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 
    
    def datos_alumno(self, id_alumno):
        params = {'id_alumno': id_alumno}
        query = """
        SELECT a.id_alumno, u.nombre, u.apellido, c.nombre_curso, p.cantidad
        FROM alumno a
        JOIN usuario u ON a.id_usuario = u.id_usuario
        JOIN matricula m ON a.id_alumno = m.id_alumno
        JOIN grupo g ON m.id_grupo = g.id_grupo
        JOIN curso c ON g.id_curso = c.id_curso
        LEFT JOIN participacion p ON a.id_alumno = p.id_alumno
        WHERE a.id_alumno = %(id_alumno)s
        """
        rv = self.PostgreSQL_Pool.execute(query, params)
        data = []
        content = {}
        for result in rv:
            content = {
                'id_alumno': result[0],
                'nombre': result[1],
                'apellido': result[2],
                'nombre_curso': result[3],
                'cantidad_participaciones': result[4]
            }
            data.append(content)
            content = {}
        return data
    
    """ @alumnos_blueprint.route('/datos', methods=['POST'])
    @cross_origin()
    def datos_alumno():
        id_alumno = int(request.json['id_alumno'])
        datos_alumno = model.datos_alumno(id_alumno)
        return jsonify(datos_alumno)  """

 