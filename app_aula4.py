from flask import Flask,render_template 

app = Flask(__name__)

#Lista de dicionario, é o que vai alimentar os textos do html
todos_posts = [
    {
        'titulo': 'Post 1',
        'conteudo': 'Isso é o conteúdo 1',
        'autor': 'Luiz Mosciaro'
    },
    {
        'titulo': 'Post 2',
        'conteudo': 'Isso é o conteúdo 2',

    }
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=todos_posts) #chamando a lista

@app.route('/home/users/<string:name>/posts/<int:id>') 
def hello(name,id):
    return "Hello, "+ name + ". Seu id é: "+ str(id) 

@app.route('/onlyget', methods = ['GET']) 
def get_only():
    return 'Pode receber apenas "get" nessa pagina'

if __name__=='__main__':
    app.run(debug=True) 