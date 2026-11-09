from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_tutte_biblioteche(self) -> list[Biblioteca] | None:
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM biblioteca ORDER BY nome ASC"
        biblioteche = []

        try:
            cursor.execute(query)
            for row in cursor:
                b = Biblioteca(
                    id=row["id"],
                    nome=row["nome"],
                    indirizzo=row["indirizzo"]
                )
                biblioteche.append(b)
            return biblioteche
        except Exception as e:
            print(f"Errore query get_tutte_biblioteche: {e}")
            return None
        finally:
            cursor.close()
            cnx.close()
