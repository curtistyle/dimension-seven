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
    cur.close()
    if user:
        return True, user[5], user[0]
    else:
        return False

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
    cur.close()
    if (lista):
        return True
    else:
        return False
    

def agregar_lista(id_user : int, name : str, desciption : str):
    db = conectar_db()
    cur = db.cursor()
    query = "INSERT INTO lists (id_user, name, description) VALUES (%s, %s, %s)"
    values = (id_user, name, desciption)
    cur.execute(query, values)
    db.commit()
    cur.close()
    
