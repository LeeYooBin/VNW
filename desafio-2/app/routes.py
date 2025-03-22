from flask import Blueprint, jsonify, request
from app.models import db, Livro

bp = Blueprint("livros", __name__)

@bp.route("/")
def home():
  return "Bem-vindo à API de Livros!", 200

@bp.route("/livros", methods=["POST"])
def cadastrar_livro():
  dados = request.json
  if not all(key in dados for key in ["titulo", "categoria", "autor", "imagem_url"]):
    return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

  novo_livro = Livro(
    titulo=dados["titulo"],
    categoria=dados["categoria"],
    autor=dados["autor"],
    imagem_url=dados["imagem_url"]
  )
  
  db.session.add(novo_livro)
  db.session.commit()

  return jsonify({"mensagem": "Livro cadastrado com sucesso!"}), 201

@bp.route("/livros", methods=["GET"])
def listar_livros():
  livros = Livro.query.all()
  return jsonify([
    {"id": livro.id, "titulo": livro.titulo, "categoria": livro.categoria, "autor": livro.autor, "imagem_url": livro.imagem_url}
    for livro in livros
  ]), 200

@bp.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
  livro = Livro.query.get(id)
  if not livro:
    return jsonify({"erro": "Livro não encontrado"}), 404

  dados = request.json
  livro.titulo = dados.get("titulo", livro.titulo)
  livro.categoria = dados.get("categoria", livro.categoria)
  livro.autor = dados.get("autor", livro.autor)
  livro.imagem_url = dados.get("imagem_url", livro.imagem_url)

  db.session.commit()
  return jsonify({"mensagem": "Livro atualizado com sucesso"}), 200

@bp.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
  livro = Livro.query.get(id)
  if not livro:
    return jsonify({"erro": "Livro não encontrado"}), 404

  db.session.delete(livro)
  db.session.commit()
  return jsonify({"mensagem": "Livro deletado com sucesso"}), 200