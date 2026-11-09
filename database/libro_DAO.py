from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL ORDER BY genere")
        lista_generi = []
        for row in cursor:
            lista_generi.append(row['genere'])
        cursor.close()
        cnx.close()
        return lista_generi


    def get_generi_filtrati(self, biblioteca, genere):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """
                SELECT libro.id, libro.titolo, libro.autore, libro.genere, libro.anno_pubblicazione, libro.id_biblioteca
                FROM libro
                JOIN biblioteca ON libro.id_biblioteca = biblioteca.id
                WHERE biblioteca.nome = COALESCE(%s, biblioteca.nome)
                AND libro.genere = COALESCE(%s, libro.genere)
                ORDER BY libro.titolo"""
        cursor.execute(query, (biblioteca, genere))
        lista_generi_filtrati = []
        for row in cursor:
            lista_generi_filtrati.append(Libro(row['id'],
                                               row['titolo'],
                                               row['autore'],
                                               row['genere'],
                                               row['anno_pubblicazione'],
                                               row['id_biblioteca']))
        cursor.close()
        cnx.close()
        return lista_generi_filtrati




