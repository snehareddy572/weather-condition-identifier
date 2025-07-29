import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    full_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    response = requests.get(full_url)
    data = response.json()

    print(data)  # 👈 ADD THIS LINE RIGHT HERE to see the full API response

    if data.get("cod") != 404:
        weather_info = data.get("main", {})
        temperature = weather_info.get("temp")
        pressure = weather_info.get("pressure")
        humidity = weather_info.get("humidity")
        description = data.get("weather", [{}])[0].get("description", "No description")

        print(f"\nWeather in {city_name.title()}:")
        print(f"🌡 Temperature: {temperature}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"🧭 Pressure: {pressure} hPa")
        print(f"☁ Description: {description}")
    else:
        print("❌ City not found!")

# Replace with your OpenWeatherMap API key
api_key = "661a9591c3344072b9781844251507"

city = input("Enter city name: ")
get_weather(city, api_key)
