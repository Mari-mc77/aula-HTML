from flask import (Flask, request,render_template) #Importa o flask

app = Flask(__name__) #Cria uma instância

@app.route("/", methods=('GET' ,)) #Assina uma rota
def index (): #Função responsavel pela página
    nome = request.args.get('nome')
    #HTML retornado
    return f"""<h1>Pagina Inicial</h1> 
    <p>Olá {nome}, que nome bonito!"""

@app.route("/outra_pagina", methods=( 'GET', )) 
def outra():
   return "<h1>Outra página</h1>"

@app.route("/galeria", methods=('GET',))
def galeria():
    return "<h1>GALERIA</h1>" 

@app.route("/contato", methods=('GET',))
def contato():
    return "<h1>CONTATO</h1>" 

@app.route("/sobre", methods=('GET',))
def sobre():
    return "<h1>Sobre...</h1>" 

@app.route("/area/<float:largura>/<float:altura>", methods=( 'GET', ))
def area(largura: float, altura: float):
    return f"""<h1> A área
    informada >L={largura} * A={altura}
    => Area={largura*altura}</h1>"""

@app.route("/parimpar/<float:numero>", methods=('GET',))
def par_ou_impar(numero):
  if numero % 2 == 0:
    return f"O número {numero} é par."
  else:
    return f"O número {numero} é ímpar."
  
@app.route("/sobrenome/<string:nome>/<string:sobrenome>", methods=('GET',))
def nomesobrenome(nome: str, sobrenome: str):
  return f"""<h1> sobrenome </h1>
  <p>{sobrenome},{nome}</p>"""

@app.route("/potencia/<float:um>/<float:dois>", methods=( 'GET', ))
def potencia(um: float, dois: float):
    return f"""<h1>{um}^{dois}
     ={um**dois}</h1>"""



@app.route("/tabuada")
@app.route("/tabuada/<numero>", methods=("GET", ))
def tabuada (numero = None): # None desobriga o valor

  if 'numero' in request.args: # se argumento existir
      numero =int (request. args.get('numero')) # atualiza numero
  
  return render_template('tabuada.html', numero=numero)
 
@app.route("/juros", methods=('GET', 'POST'))
def calculo_juros():
    if request.method == 'POST':
        investimento = float(request.form['investimento'])
        juros_anuais = float(request.form['juros']) / 100
        tempo_meses = int(request.form['tempo'])
        contribuicao = float(request.form['contribuicao'])

        montante = investimento
        for mes in range(tempo_meses):
            montante += contribuicao
            montante *= (1 + juros_anuais / 12)

        return f'Valor final após {tempo_meses} meses: R$ {montante:.2f}'

    return render_template('juros.html')

@app.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        if email == 'aluno@senai.br' and senha == 'senai':
            return '<h1>Usuário Logado com Sucesso!</h1>'
        else:
            return '<h1>Usuário ou senha incorretos. Tente novamente.</h1>'

    return render_template('login.html')

@app.route("/imc", methods=('GET', 'POST'))
def calcular_imc():
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])
            altura = float(request.form['altura'])
            imc = peso / (altura ** 2)

            if imc < 18.5:
                classificacao = 'Magreza'
                grau_obesidade = 0
            elif 18.5 <= imc <= 24.9:
                classificacao = 'Normal'
                grau_obesidade = 0
            elif 25.0 <= imc <= 29.9:
                classificacao = 'Sobrepeso'
                grau_obesidade = 1
            elif 30.0 <= imc <= 39.9:
                classificacao = 'Obesidade'
                grau_obesidade = 2
            else:
                classificacao = 'Obesidade Grave'
                grau_obesidade = 3

            return f'''
                <h1>Seu IMC é: {imc:.2f}</h1>
                <h2>Classificação: {classificacao}</h2>
                <h2>Grau de Obesidade: {grau_obesidade}</h2>
            '''
        except ValueError:
            return '<h1>Erro: Por favor insira valores válidos para peso e altura.</h1>'
    
    return render_template('imc.html')
