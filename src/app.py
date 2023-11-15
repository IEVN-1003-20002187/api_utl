from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index ():
       titulo='IEVN1003'
       list=['petra','celia','rigoberto'] 
       return render_template('index.html', titulo=titulo, list=list)

@app.route('/Holi')
def Holi():
    return 'Holi nena'

@app.route('/user/<string:user>')
def user(user):
    return 'Holi como te encuentras esta noche preciosa?' + user

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero: {}".format(n)

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "ID : {} Nombre: {}".format(id,username)

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return "La suma es de : {}".format(n1 + n2)
@app.route('/default')
@app.route('/default/<string:n>')
def default(n= 'Karen'):
    return "El nombre o valor de alumno n es " + n


if __name__=='__main__':
    app.run(debug=True)
