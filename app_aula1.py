from flask import Flask

app = Flask(__name__) #Chama o flask / __name__ > When you run your script, the __name__ variable equals __main__. When you import the containing script, it will contain the name of the script.

#@ = decorator: modifica o funcionamento da funcao sem modificar ela mesma (a funcao)
@app.route('/') #essa é a pagina inicial
@app.route('/home') #isso é outra url 
def hello():
    return "Hello World"


if __name__=='__main__':
    app.run(debug=True) 