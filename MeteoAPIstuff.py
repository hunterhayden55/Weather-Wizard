import requests

# Example coordinates (replace with user location automatically on website when it asks for location)
lat, lon = 38.64, -121.27  # Sacramento area

# Open-Meteo API endpoint
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,dewpoint_2m,pressure_msl,wind_speed_10m"

# Make the request
response = requests.get(url)
weather_data = response.json()

# Extract current weather details
current_weather = weather_data["current"]

print(f"Temperature: {current_weather['temperature_2m']}°C")
print(f"Dewpoint: {current_weather['dewpoint_2m']}°C")
print(f"Pressure: {current_weather['pressure_msl']} hPa")
print(f"Wind Speed: {current_weather['wind_speed_10m']} m/s")
