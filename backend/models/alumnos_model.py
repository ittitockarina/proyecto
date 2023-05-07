from backend.models.postgres_connection_pool2 import PostgreSQLPool
#PostgreSQL_Pool
class UserModel:
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
