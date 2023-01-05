from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O pequeno príncipe',
        'autor': 'Antoine de Saint-Exupéry'
    },
    {
        'id': 2,
        'título': 'Arsène Lupin contra Herlock Sholmes',
        'autor': 'Maurice Leblanc'
    },
    {
        'id': 3,
        'título': 'Arsène Lupin o ladrão de casaca',
        'autor': 'Maurice Leblanc'
    },
]

# Consultar (todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)
# Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_por_id(id):
    alteracao = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(alteracao)
            return jsonify(livro[indice])
# Criar
@app.route('/livros', methods=['POST'])
def incluir_livro():
    novo = request.get_json()
    livros.append(novo)
    return jsonify(livros)
# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)