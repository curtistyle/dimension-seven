from flask import Flask, render_template, request, session
# from flask_mysqldb import MySQL
from database import consultar_usuario
# import config 

app = Flask(__name__)

# app.config['MYSQL_HOST'] = config.MYSQL_HOST
# app.config['MYSQL_USER'] = config.MYSQL_USER
# app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
# app.config['MYSQL_DB'] = config.MYSQL_DB
# app.config['SECRET_KEY'] = config.SECRET_KEY

# db = MySQL(app)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template("login.html") 
    else:
        email = request.form['email']
        password = request.form['password']
        
        alert = consultar_usuario(email, password)
        if (alert):
            # Si existe el usuario en la db:
            return render_template("index.html", state=alert)
        else:
            # Si no existe: 
            return render_template("login.html", alert=alert)
    
@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    if request.method == "GET":
        return render_template("sign_up.html")



if __name__=="__main__":
    app.run(debug="True")


