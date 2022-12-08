import requests

from src.PyWind.domain.entities.windforecast import WindForecast
from src.PyWind.service_smhi.resource_models import SmhiPointRequest, SmhiTimeSeries, SmhiParameter
from src.PyWind.service_smhi.parser import parse_point_request


class SmhiGateway:
    @staticmethod
    def get_bjorko_farjan_wind_forecasts() -> list[WindForecast]:
        request_json = SmhiGateway.__get_json_point_request()
        point_request = parse_point_request(request_json)
        winds = SmhiGateway.__map_wind_list(point_request)
        return winds

    @staticmethod
    def __get_json_point_request() -> dict:
        request = requests.get('https://opendata-download-metfcst.smhi.se/api/'
                               'category/pmp3g/version/2/geotype/point/lon/16/lat/58/data.json')
        return request.json()

    @staticmethod
    def __map_wind_list(point_request: SmhiPointRequest) -> list[WindForecast]:
        return [SmhiGateway.__map_smhi_series_wind(
            x,
            point_request.reference_time,
            point_request.geometry.coordinates[0]
        ) for x in point_request.time_series]

    @staticmethod
    def __map_smhi_series_wind(series: SmhiTimeSeries, reference_time, coordinates) -> WindForecast:
        return WindForecast(
            SmhiGateway.__get_parameter_value(series.parameters, "ws"),
            SmhiGateway.__get_parameter_value(series.parameters, "gust"),
            SmhiGateway.__get_parameter_value(series.parameters, "wd"),
            coordinates[0],
            coordinates[1],
            reference_time,
            series.valid_time,
            "smhi"
        )

    @staticmethod
    def __get_parameter_value(parameters: list[SmhiParameter], name: str) -> object:
        return [x for x in parameters if x.name == name][0].values[0]
