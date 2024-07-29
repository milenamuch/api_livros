from flask import Flask, jsonify, request

app = Flask(__name__) 

livros = [
    {
        'id': 1,
        'título': 'Mindset: A nova psicologia do sucesso',
        'autor': 'Carol S. Dweck',
    },
    {
        'id': 2,
        'título': 'O Pequeno Príncipe',
        'autor': 'Antoine de Saint-Exupéry',
    },
    {
        'id': 3,
        'título': 'Alice no País das Maravilhas',
        'autor': 'Lewis Carroll',
    }
]

#criar
@app.route('/livros/' , methods = ['POST'])
def cadastrar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)


#Visualizar todos os livros
@app.route('/livros/' , methods = ['GET'])
def obter_livros():
    return jsonify(livros)

#Visualizar livro por id
@app.route('/livros/<int:id>' , methods = ['GET'])
def obter_livro_por_id(id):
    
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#Editar
@app.route('/livros/<int:id>' , methods = ['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[i].update(livro_alterado)
            return jsonify(livros[i])
        
#Excluir
@app.route('/livros/<int:id>' , methods = ['DELETE'])
def excluir_livro(id):
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[i]
            
    return jsonify(livros)
        
        
app.run(port=5000,host='localhost', debug= True)