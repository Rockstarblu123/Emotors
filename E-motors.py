from flask import Flask, render_template, url_for, request, redirect, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from flask_login import LoginManager, login_user, logout_user
from flask_mail import Mail, Message
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User
#holada
motors = Flask(__name__)


# Configuración de la aplicación
motors.config.from_object(config['development'])
motors.config.from_object(config['mail'])
db = MySQL(motors)
mail = Mail(motors)
adminSession = LoginManager(motors)

@adminSession.user_loader
def addUser(id):
    return ModelUser.get_by_id(db, id)

@motors.route('/')
def home():
    return render_template('home.html')

@motors.route('/user')
def user():
    return redirect(url_for('sProducto'))

@motors.route('/admin')
def admin():
    return render_template('admin.html')

@motors.route('/store')
def store():
    return render_template('store.html')

@motors.route('/cart')
def cart():
    return render_template('cart.html')

@motors.route('/moto1')
def moto1():
    return render_template('moto1.html')


@motors.route('/User_page')
def User_page():  # Renombrado para evitar conflicto con la clase User
    return render_template('User.html')

@motors.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        usuario = User(0, None, request.form['correo'], request.form['clave'], None, None)
        usuarioAutenticado = ModelUser.signin(db, usuario)
        
        if usuarioAutenticado is not None:
            if usuarioAutenticado.clave:
                login_user(usuarioAutenticado)
                session['NombreU'] = usuarioAutenticado.nombre
                session['PerfilU'] = usuarioAutenticado.perfil
                
                if usuarioAutenticado.perfil == 'A':
                    return render_template('admin.html')
                else:
                    return render_template('User.html')
            else:
                return 'Contraseña incorrecta'
        else:
            return 'Usuario inexistente'
    else:
        return render_template('signin.html')

@motors.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        claveCifrado = generate_password_hash(clave)
        fechareg = datetime.datetime.now()
        
        regUsuario = db.connection.cursor()
        regUsuario.execute("INSERT INTO usuario (nombre, correo, clave, fechareg) VALUES (%s, %s, %s, %s)", (nombre, correo, claveCifrado, fechareg))
        db.connection.commit()
        mensaje =  Message(subject='welcometo a E-motors', recipients=[correo])
        mensaje.html = render_template('mail.html', nombre = nombre)
        mail.send(mensaje)
        regUsuario.close()
        
        return redirect(url_for('home'))
    else:
        return render_template('signup.html')

@motors.route('/signout', methods=['GET', 'POST'])
def signout():
    logout_user()
    return redirect(url_for('home'))

@motors.route('/sUsuario', methods=['GET', 'POST'])
def sUsuario():
    sUsuario = db.connection.cursor()
    sUsuario.execute("SELECT * FROM usuario")
    U = sUsuario.fetchall()
    sUsuario.close()
    return render_template('usuarios.html', Usuarios=U)

@motors.route('/sMotos', methods=['GET', 'POST'])
def sMotos():
    sMotos = db.connection.cursor()
    sMotos.execute("SELECT * FROM motos")  # Corregido para consultar la tabla correcta
    M = sMotos.fetchall()
    sMotos.close()
    return render_template('motos.html', Motos=M)

if __name__ == '__main__':
    motors.run(port=3300)
