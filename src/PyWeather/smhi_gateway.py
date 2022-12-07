from src.PyWeather.models.wind import Wind
from src.PyWeather.smhi.smhi_mapper import SmhiMapper
from src.PyWeather.smhi.smhi_parser import SmhiParser
from src.PyWeather.smhi.smhi_repository import SmhiRepository


class SmhiGateway:
    @staticmethod
    def get_wind_collection() -> list[Wind]:
        request_json = SmhiRepository.get_json_point_request()
        point_request = SmhiParser.point_request(request_json)
        winds = SmhiMapper.map_wind_list(point_request)
        return winds
