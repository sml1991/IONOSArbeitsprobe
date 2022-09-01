"""
Da wir ausschließlich von SQLite Gebrauch machen wollen,
bietet es sich an, das der SQLite C API näher stehende 
APSW Paket zu nutzen. Muss man natürlich nicht.
Auf SQLAlchemy oder andere Bestien verzichte ich außerdem auch.
"""
from apsw import Connection


class SQLiteDB:
    """    
    Es folgt ein etwas erwzungenes Beispiel für Klassen 
    als "dependable" bzw. aufrufbar gemachter Instanzen.
    Normalerweise würde ich sowas nicht machen - keine Angst.^^
    """
    def __call__(self, cmd: str, values: tuple=None):
        conn = Connection("friends.db")
        cursor = conn.cursor()
        if values:
            return cursor.execute(cmd, values)
        else:
            return cursor.execute(cmd)




