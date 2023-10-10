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
    cur.execute("SELECT * FROM users WHERE email = %s AND PASSWORD = %s", (email, password))
    user = cur.fetchone()
    cur.close()
    if user:
        return True
    else:
        return False


        
    
