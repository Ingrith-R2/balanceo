from flask import Flask
servidor = Flask(__name__)
@servidor .route('/')

def hola():
    return "Hola soy el servidor 1"
if __name__ == '__main__':
    servidor .run(host='0.0.0.0')