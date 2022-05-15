from flask import Flask,render_template 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #chama o template da pagina

@app.route('/home/users/<string:name>/posts/<int:id>') 
def hello(name,id):
    return "Hello, "+ name + ". Seu id é: "+ str(id) 

@app.route('/onlyget', methods = ['GET']) 
def get_only():
    return 'Pode receber apenas "get" nessa pagina'

if __name__=='__main__':
    app.run(debug=True) 