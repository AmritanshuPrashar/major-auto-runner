import requests
import schedule
import time

# Function to get weather data
def get_weather_data():
    url = "https://ai-weather-by-meteosource.p.rapidapi.com/current"
    
    querystring = {
        "lat": "30.9091",
        "lon": "77.1087",
        "timezone": "auto",
        "language": "en",
        "units": "auto"
    }
    
    headers = {
        "X-RapidAPI-Key": "d9e72d5342msha5223a25ee12e1fp176a8djsn77e13318c0fa",
        "X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    return response.json()

# Function to send data to the endpoint
def send_data_to_endpoint(temperature, humidity):
    url = "https://majorserver.onrender.com/add"
    
    data = {
        "data": {
            "temperature": temperature,
            "humidity": humidity
        }
    }
    
    response = requests.post(url, json=data)
    
    print("Data Sent to Endpoint:")
    print(response.text)

# Function to perform the tasks twice a day
def perform_tasks():
    # Get weather data
    weather_data = get_weather_data()
    
    # Extract temperature and humidity from the response
    temperature = weather_data["current"]["temperature"]
    humidity = weather_data["current"]["humidity"]
    
    # Send data to the endpoint
    send_data_to_endpoint(temperature, humidity)

# Schedule tasks to run twice a day
schedule.every().day.at("08:00").do(perform_tasks)
schedule.every().day.at("20:00").do(perform_tasks)

# Run the scheduled tasks indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
