from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/perfil/<usuario>")
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=70, debug=True)