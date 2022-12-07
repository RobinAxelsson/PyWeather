from .models.wind import Wind
from src.PyWeather.mapper import SmhiMapper
from .smhi.parser import SmhiParser
from .smhi.repository import SmhiRepository


class SmhiGateway:
    @staticmethod
    def get_wind_collection() -> list[Wind]:
        request_json = SmhiRepository.get_json_point_request()
        point_request = SmhiParser.point_request(request_json)
        winds = SmhiMapper.map_wind_list(point_request)
        return winds
