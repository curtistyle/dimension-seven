from mysql import connector
from mysql.connector import Error
import config

def conectar_db():
    connection = None
    try:
        connection = connector.connect(
            host=config.MYSQL_HOST,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            database=config.MYSQL_DB
        )
        print("Conexion a la Base de Datos MySQL exitosa.")
    except Error as e:
        print(f"Ha ocurrido un error: '{e}'")
    return connection


def consultar_usuario(email : str, password : str):
    """Retorna `True` si el usuario existe en la base de datos"""
    db = conectar_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cur.fetchone()
    print( f"{user=}" )
    cur.close()
    if user:
        return True, user[5], user[0]
    else:
        return False

def obtener_usuario( id_user : int ):
    db = conectar_db()
    cur = db.cursor()
    query = "SELECT * FROM users WHERE id = %s"
    values = (id_user, )
    cur.execute(query, values)
    user = cur.fetchall()
    cur.close()
    return user

def agregar_usuario(nickname, name, surname, email, password):
    db = conectar_db()
    cur = db.cursor()
    query = "INSERT INTO users (email, password, name, surname, nick_name) VALUES (%s, %s, %s, %s, %s)"
    values = (email, password, name, surname, nickname)
    cur.execute(query, values)
    db.commit()
    cur.close()   


def consultar_lista(id_user : int, name : str):
    db = conectar_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM lists WHERE id_user = %s AND name = %s", (id_user, name))
    lista = cur.fetchone()
    db.close()
    print("lista: ", lista)
    if (lista):
        return lista[0]
    else:
        return None
    
def obtener_listas(id_user):
    db = conectar_db()
    cur = db.cursor()
    cur.execute("SELECT id, name FROM lists WHERE id_user = %s", (id_user,))
    data = cur.fetchall()
    db.close()
    if data:
        return data
    else:
        return None
    
def obtener_lista(id_user : int, id_lista):
    db = conectar_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM lists WHERE id = %s AND id_user = %s", (id_lista, id_user))
    data = cur.fetchone()
    db.close()
    if data: 
        return data
    else:
        return None

def agregar_lista(id_user : int, name : str, desciption : str):
    db = conectar_db()
    cur = db.cursor()
    query = "INSERT INTO lists (id_user, name, description) VALUES (%s, %s, %s)"
    values = (id_user, name, desciption)
    cur.execute(query, values)
    nuevo_id = cur.lastrowid
    db.commit()
    
    return nuevo_id
    
def eliminar_lista( id_list : int ):
    db = conectar_db()
    cur = db.cursor()

    cur.execute("DELETE FROM lists WHERE id=%s", (id_list, ))
    db.commit()
    
    
def modificar_privacy_en_lista( id_list : int, despues : str ):
    db = conectar_db()
    cur = db.cursor()
    query = f"UPDATE lists SET privacy = '{despues}' WHERE id = '{id_list}'"
    cur.execute( query )
    db.commit()
    print( cur.rowcount, " record(s) affected")
    

def actualizar_usuario( id_user : int, first_name : str, last_name : str, nickname : str , role : str ):
    db = conectar_db()
    cur = db.cursor()
    query = "UPDATE users SET name = %s, surname = %s, nick_name = %s, role = %s WHERE id = %s"
    values = ( first_name, last_name, nickname, role, id_user )
    print( f"{query}" )
    cur.execute( query, values )
    db.commit()
    
    print( cur.rowcount, " record(s) affected")