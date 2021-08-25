import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS employee(
    prenom text,
    nom text,
    salaire int
)
""")
d = {"prenom": "Paul", "nom": "Pierre", "salaire": 20000}
c.execute("DELETE FROM employee WHERE prenom=:prenom AND nom=:nom", d)
conn.commit()

d = {"prenom": "Paul"}
c.execute("SELECT * FROM employee WHERE prenom=:prenom", d)
donnees = c.fetchall()
print(donnees)
conn.commit()

conn.close()
