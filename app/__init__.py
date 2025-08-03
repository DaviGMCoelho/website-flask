from flask import Flask
app = Flask(__name__) # Cria o ambiente do flask
from app import routes
