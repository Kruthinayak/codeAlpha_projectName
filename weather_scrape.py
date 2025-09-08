import requests
from bs4 import BeautifulSoup

def get_weather(city):
    url = f"https://www.timeanddate.com/weather/india/{city.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        print("City not found or site unavailable.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    try:
        temp = soup.find("div", class_="h2").text.strip()
        condition = soup.find("div", class_="h2").find_next("p").text.strip()

        print(f"\nWeather in {city.capitalize()}:")
        print(f"Temperature: {temp}")
        print(f"Condition: {condition}")
    except:
        print("Could not extract weather data. Site structure may have changed.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)

