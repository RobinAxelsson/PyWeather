import json

from src.PyWind import PyWind

windForecasts = PyWind.get_bjorko_farjan_wind_forecasts()
json_winds = [json.dumps(x.__dict__) for x in windForecasts]
print(",\n".join(json_winds))
