import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="nushrati_local",
    password="Nushrat2005",
    database="flight_game"
)

cursor = conn.cursor()

country_code = input("Anna maakoodi (esim. FI): ").upper()

query = """
    SELECT type, COUNT(*) 
    FROM airport 
    WHERE iso_country = %s 
    GROUP BY type
"""
cursor.execute(query, (country_code,))

results = cursor.fetchall()
if results:
    print(f"Lentokenttien lukumäärät maassa {country_code}:")
    for airport_type, count in results:
        print(f"{airport_type}: {count}")
else:
    print(f"Maassa {country_code} ei löytynyt lentokenttiä tietokannasta.")

BDcursor.close()
conn.close()
