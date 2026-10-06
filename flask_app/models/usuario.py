from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
        
    def __init__(self, data):
        self.id = data.get('id')
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.email = data.get('email')
        self.password = data.get('password')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);"
        result = connectToMySQL('CinePedia').query_db(query, data)
        return result 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM  usuarios;"
        results = connectToMySQL('CinePedia').query_db(query)
        usuarios = []
        for row in results:
            usuarios.append(cls(row))
        return usuarios

    @classmethod
    def buscar_por_email(cls, datos):
        query = "SELECT * FROM usuarios WHERE email = %(email)s"
        resultados = connectToMySQL('CinePedia').query_db(query, datos)
        if len(resultados) == 1:
           #Si existe el usuario
           usuario = cls(resultados[0])
           return usuario #Regreso la instancia del usuario con ese correo
        else:
           return False

        
        