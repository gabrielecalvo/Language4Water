import requests

def _get_woeid_from_city_name(city_name):
    json_data = requests.get(f"https://www.metaweather.com/api/location/search/?query={city_name}").json()
    if not json_data:
        raise ValueError(f"No city found with name: {city_name}")
    first_result_woeid = json_data[0]['woeid']
    return first_result_woeid
    
def _get_woeid_from_latlon(lat, lon):
    json_data = requests.get(f"https://www.metaweather.com/api/location/search/?lattlong={lat},{lon}").json()
    if not json_data:
        raise ValueError(f"No location found with latitude {lat} and longitude {lon}")
    first_result_woeid = json_data[0]['woeid']
    return first_result_woeid

def _get_weather_from_woeid(woeid):
    json_data = requests.get(f"https://www.metaweather.com/api/location/{woeid}").json()
    json_data['consolidated_weather']
    return json_data
    
def print_weather(city_name=None, lat=None, lon=None):
    if city_name is None:
        woeid = _get_woeid_from_latlon(lat, lon)
    else:
        woeid = _get_woeid_from_city_name(city_name)
        
    weather_data = _get_weather_from_woeid(woeid)
    
    for i in weather_data['consolidated_weather']:
        print(i['applicable_date'], i['weather_state_name'])
