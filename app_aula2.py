from flask import Flask

app = Flask(__name__)

@app.route('/home/users/<string:name>/posts/<int:id>') #ou seja, na url digita /home/"Algum nome"

def hello(name,id):
    # Retornará o nome digitado na url no texto da pagina
    return "Hello, "+ name + ", seu id é: "+ str(id) 

@app.route('/onlyget', methods = ['GET']) 
def get_only():
    #Get = envia dados no CABEÇALHO até 255chars
    #Post = envia imagens e dados maiores
    return 'Pode receber apenas "get" nessa pagina'

if __name__=='__main__':
    app.run(debug=True) 