import requests

from PyWind.entities.windforecast import WindForecast
from .resources import parse_point_request
from .resources import SmhiPointRequest
from .resources import SmhiParameter
from .resources import SmhiTimeSeries


def get_bjorko_farjan_wind_forecasts() -> list[WindForecast]:
    request_json = __get_json_point_request(57.704, 11.69)
    point_request = parse_point_request(request_json)
    winds = __map_wind_list(point_request)
    return winds


def __get_json_point_request(latitude, longitude) -> dict:
    base_url = 'https://opendata-download-metfcst.smhi.se/api/'
    endpoint = f'category/pmp3g/version/2/geotype/point/lon/{longitude}/lat/{latitude}/data.json'
    request = requests.get(base_url + endpoint)
    return request.json()


def __map_wind_list(point_request: SmhiPointRequest) -> list[WindForecast]:
    return [__map_smhi_series_wind(
        x,
        point_request.reference_time,
        point_request.geometry.coordinates[0]
    ) for x in point_request.time_series]


def __map_smhi_series_wind(series: SmhiTimeSeries, reference_time, coordinates) -> WindForecast:
    return WindForecast(
        __get_parameter_value(series.parameters, "ws"),
        __get_parameter_value(series.parameters, "gust"),
        __get_parameter_value(series.parameters, "wd"),
        coordinates[1],
        coordinates[0],
        reference_time,
        series.valid_time,
        "smhi"
    )


def __get_parameter_value(parameters: list[SmhiParameter], name: str) -> object:
    return [x for x in parameters if x.name == name][0].values[0]
