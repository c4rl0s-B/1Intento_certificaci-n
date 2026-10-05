from flask_app import app
from flask import render_template, session, redirect, request
from flask_app.models.usuario import Usuario


@app.route('/registro')
def usuarios():
    return render_template('registro.html')

@app.route('/registro', methods=['POST'])
def registrar_usuario():
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'E-email': request.form['E-email'],
        'password': request.form['password']
    }
    Usuario.save(data)
    return redirect('usuarios')

@app.route('/usuarios')
