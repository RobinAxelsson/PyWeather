import json
from unittest import TestCase

from src.PyWeather.smhi.repository import SmhiRepository
from src.PyWeather.smhi_gateway import SmhiGateway


class SmhiAcceptanceTests(TestCase):
    json_dict = None

    def setUp(self):
        SmhiRepository.get_json_point_request = SmhiAcceptanceTests.__load_smhi_point_request_dict

    def test_get_wind_collection(self):

        # Arrange & Act
        winds = SmhiGateway.get_wind_collection()
        wind0 = winds[0]

        # Assert
        self.assertEqual(52, wind0.direction)
        self.assertEqual(1.2, wind0.mean)
        self.assertEqual(3.3, wind0.gust)

    @staticmethod
    def __load_smhi_point_request_dict() -> dict:
        if SmhiAcceptanceTests.json_dict is None:
            with open("json/smhi.point-request.json", 'r') as f:
                SmhiAcceptanceTests.json_dict = json.load(f)
        return SmhiAcceptanceTests.json_dict
