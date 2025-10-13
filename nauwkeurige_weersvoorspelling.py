import requests

def huidig_weer(lat, lng, city = "stad"):

    open_meteo_uri = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lng}&current=temperature_2m,wind_speed_10m"
    response = requests.get(open_meteo_uri)
    response_data = response.json()

    temp = response_data['current']['temperature_2m']
    temp_unit = response_data['current_units']['temperature_2m']
    wind = response_data['current']['wind_speed_10m']
    wind_unit = response_data['current_units']['wind_speed_10m']

    return f"In {city} is het nu {temp} {temp_unit}. De windsnelheid is {wind} {wind_unit}."
print(huidig_weer(52.0908, 5.1222, "Utrecht" ))
