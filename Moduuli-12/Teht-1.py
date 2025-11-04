import requests

def hae_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        print("\nChuck Norris -vitsi:\n")
        print(data["value"])
    except requests.RequestException as e:
        print("Virhe haettaessa vitsiä:", e)

if __name__ == "__main__":
    hae_vitsi()
