from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_word():
    return render_template("index.html")

@app.route('/Acercade')
def Acercade():
    return render_template("about.html")

@app.route('/Articulos/')
def Articulos():
    return ("<h1>Articulos</h1>")

@app.route('/Articulos/<id>')
def lista_articulos(id):
    return "<h1>Consulta de articulos: {}</h1>".format(id)

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Pagina no encontrada en el servidor</h1>"

if __name__ == '__main__':
    app.run(port=80,debug=True)