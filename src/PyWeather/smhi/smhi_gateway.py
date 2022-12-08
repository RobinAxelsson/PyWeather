from src.PyWeather.models.wind import Wind
from src.PyWeather.smhi.mapper import SmhiMapper
from . import Repository, parse_point_request


class SmhiGateway:
    @staticmethod
    def get_wind_collection() -> list[Wind]:
        request_json = Repository.get_json_point_request()
        point_request = parse_point_request(request_json)
        winds = SmhiMapper.map_wind_list(point_request)
        return winds
