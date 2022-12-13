import json

from PyWind.entities.windforecast import WindForecast

__file_path = './PyWind/data_access/wind_forecast/wind_forecasts.json'


def create(wind_forecasts: [WindForecast]):
    json_winds = [json.dumps(x.__dict__) for x in wind_forecasts]
    with open(__file_path, 'w') as f:
        f.write("[\n" + ',\n'.join(json_winds) + "\n]")


def get() -> [WindForecast]:
    with open(__file_path, 'r') as f:
        forecast_dicts = json.loads(f.read())
    return list(map(lambda x: __parse(x), forecast_dicts))


def __parse(forecast_dict: dict):
    return WindForecast(
        forecast_dict['mean_wsp'],
        forecast_dict['max_wsp'],
        forecast_dict['direction'],
        forecast_dict['latitude'],
        forecast_dict['longitude'],
        forecast_dict['reference_time'],
        forecast_dict['target_time'],
        forecast_dict['source']
    )


if __name__ == '__main__':
    __file_path = 'wind_forecasts.json'
    get()
