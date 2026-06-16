weather_data = {
    "hyderabad": "34°C Sunny",
    "bangalore": "28°C Cloudy",
    "chennai": "36°C Hot",
    "mumbai": "32°C Humid",
    "delhi": "38°C Sunny"
}


def weather_tool(query):

    query = query.lower()

    for city in weather_data:
        if city in query:
            return weather_data[city]

    return "Weather data not available"