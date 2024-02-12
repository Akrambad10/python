import sqlite3

conn = sqlite3.connect("example.db")
print("opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (1,'FAITH KARIMI',23,345000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'BOB KURIA',23,15000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'JANE MUTHONI',27,40000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'MARY ANNE',25,945000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'MARK KURIA',34,645000.00)")

conn.commit()
print("records inserted successfully")
conn.close()

