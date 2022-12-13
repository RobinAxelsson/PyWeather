import json
from unittest import TestCase
from ..smhi_gateway import get_bjorko_farjan_wind_forecasts


class SmhiAcceptanceTests(TestCase):
    json_dict = None

    def setUp(self):
        __get_json_point_request = SmhiAcceptanceTests.__load_smhi_point_request_dict

    def test_get_wind_collection(self):

        # Arrange & Act
        winds = get_bjorko_farjan_wind_forecasts()
        wind0 = winds[0]

        # Assert
        self.assertEqual(52, wind0.direction)
        self.assertEqual(1.2, wind0.mean_wsp)
        self.assertEqual(3.3, wind0.max_wsp)

    @staticmethod
    def __load_smhi_point_request_dict(latitude, longitude) -> dict:
        if SmhiAcceptanceTests.json_dict is None:
            with open("smhi.point-request.json", 'r') as f:
                SmhiAcceptanceTests.json_dict = json.load(f)
        return SmhiAcceptanceTests.json_dict
