from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
        
    def __init__(self, data):
        self.id = data.get('id')
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.email = data.get('E-email')
        self.password = data.get('password')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

        @classmethod
        def save(cls, data):
            query = "INSERT INTO usuarios (nombre, apellido, E-email, password) VALUES (%(nombre)s, %(apellido)s, %(E-email)s, %(password)s);"
            result = connectToMySQL('peliculas').query_db(query, data)
            return result 