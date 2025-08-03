from app import app
from flask import render_template

@app.route('/') # Cria rota principal
@app.route('/index') # Cria rotas alternativas
def index(): # Chama função de acordo com decorators
    nome='Recrutador'
    dados={
        'mensagem': 'Sabia que eu tenho um chatbot?'
    }
    return render_template('index.html', nome=nome, dados=dados) # Define um parâmetro
