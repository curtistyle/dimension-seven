from flask import Flask, render_template, request, session, redirect, url_for
from database import consultar_usuario, agregar_usuario, agregar_lista, consultar_lista
from config import SECRET_KEY
from interface import mySpotify
from data_consistency import Consistency



app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
sp = mySpotify()

def estado_usuario():
    """Retorna `True` si el usuario esta en una sesión activo."""
    if len(session.values()) > 0:
        return True
    else:
        return False
    

@app.route("/", methods=['GET'])
def index():
    if estado_usuario(): 
        # Si hay una sesion activa:
        return render_template("index.html",state=True, nickname=session['nickname'])
    else:
        return render_template("index.html",state=False)

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template("login.html") 
    else:
        email = request.form['email']
        password = request.form['password']
        
        alert, nickname, user_id = consultar_usuario(email, password)

        if (alert):
            session['email'] = email
            session['nickname'] = nickname
            session['id'] = user_id
            # Si existe el usuario en la db:
            return redirect(url_for("index"))
        else:
            # Si no existe: 
            return render_template("login.html", alert=alert)
    
@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    if request.method == "GET":
        return render_template("sign_up.html")
    if request.method == "POST":
        nickname = request.form['nickname']
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']
        agregar_usuario(nickname, name, surname, email, password)
        return redirect(url_for("index"))


@app.route("/log_out")
def log_out():
    print("antes: ",len(session.values()))
    session.clear()
    print("despues: ",len(session.values()))
    return redirect(url_for("index"))
        
@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        if estado_usuario():
            return render_template("search.html", state=estado_usuario(), nickname=session['nickname'])
        else:
            return render_template("search.html", state=False)
    if request.method == 'POST':
        if estado_usuario():
            search = request.form['artist']
            data = sp.search(search)
            return render_template("results.html", state=estado_usuario(), nickname=session['nickname'], albums=data, artist=search)
        else:
            search = request.form['artist']
            data = sp.search(search)
            return render_template("results.html", state=False, albums=data, artist=search)
            
@app.route("/create_list", methods=['GET', 'POST'])
def create_list():
    if request.method == 'GET': 
        if estado_usuario():
            return render_template("create_list.html", state=estado_usuario(),alert=None, nickname=session['nickname'])   
    if request.method == 'POST':
        if estado_usuario():
            alert =[False, False, False]
            name = request.form['name']
            description = request.form['description']
            id_user = session['id']
            consistencia = Consistency.agregar_lista(name, description)
            if (consistencia == None):
                # * Si los datos son consistentes, agrega la lista a la base de datos
                if (consultar_lista == False):
                    # ? Si la lista no existe
                    alert[0] = True
                    agregar_lista(id_user, name, description)
                    return render_template("create_list.html", state=estado_usuario(), alert=alert, nickname=session['nickname'], name_list=name, consistencia=consistencia)
                else:
                    # ? Si la lista existe
                    alert[2] = True
                    return render_template("create_list.html", state=estado_usuario(), alert=alert, nickname=session['nickname'], name_list=name, consistencia=consistencia) 
            else:
                # ! Si los datos no son consistentes:
                alert[1] = True
                return render_template("create_list.html", state=estado_usuario(), alert=alert, nickname=session['nickname'], name_list=name, consistencia=consistencia, name=name, description=description)     
    

if __name__=="__main__":
    app.run(debug="True")
    


