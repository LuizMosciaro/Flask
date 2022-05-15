from flask import Flask, redirect,render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import desc

app = Flask(__name__)

#Configurando BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(100), nullable=False) 
    content = db.Column(db.Text, nullable=False) 
    author = db.Column(db.String(20), nullable=False, default='N/A') 
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

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

    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods= ['GET','POST']) #default é só 'get'
def posts():

    if request.method == 'POST': #se for 'post' adiciona para o db
        post_title = request.form['title'] #está pegando o que foi escrito no formulario e armazena em uma variavel
        post_content = request.form['content']
        post_author = request.form['author']
        new_post =  BlogPost(title=post_title,content=post_content,author=post_author) #monta o novo objeto
        db.session.add(new_post) #add ao db mas ainda não salva
        db.session.commit() #isso sim salva a alteração
        return redirect('/posts') #redireciona para a mesma pagina que já estava, comando 'redirect'
    else:
        all_posts = BlogPost.query.order_by(desc(BlogPost.date_posted)).all() #da pra configurar por qual organizar com o 'order_by'
        return render_template('posts.html', posts=all_posts)

@app.route('/home/users/<string:name>/posts/<int:id>') 
def hello(name,id):
    return "Hello, "+ name + ". Seu id é: "+ str(id) 

@app.route('/onlyget', methods = ['GET']) 
def get_only():
    return 'Pode receber apenas "get" nessa pagina'

if __name__=='__main__':
    app.run(debug=True) 