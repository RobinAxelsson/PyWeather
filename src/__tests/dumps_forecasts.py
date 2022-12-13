import json
from PyWind import get_bjorko_farjan_wind_forecasts

windForecasts = get_bjorko_farjan_wind_forecasts()
json_winds = [json.dumps(x.__dict__) for x in windForecasts]

with open('./__test/wind_forecasts.json', 'w') as f:
    f.write("[\n" + ',\n'.join(json_winds) + "\n]")
