from backend.models.postgres_connection_pool2 import PostgreSQLPool
#PostgreSQL_Pool
class JustificacionModel:
    def __init__(self):        
        self.PostgreSQL_Pool = PostgreSQLPool()

    def get_justificacion(self, id_justif):    
        params = {'id_justif' : id_justif}      
        rv = self.PostgreSQL_Pool.execute("SELECT * from justificacion where id_justif=%(id_justif)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_justif': result[0], 'id_asist': result[1], 'fecha': result[2], 'descrip': result[3]}
            data.append(content)
            content = {}
        return data

    def get_justificaciones(self):  
        rv = self.PostgreSQL_Pool.execute("SELECT * from justificacion")  
        data = []
        content = {}
        for result in rv:
            content = {'id_justif': result[0], 'id_asist': result[1], 'fecha': result[2], 'descrip': result[3]}
            data.append(content)
            content = {}
        return data

    def create_justificacion(self, id_asist, fecha,descrip):    
        data = {
            'id_asist' : id_asist,
            'fecha' : fecha,
            'descrip' : descrip
        }  
        query = """insert into justificacion (id_asist, fecha,descrip) 
            values (%(id_asist)s, %(fecha)s, %(descrip)s)"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        data['id_justif'] = cursor.lastrowid
        return data

    def update_justificacion(self, id_justif,id_asist, fecha,descrip):
        data = {
            'id_justif' : id_justif,
            'id_asist' : id_asist,
            'fecha' : fecha,
            'descrip' : descrip
        }  
        query = """update justificacion set id_asist = %(id_asist)s, fecha = %(fecha)s, descrip = %(descrip)s where id_justif = %(id_justif)s"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   
        result = {'result':1} 
        return result

    def delete_justificacion(self, id_justif):    
        params = {'id_justif' : id_justif}      
        query = """delete from justificacion where id_justif = %(id_justif)s"""    
        self.PostgreSQL_Pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 