from flask import Flask

# Crear un objeto flask 
app = Flask(__name__)


@app.route('/')
def index():
    return 'hola 3687386'
