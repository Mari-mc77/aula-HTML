from flask import Flask,request # Importa o flask

app = Flask(__name__) # cria uma instância

@app.route("/", methods=( 'GET',)) # Assina uma rota
def index(): # função responsável pela página
    nome = request.args.get('nome')

    return f"""<h1>Pagina inicial</h1>
        <p>olá {nome}, que nome bonitooo!"""

@app.route("/galeria", methods=( 'GET', )) 
def galeria():
    return "<h1>Galeria</h1>"

@app.route("/contato", methods=( 'GET', )) 
def contato():
    return "<h1>contato</h1>"

@app.route("/sobre", methods=( 'GET', )) 
def sobre():
    return "<h1>sobre</h1>"

