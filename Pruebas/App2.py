from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Página de inicio"

@app.route('/servicios')
def servicios():
    return "listado de servicios"

@app.route('/Sobre nosotros')
def sobre_nosotros():
    return "información sobre la empresa"

@app.route('/saber más')
def equipo():
    return "información adicional"

@app.route('/contacto')
def contacto():
    return "Formulario de contacto"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

#http://127.0.0.1:5000/saludo/katerin -> se debe usar los slash para ver el resultado en la web#