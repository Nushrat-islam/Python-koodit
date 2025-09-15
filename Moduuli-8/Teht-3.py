import mysql.connector
from geopy.distance import geodesic

conn = mysql.connector.connect(
    host="localhost",
    user="nushrati_local",
    password="Nushrat2005",
    database="flight_game"
)

cursor = conn.cursor()

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ").upper()
icao2 = input("Anna toisen lentokentän ICAO-koodi: ").upper()

query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"

cursor.execute(query, (icao1,))
result1 = cursor.fetchone()

cursor.execute(query, (icao2,))
result2 = cursor.fetchone()

if not result1:
    print(f"Lentokenttää {icao1} ei löytynyt tietokannasta.")
elif not result2:
    print(f"Lentokenttää {icao2} ei löytynyt tietokannasta.")
else:
    coord1 = (result1[0], result1[1])
    coord2 = (result2[0], result2[1])
    
    distance_km = geodesic(coord1, coord2).kilometers
    print(f"Etäisyys {icao1} ja {icao2} välillä: {distance_km:.2f} km")

cursor.close()
conn.close()
