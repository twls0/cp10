from flask import Flask, render_template, request
import formulario, os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def main():
    formulario1 = formulario.formularioWTF()
    return render_template('index.html',formulario1=formulario1)

@app.route('/recibido', methods=['POST'])
def recibido():
    print(request.form)
    return 'ok'