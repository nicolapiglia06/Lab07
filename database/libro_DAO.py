from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self) -> list[str] | None:
        """
        Recupera la lista dei generi distinti presenti nel database.
        """
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL ORDER BY genere ASC"
        generi = []

        try:
            cursor.execute(query)
            for row in cursor:
                generi.append(row["genere"])
            return generi
        except Exception as e:
            print(f"Errore query get_generi: {e}")
            return None
        finally:
            cursor.close()
            cnx.close()

    def get_libri_filtrati(self, id_biblioteca: int | None = None, genere: str | None = None) -> list[Libro] | None:
        """
        Recupera i libri dal database filtrati per biblioteca e/o genere.
        """
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM libro WHERE 1=1"
        params = []

        if id_biblioteca is not None:
            query += " AND id_biblioteca = %s"
            params.append(id_biblioteca)

        if genere is not None and genere != "":
            query += " AND genere = %s"
            params.append(genere)

        query += " ORDER BY titolo ASC"
        libri = []

        try:
            cursor.execute(query, tuple(params))
            for row in cursor:
                l = Libro(
                    id=row["id"],
                    titolo=row["titolo"],
                    autore=row["autore"],
                    genere=row["genere"],
                    anno_pubblicazione=row["anno_pubblicazione"],
                    id_biblioteca=row["id_biblioteca"]
                )
                libri.append(l)
            return libri
        except Exception as e:
            print(f"Errore query get_libri_filtrati: {e}")
            return None
        finally:
            cursor.close()
            cnx.close()
