import json

from PyWind.entities.windforecast import WindForecast


def get_forecasts_double():
    return __get_forecasts_double('src/__tests/wind_forecasts.json')


def __get_forecasts_double(filepath):
    json_forecasts = []
    with open(filepath, 'r') as f:
        json_forecasts = json.load(f)
    forecasts = list(map(lambda x: __parse(x), json_forecasts))
    return forecasts


def __parse(forecast_dict: dict):
    forecast = WindForecast.__new__(WindForecast)
    forecast.__init__()
    for key in forecast_dict:
        forecast.__setattr__(key, forecast_dict[key])
    return forecast


if __name__ == '__main__':
    __get_forecasts_double('wind_forecasts.json')
