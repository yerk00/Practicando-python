from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
""" @app.route #ruta raiz
def index():   #vistas expresadas en forma de funcion
    return " egtrguhse9uhgrgh98ssf9 " #se puedenb retornar etiquetas y distintas cosas como tecto plano osea texto no estructurado
     #"""

# paramewtros para la conexion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'base_datos'

conexion = MySQL(app)


@app.before_request
def before_request():
    print("Antes del request")


@app.after_request
def after_request(response):
    print("Después del request")
    return response


@app.route('/')
def index():
    # return "<h3>tigrreeee</h3>"
    cursos = ['Kotlin', 'Python', 'Java', 'c++', 'Dart', 'JavaScript']
    data = {
        'titulo': 'Index',
        'welcome': 'hol',
        'cursos': cursos,
        'ncursos': len(cursos)
    }
    return render_template('index.html', data=data) # aqui le paso una plantilla o un template que es un html

# para urls dinbamicas o perzonalizada consiste en darles parametros
@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'titulo': 'contact',
        'nombre': nombre,
        'edad': edad
    }
    return render_template('contacto.html', data=data)


def query_string(): # request son las peticiones
    print(request)
    print(request.args)
    print(request.args.get('parametro1'))
    print(request.args.get('parametro2'))
    return "vale"


@app.route('/cursos')
def listar_cursos():
    data = {}
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM curso ORDER BY nombre ASC"
        cursor.execute(sql)
        cursos = cursor.fetchall()
        # print(cursos)
        data['cursos'] = cursos
        data['mensaje'] = 'Exito'
    except Exception as ex:
        data['mensaje'] = 'Error...'
    return jsonify(data)

# para darle forma a un error o algo no encontradoo (personalizado)
def pagina_no_encontrada(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string) #una url dentro de un view
    app.register_error_handler(404, pagina_no_encontrada) #vinculamos el error
    app.run(debug=True, port=5000) # para la depuracion
