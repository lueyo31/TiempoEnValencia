import requests
import json

# URL de la API
url = "https://api.open-meteo.com/v1/forecast?latitude=39.47&longitude=-0.38&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

# Hacer la petición GET
response = requests.get(url)

# Verificar si la petición fue exitosa
if response.status_code == 200:
    # Guardar la respuesta en un archivo JSON
    with open('time.json', 'w') as file:
        json.dump(response.json(), file, indent=4)
else:
    print(f"Error en la petición: {response.status_code}")