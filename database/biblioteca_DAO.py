from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass
    def get_biblioteche(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT id, nome, indirizzo FROM biblioteca ORDER BY nome")
        lista_biblioteche = []
        for row in cursor:
            lista_biblioteche.append(Biblioteca(row['id'], row['nome'], row['indirizzo']))
        cursor.close()
        cnx.close()
        return lista_biblioteche
