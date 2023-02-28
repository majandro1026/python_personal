
class ConexionSQL:

    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def conexion(user, password, host, database):
        import mysql.connector
        from mysql.connector import errorcode
        try:
            cnx = mysql.connector.connect(
                user = user,
                password = password,
                host = host,
                database = database 
        )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Algo salió mal. Error con tu usuario o contraseña')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('La base de datos no existe')
            else:
                print(err)
        else:
            print('Conexión exitosa')
            cnx.close()

if __name__ == '__main__':
    ConexionSQL.conexion('root', 'Mp1026murci@', 'localhost', 'sakila')
