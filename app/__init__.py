from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Criação da aplicação Flask
app = Flask(__name__)
app.secret_key = 'PD12345678'  # Substitua por uma chave segura em produção

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///microblog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do SQLAlchemy
db = SQLAlchemy(app)

# Inicialização do LoginManager
login = LoginManager(app)
login.login_view = 'login'  # Nome da função que trata o login

# Importações após a criação de app e db
from app.models.models import User  # Ajuste conforme a estrutura do seu projeto
from app import routes

# Carregador de usuário para o Flask-Login
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()
