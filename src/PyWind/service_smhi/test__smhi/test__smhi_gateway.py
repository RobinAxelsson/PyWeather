import json
from unittest import TestCase

from src.PyWind.service_smhi.smhi_gateway import SmhiGateway


class SmhiAcceptanceTests(TestCase):
    json_dict = None

    def setUp(self):
        SmhiGateway._SmhiGateway__get_json_point_request = SmhiAcceptanceTests.__load_smhi_point_request_dict

    def test_get_wind_collection(self):

        # Arrange & Act
        winds = SmhiGateway.get_bjorko_farjan_wind_forecasts()
        wind0 = winds[0]

        # Assert
        self.assertEqual(52, wind0.direction)
        self.assertEqual(1.2, wind0.mean_wsp)
        self.assertEqual(3.3, wind0.max_wsp)

    @staticmethod
    def __load_smhi_point_request_dict() -> dict:
        if SmhiAcceptanceTests.json_dict is None:
            with open("smhi.point-request.json", 'r') as f:
                SmhiAcceptanceTests.json_dict = json.load(f)
        return SmhiAcceptanceTests.json_dict
