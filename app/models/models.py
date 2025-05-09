from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, DateTime, ForeignKey
from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    remember: Mapped[bool] = mapped_column(Boolean, default=False)
    last_login: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relacionamento com os posts do usuário
    posts: Mapped[list["Post"]] = relationship(
        "Post",
        back_populates="author",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    body: Mapped[str] = mapped_column(String(280), nullable=False)  # limite de 280 caracteres
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    # Relacionamento com o autor (usuário)
    author: Mapped["User"] = relationship("User", back_populates="posts")

    def __repr__(self):
        return f'<Post {self.body[:30]}...>'
