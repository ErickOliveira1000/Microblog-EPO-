from datetime import datetime
from sqlalchemy import select
from app import db
from app.models.models import Post,User

def validate_user_password(username: str, password: str) -> bool:
    '''Verifica se o nome de usuário e senha conferem com o banco.'''
    query = select(User.password).where(User.username == username)
    result = db.session.scalars(query).first()
    return result == password  # 🔴 Alerta: comparação direta de senha em texto simples

def user_exists(username: str) -> User | None:
    '''Verifica se o usuário existe no banco de dados.'''
    query = select(User).where(User.username == username)
    return db.session.scalars(query).first()

def create_user(username: str, password: str, remember: bool = False, last_login: datetime = None) -> None:
    '''Cria um novo usuário no banco de dados.'''
    new_user = User(
        username=username,
        password=password,  # 🔴 Alerta: senha armazenada em texto simples
        remember=remember,
        last_login=last_login or datetime.utcnow()
    )
    db.session.add(new_user)
    db.session.commit()

def create_post(body, username):
    user = db.session.scalar(select(User).where(User.username == username))
    if user:
        post = Post(body=body, author=user)
        db.session.add(post)
        db.session.commit()

def get_timeline():
    """Retorna os 5 posts mais recentes."""
    return db.session.query(Post).order_by(Post.timestamp.desc()).limit(5).all()