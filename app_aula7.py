from flask import Flask, redirect,render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import desc

app = Flask(__name__)

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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods= ['GET','POST']) 
def posts():

    if request.method == 'POST': 
        post_title = request.form['title'] 
        post_content = request.form['content']
        post_author = request.form['author']
        new_post =  BlogPost(title=post_title,content=post_content,author=post_author) 
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts') 
    else:
        all_posts = BlogPost.query.order_by(desc(BlogPost.date_posted)).all() 
        return render_template('posts.html', posts=all_posts)

@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id) #get_or_404 tras o erro 404 se não encontrar o id exato
    db.session.delete(post) #deletando o id
    db.session.commit() #gravando no db
    return redirect('/posts') #voltando p pagina '/posts'

@app.route('/posts/editar/<int:id>',methods=['GET','POST']) #Pra editar tem que ter ambos metodos, pq vai editar tbm no db
def editar(id):
    post = BlogPost.query.get_or_404(id) #get_or_404 tras o erro 404 se não encontrar o id exato

    if request.method == 'POST':    
        post.title = request.form['title']
        post.content = request.form['content']
        post.author = request.form['author']
        db.session.commit() #gravando no db
        return redirect('/posts') 
    else:
        return render_template('edit.html', post=post)

if __name__=='__main__':
    app.run(debug=True) 