# Simple Weather App
# Gets current weather information for any city using OpenWeatherMap API.
# Written by Malik Talha (or your name)

import requests

print("☁️ Welcome to the Weather App!")

api_key = input("Enter your OpenWeatherMap API key: ")
city = input("Enter the city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        print(f"City not found: {data['message']}")
    else:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\nWeather in {city}:")
        print(f"- Condition: {weather}")
        print(f"- Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"- Humidity: {humidity}%")
        print(f"- Wind Speed: {wind_speed} m/s")

except Exception as e:
    print("An error occurred while fetching the weather. Please try again.")
    print("Error:", e)
