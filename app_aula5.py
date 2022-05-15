from flask import Flask,render_template 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#Configurando BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db' #Caminho relativo do bd
db = SQLAlchemy(app) #linkando o nosso app flask com o banco de dados

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True) #criando a coluna do 'id' / colocando uma int unica com o primary key
    title = db.Column(db.String(100), nullable=False) #criando a coluna do titulo / não pode ser nulo
    content = db.Column(db.Text, nullable=False) #sem limite de numero de texto / não pode ser nulo
    author = db.Column(db.String(20), nullable=False, default='N/A') #criando a coluna do conteudo / não pode ser nulo / se for nulo, colocará 'n/a'
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) #criando coluna da data / tempo é utc agora

    #1)Para criar a db fui ao terminal e escrevi 'from app_aula5 import db'(nome desse arquivo + o nome do banco que é 'db')
    #2)Em seguida o comando 'db.create_all()' >>cria o db acima na mesma pasta
    #3)Digitar o comando 'from app_aula5 import BlogPost' >> com o modelo do db
    #4)Digitar 'BlogPost.query.all()' >> faz mostrar tudo do modelo, inicialmente retorna '[]' que é uma lista vazia pq nada foi add
    #5)Para adicionar ao db basta usar o comando 'db.session.add(BlogPost(title = 'Blog Post 1',content = 'Conteudo adbcd', author = 'Eduardo'))' 
    #6)Quando incluir vai printar o que solicitamos no metodo 'def __repr__' ou seja, apenas o self.id
    #7)Para acessar o valor individual da coluna 'title' do db escrever: BlogPost.query.all()[0].title >> retorna o titulo da primeira linha do db (0)
    #7)Caso fosse para acessar o 'author' faria: BlogPost.query.all()[0].author
    #8)


    def __repr__(self):
        return 'Blog post '+str(self.id)
        

todos_posts = [
    {
        'titulo': 'Post 1',
        'conteudo': 'Isso é o conteúdo 1',
        'autor': 'Luiz Mosciaro'
    },
    {
        'titulo': 'Post 2',
        'conteudo': 'Isso é o conteúdo 2',

    },
        {
        'titulo': 'Post 3',
        'conteudo': 'Isso é de FlordeIza',
        'autor':'Iza Mosciaro'

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