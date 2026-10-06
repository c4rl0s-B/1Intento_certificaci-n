from flask_app import app
from flask import render_template, session, redirect, request,flash
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt #Importamos Bcrypt

bcrypt = Bcrypt(app) #Generamos un objeto llamado bcrypt

@app.route("/registro/crear", methods=["POST"])

def registrar_usuario():
    #En este espacio validarías el formulario
    #Hasheamos la contraseña
    pass_hasheado = bcrypt.generate_password_hash(request.form['password'])
    #Generamos un diccionario con toda la info contraseña hasheada
    data = {
       "nombre": request.form['nombre'],
       "apellido": request.form['apellido'],
       "email": request.form['email'],
       "password": pass_hasheado
    }
    #Invocamos el método para guardar el usuario
    nuevo_id = Usuario.save(data) #Recibiendo el ID del nuevo Usuario
    session['usuario_id'] = nuevo_id #Guardamos en sesión el id del usuario
    Usuario.save(data)
    return redirect('/usuario')

@app.route('/')
def inicio():
    return redirect('/registro')


@app.route('/usuario')
def usuario():

    usuarios = Usuario.get_all()

    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/registro')
def registro():
    return render_template('registro.html')

# @app.route('/registro/crear', methods=['POST'])
# def registrar_usuario():
#     data = {
#         'nombre': request.form['nombre'],
#         'apellido': request.form['apellido'],
#         'email': request.form['email'],
#         'password': request.form['password'],
#         'confirmar': request.form['confirmar']
#     }
#     Usuario.save(data)
#     return redirect('/usuarios')

@app.route("/login", methods=['POST','GET'])

def login():

   #Verificamos que el email exista en BD
    usuario = Usuario.buscar_por_email(request.form)
    if not usuario: #En caso de no estar registrado mandamos mensaje de error
       flash("E-mail no registrado", "login")
       return redirect("/registro")

  

   #Comparamos las contraseñas
    if not bcrypt.check_password_hash(usuario.password, request.form['password']):

        flash("Password incorrecto", "login") #Si no coinciden mandamos mensaje error

        return redirect("/registro")
    session['usuario_id'] = usuario.id #Guardamos en sesión el id del usuario
    return redirect("/usuario")

 





