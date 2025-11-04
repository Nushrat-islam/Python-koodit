import requests

def hae_saa(api_avain, kaupunki):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_avain}&lang=fi"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        lampotila_kelvin = data["main"]["temp"]
        lampotila_celsius = lampotila_kelvin - 273.15

        saakuvaus = data["weather"][0]["description"]
        print(f"\nSää paikkakunnalla {kaupunki}: {saakuvaus}")
        print(f"Lämpötila: {lampotila_celsius:.1f} °C")

    except requests.exceptions.HTTPError:
        print("Virhe: Kaupunkia ei löytynyt tai API-avain on virheellinen.")
    except requests.RequestException as e:
        print("Verkkovirhe:", e)
    except KeyError:
        print("Tietoja ei voitu lukea palvelusta.")

if __name__ == "__main__":
    print("=== OpenWeather säätiedot ===")
    api_avain = input("Anna oma OpenWeather API key: ").strip()
    kaupunki = input("Anna paikkakunnan nimi: ").strip()
    hae_saa(api_avain, kaupunki)
