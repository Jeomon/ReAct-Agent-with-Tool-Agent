from src.tool import tool
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from typing import *
import os
load_dotenv()

class Weather(BaseModel):
    location: str = Field(..., description='The location to fetch the current weather from.', example=['London'])

@tool('Weather Tool', args_schema=Weather)
def weather_tool(location: str='Kochi'):
    """
    Fetches the current weather conditions and forecast for the given location using OpenWeatherMap API.
    """
    import os
    import requests
    import json
    from pydantic import BaseModel
    api_key = os.environ.get('OPENWEATHERMAP_API_KEY')
    try:
        base_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
        forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric'
        response = requests.get(base_url)
        forecast_response = requests.get(forecast_url)
        response.raise_for_status()
        forecast_response.raise_for_status()
        weather_data = response.json()
        forecast_data = forecast_response.json()
        weather = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        forecast = ''
        for i in range(0, 40, 8):
            forecast += f'Forecast for {forecast_data['list'][i]['dt_txt']}: {forecast_data['list'][i]['weather'][0]['description']}\n'
        return f'Location: {location}\nWeather: {weather}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nForecast:\n{forecast}'
    except requests.exceptions.HTTPError as errh:
        return f'HTTP Error: {errh}'
    except requests.exceptions.ConnectionError as errc:
        return f'Error Connecting: {errc}'
    except requests.exceptions.Timeout as errt:
        return f'Timeout Error: {errt}'
    except requests.exceptions.RequestException as err:
        return f'Something went wrong: {err}'

class SystemTime(BaseModel):
    format:str=Field(...,description="The format of the time.",example=['%H:%M:%S'])

@tool("System Time Tool",args_schema=SystemTime)
def system_time_tool(format:str):
    '''
    Retrieves the current system time in the specified format.
    '''
    import time
    try:
        current_time=time.strftime(format)
    except Exception as err:
        return f"Error: {err}"
    return current_time

class NewsAPI(BaseModel):
    query:str=Field(...,description="The query or topic to fetch news articles.",example=['An example for query'])
    api_key:str=Field(...,description="The API key for News API.",example=['An example for api key'])

@tool("News API Tool",args_schema=NewsAPI)
def news_api_tool(query:str,api_key:str):
    '''
    Fetches news articles based on the given query or topic using News API and returns the formatted results.
    '''
    import requests
    import os
    api_key=os.environ.get('NEWS_API_KEY')
    try:
        url=f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
        response=requests.get(url)
        data=response.json()
        articles=data['articles']
        formatted_results=''
        for article in articles:
            formatted_results+=f"{article['title']}\n{article['description']}\n{article['url']}\n\n"
        return formatted_results
    except Exception as err:
        return f"Error: {err}"

