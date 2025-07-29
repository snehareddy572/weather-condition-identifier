import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        weather_info = data.get("main", {})
        temperature = weather_info.get("temp", "N/A")
        pressure = weather_info.get("pressure", "N/A")
        humidity = weather_info.get("humidity", "N/A")

        weather_list = data.get("weather")
        if weather_list and isinstance(weather_list, list) and len(weather_list) > 0:
            description = weather_list[0].get("description", "No description")
        else:
            description = "No description"

        print(f"\nWeather in {city_name.title()}:")
        print(f"🌡 Temperature: {temperature}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"🧭 Pressure: {pressure} hPa")
        print(f"☁ Description: {description}")

    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            print("❌ Unauthorized: Check your API key.")
        elif response.status_code == 404:
            print("❌ City not found!")
        else:
            print(f"⚠ HTTP error occurred: {e}")
    except Exception as e:
        print(f"⚠ An error occurred: {e}")


api_key = "c020e3d2677a33793715ca637b369481"

city = input("Enter city name: ").strip()
get_weather(city, api_key)
