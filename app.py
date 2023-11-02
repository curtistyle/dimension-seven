from flask import Flask, render_template, request, session, redirect, url_for
from database import consultar_usuario, agregar_usuario, agregar_lista, consultar_lista, obtener_listas, obtener_lista, eliminar_lista, modificar_privacy_en_lista, obtener_usuario, actualizar_usuario
from config import SECRET_KEY
from interface import mySpotify, File, DataMethods
from data_consistency import Consistency, AlertMessages
# from waitress import serve



app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SSL_DISABLE'] = True
sp = mySpotify()

def estado_usuario():
    """Retorna `True` si el usuario esta en una sesión activo."""
    if len(session.values()) > 0:
        return True
    else:
        return False
    

@app.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
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
            lyst_user = obtener_listas(session['id'])
            print(lyst_user)
            return render_template("results.html", state=estado_usuario(), nickname=session['nickname'], albums=data, artist=search, lyst_user=lyst_user)
        else:
            search = request.form['artist']
            data = sp.search(search)
            return render_template("results.html", state=False, albums=data, artist=search)


@app.route("/add_tracks", methods=['GET', 'POST'])
def add_tracks():
    error = []
    if request.method == 'POST':
        if estado_usuario():
            tracks = request.form.getlist('lista')
            lyst_target = request.form.get('select')
            id_list = consultar_lista(session['id'], lyst_target)
            if id_list:
                tracks = DataMethods.format_list(tracks)
                print("TRACKS", tracks)
                File(str(id_list)).data_insert(tracks,error)
                return redirect(url_for("index"))
            else:
                return redirect(url_for("index"))

   
@app.route("/create_list", methods=['GET', 'POST'])
def create_list():
    if request.method == 'GET': 
        if estado_usuario():
            return render_template("create_list.html", state=estado_usuario(),alerts=[], nickname=session['nickname'])   
    if request.method == 'POST':
        if estado_usuario():
            
            name = request.form['name']
            description = request.form['description']
            
            id_lista = consultar_lista( session['id'], name) 
            
            alerts = AlertMessages()._view_list( name, description, id_lista )
            
            if ( id_lista is None ):
                id_lista = agregar_lista( session['id'], name, description )
                File( str( id_lista ) ).fcreate( session['id'], 
                                                name, 
                                                session['email'], 
                                                session['nickname'], 
                                                description )
            
            return render_template( "create_list.html", state=estado_usuario(), alerts=alerts, nickname=session['nickname'], name_list=name, name=name, description=description )
            
  
@app.route("/edit_list", methods=['POST', 'GET'])  
def edit_list():
    if estado_usuario():
        if request.method == 'POST':
            list_target = request.form["edit"]
            session['list_target'] = list_target
            data = File(str(list_target)).get_data() 
            info = File(str(list_target)).get_info()
            return render_template("edit_list.html", state=True, nickname=session['nickname'], data=data, info=info)
        if request.method == 'GET':
            data = File(str(session['list_target'])).get_data() 
            info = File(str(session['list_target'])).get_info()
            return render_template("edit_list.html", state=True, nickname=session['nickname'], data=data, info=info)


@app.route("/edit_profile", methods=['GET', 'POST'])
def edit_profile():
    if estado_usuario():
        if request.method == 'GET':
            
            data_user = obtener_usuario( int(session['id']) )
            
            print(data_user)
            
            return render_template("edit_profile.html", state=True, nickname=session['nickname'], data=data_user[0])
        elif request.method == 'POST':            
            data_user = dict( firs_name=request.form['first_name'], last_name=request.form['last_name'], user_name=request.form['user_name'], role=request.form['role'] )
            
            # actualiza db
            actualizar_usuario( session['id'], data_user['firs_name'], data_user['last_name'], data_user['user_name'], data_user['role'] )
            
            return redirect( url_for("edit_profile") )


@app.route("/save_list", methods=['POST'])  
def save_list():
    if estado_usuario():
        if request.method == 'POST':
            name = request.form['list_name']
            description = request.form['description']
            privacy = request.form.get('btnradio')
            modificar_privacy_en_lista( session['list_target'], privacy )

            lyst = DataMethods.kwargsLists_to_dictionaryList( artist=request.form.getlist('artist'),  
                                                    album=request.form.getlist('album'),
                                                    track=request.form.getlist('track'),
                                                    order=DataMethods.listString_to_listInt(request.form.getlist('order')), 
                                                    time=request.form.getlist('time') )
            File(str(session['list_target'])).overwrite( lyst, name=name, description=description, privacy=privacy )
            # return render_template("edit_list.html", state=True, nickname=session['nickname'], lyst=lyst)  
            return redirect( url_for("edit_list") )
            
@app.route("/view_lists", methods=['GET', 'POST'])
def view_lists():
    if estado_usuario():
        if request.method == 'GET':
            lysts_db = obtener_listas( session['id'] )
            data = File.get_lists( lysts_db )
            return render_template("view_lists.html", state=True, nickname=session['nickname'], data=data)
        
@app.route("/delete_list", methods=['POST'])
def delete_list():
    if estado_usuario():
        if request.method == 'POST':
            name_list = request.form['btn_delete']
            id_list = consultar_lista( session['id'], name_list )
            if id_list is not None:
                eliminar_lista( id_list )
                File(str(id_list)).rename_file(str(id_list) + "_del")
                return redirect(url_for("view_lists"))

@app.route("/test", methods=['GET'])
def test():
    return render_template("test.html")

if __name__=="__main__":
    # app.run(port=5000, host='0.0.0.0', debug=True)
    # serve(app, host='0.0.0.0', port=80, threads=2)
    app.run(debug=True)
    
    


