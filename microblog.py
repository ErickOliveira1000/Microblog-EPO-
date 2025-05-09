import os
from app import app, db  # Certifique-se de que 'db' é importado do app.__init__.py
import webbrowser
import threading

def open_browser():
    """Abre o navegador automaticamente na URL do servidor."""
    webbrowser.open_new("http://127.0.0.1:5000")

def create_database():
    """Garante que as tabelas do banco de dados sejam criadas."""
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    # Criar o banco de dados (se necessário)
    create_database()

    # Abrir navegador automaticamente após 1.25s
    threading.Timer(1.25, open_browser).start()

    # Iniciar o servidor Flask em modo debug
    app.run(debug=True)


