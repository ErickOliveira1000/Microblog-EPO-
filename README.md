# Microblog Flask

Este é um projeto de microblog construído com Flask, SQLAlchemy e Flask-Login.

## Funcionalidades

- Cadastro de usuários
- Login com autenticação e "lembrar de mim"
- Criação de posts com corpo de texto e registro de data/hora
- Visualização da timeline com os posts dos usuários
- Logout
- Estilização com HTML e CSS
- Mensagens de erro para login inválido
- Integração com GitHub

## Estrutura de Diretórios

```
microblog/
│
├── app/
│   ├── __init__.py         # Inicialização da aplicação e configuração do Flask
│   ├── models/
│   │   └── models.py       # Modelos do banco de dados (User e Post)
│   ├── templates/          # Arquivos HTML (base.html, index.html, login.html etc.)
│   ├── static/             # Arquivos estáticos (style.css)
│   └── routes.py           # Rotas da aplicação
│
├── venv/                   # Ambiente virtual (não enviado ao GitHub)
├── microblog.py            # Arquivo para rodar a aplicação
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
```

## Como executar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:

- Windows:
```bash
venv\Scripts\activate
```

- Linux/macOS:
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute o servidor:
```bash
python microblog.py
```

6. Acesse o site em [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Licença

Este projeto é apenas para fins educacionais.
