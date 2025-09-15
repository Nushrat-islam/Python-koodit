import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="nushrati_local",
    password="Nushrat2005",
    database="flight_game"
)

cursor = conn.cursor()

icao_code = input("Enter ICAO code: ").upper()

query = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(query, (icao_code,))

result = cursor.fetchone()

if result:
    name, municipality = result
    print(f"Airport Name: {name}")
    print(f"Municipality: {municipality}")
else:
    print("No airport found with that ICAO code.")

cursor.close()
conn.close()