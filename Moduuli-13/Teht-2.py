import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

def get_airport_by_icao(code):
    conn = sqlite3.connect("airports.db")
    cursor = conn.cursor()

    cursor.execute("SELECT ident, name, municipality FROM airport WHERE ident = ?", (code,))
    row = cursor.fetchone()

    conn.close()
    return row


@app.route("/kentta/<string:icao>")
def airport_api(icao):
    data = get_airport_by_icao(icao.upper())

    if data is None:
        return jsonify({"error": "Airport not found"}), 404

    ident, name, municipality = data

    result = {
        "ICAO": ident,
        "Name": name,
        "Municipality": municipality
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
