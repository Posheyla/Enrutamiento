from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def paginadeInicio():
    return "¡Hola mundo!"

@app.route('/dojo')
def paginadeDojo():
    return "¡Dojo!"

@app.route('/say/<nombre>')
def paginadeSay(nombre):
    print(type(nombre))
    return "¡Hola, " + nombre + "!"

@app.route('/repeat/<int:numero>/<palabra>')
def paginadeRepeat(numero,palabra):
    return render_template("Repeat.html",numero=numero,palabra=palabra)


if __name__ == "__main__":
    app.run(debug=True)

