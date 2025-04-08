from .extensions import db

class Livro(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  titulo = db.Column(db.String(100), nullable=False)
  categoria = db.Column(db.String(50), nullable=False)
  autor = db.Column(db.String(100), nullable=False)
  imagem_url = db.Column(db.String(255), nullable=False)
