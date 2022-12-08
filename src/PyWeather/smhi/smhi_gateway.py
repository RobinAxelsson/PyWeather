import requests

from src.PyWeather.models.wind import Wind
from src.PyWeather.smhi.resource_models import SmhiPointRequest, SmhiTimeSeries, SmhiParameter
from src.PyWeather.smhi.parser import parse_point_request


class SmhiGateway:
    @staticmethod
    def get_wind_collection() -> list[Wind]:
        request_json = SmhiGateway.__get_json_point_request()
        point_request = parse_point_request(request_json)
        winds = SmhiGateway.__map_wind_list(point_request)
        return winds

    @staticmethod
    def __get_json_point_request() -> object:
        request = requests.get('https://opendata-download-metfcst.smhi.se/api/'
                               'category/pmp3g/version/2/geotype/point/lon/16/lat/58/data.json')
        return request.json()

    @staticmethod
    def __map_wind_list(point_request: SmhiPointRequest) -> list[Wind]:
        return [SmhiGateway.__map_smhi_series_wind(x) for x in point_request.time_series]

    @staticmethod
    def __map_smhi_series_wind(series: SmhiTimeSeries) -> Wind:
        return Wind(
            SmhiGateway.__get_parameter_value(series.parameters, "ws"),
            SmhiGateway.__get_parameter_value(series.parameters, "gust"),
            SmhiGateway.__get_parameter_value(series.parameters, "wd")
        )

    @staticmethod
    def __get_parameter_value(parameters: list[SmhiParameter], name: str) -> list:
        return [x for x in parameters if x.name == name][0].values[0]
