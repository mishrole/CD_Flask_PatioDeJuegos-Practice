from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)

def not_found(e):
    return "<p>¡Lo siento! No hay respuesta. Inténtalo otra vez</p>"

@app.route('/play', methods=['GET'])
def play():
    size = 3
    color = 'blue'
    return render_template("play.html", size=size, color=color)

@app.route('/play/<int:size>', methods=['GET'])
def playSize(size):
    color = 'green'
    return render_template("play.html", size=size, color=color)

@app.route('/play/<int:size>/<color>', methods=['GET'])
def playSizeColor(size, color):
    return render_template("play.html", size=size, color=color)

if __name__ == "__main__":
    app.run( debug = True )