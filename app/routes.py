from flask import (
    render_template, request,
    url_for, redirect, session, flash
)
from flask_login import login_required
from app import app
from app import alquimias

# Chave secreta para habilitar sessões no Flask
app.secret_key = 'sua_chave_secreta_aqui'

@app.route('/')
def index():
    username = session.get('username')
    user = {'username': username} if username else None

    posts = []
    if user:
        posts = alquimias.get_timeline()

    return render_template(
        'index.html',
        title='Página Inicial',
        user=user,
        posts=posts
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    mensagem = None
    if request.method == 'POST':
        username = request.form['username'].lower()
        password = request.form['password'].lower()

        if alquimias.validate_user_password(username, password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('Usuário ou senha inválidos!')
            return redirect(url_for('login'))
    
    return render_template('login.html', mmensagem=mensagem)

@app.route('/logout')
def logout():
    # Remove o nome de usuário da sessão
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username'].lower()

        if alquimias.user_exists(username):
            return redirect(url_for('login'))

        password = request.form['password'].lower()
        remember = True if request.form.get('remember') == 'on' else False
        alquimias.create_user(username, password, remember)
        session['username'] = username
        return redirect(url_for('index'))

    return render_template('cadastro.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    if request.method == 'POST':
        texto = request.form['body']
        alquimias.create_post(texto, username)
        return redirect(url_for('index'))

    return render_template('post.html')
