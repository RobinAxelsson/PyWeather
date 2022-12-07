import json
from unittest import TestCase

from src.PyWeather.mapper import SmhiMapper
from src.PyWeather.smhi.parser import SmhiParser


class SmhiGatewayTests(TestCase):
    def test_parse_point_request(self):
        request_dict = SmhiGatewayTests.__load_smhi_point_request_dict()
        request = SmhiParser.point_request(request_dict)
        time_series0 = request.time_series[0]
        smhi_mapper = SmhiMapper()
        wind = smhi_mapper._SmhiMapper__map_smhi_series_wind(time_series0)
        self.assertEqual(52, wind.direction)
        self.assertEqual(1.2, wind.mean)
        self.assertEqual(3.3, wind.gust)

    __json_dict = None

    @staticmethod
    def __load_smhi_point_request_dict() -> dict:
        if SmhiGatewayTests.__json_dict is None:
            with open("json/smhi.point-request.json", 'r') as f:
                SmhiGatewayTests.__json_dict = json.load(f)
        return SmhiGatewayTests.__json_dict
