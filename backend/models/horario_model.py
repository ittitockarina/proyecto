from backend.models.postgres_connection_pool2 import PostgreSQLPool
#PostgreSQL_Pool
class HorarioModel:
    def __init__(self):        
        self.PostgreSQL_Pool = PostgreSQLPool()

    def get_horario(self, id_horario):    
        params = {'id_horario' : id_horario}      
        rv = self.PostgreSQL_Pool.execute("SELECT * from horario where id_horario=%(id_horario)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_horario': result[0], 'id_grupo': result[1], 'hora_inicio': result[2], 'hora_fin': result[3],'dia': result[4]}
            data.append(content)
            content = {}
        return data

    def get_horarios(self):  
        rv = self.PostgreSQL_Pool.execute("SELECT * from horario")  
        data = []
        content = {}
        for result in rv:
            content = {'id_horario': result[0], 'id_grupo': result[1], 'hora_inicio': result[2], 'hora_fin': result[3],'dia': result[4]}
            data.append(content)
            content = {}
        return data

    def create_horario(self, id_grupo, hora_inicio,hora_fin,dia):    
        data = {
            'id_grupo' : id_grupo,
            'hora_inicio' : hora_inicio,
            'hora_fin' : hora_fin,
            'dia' : dia
        }  
        query = """insert into horario (id_grupo, hora_inicio,hora_fin,dia) 
            values (%(id_grupo)s, %(hora_inicio)s, %(hora_fin)s,%(dia)s)"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        data['id_horario'] = cursor.lastrowid
        return data

    def update_horario(self, id_horario, id_grupo, hora_inicio,hora_fin,dia):    
        data = {
            'id_horario' : id_horario,
            'id_grupo' : id_grupo,
            'hora_inicio' : hora_inicio,
            'hora_fin' : hora_fin,
            'dia' : dia
        }  
        query = """update horario set id_grupo = %(id_grupo)s, hora_inicio = %(hora_inicio)s, hora_fin = %(hora_fin)s, dia = %(dia)s where id_horario = %(id_horario)s"""    
        cursor = self.PostgreSQL_Pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_horario(self, id_horario):    
        params = {'id_horario' : id_horario}      
        query = """delete from horario where id_horario = %(id_horario)s"""    
        self.PostgreSQL_Pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 