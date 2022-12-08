import json
from unittest import TestCase, skip

from src.PyWeather.models.wind import Wind
from src.PyWeather.smhi_gateway import SmhiGateway


class SmhiIntegrationTests(TestCase):

    def test_get_wind_collection(self):

        # Act
        winds = SmhiGateway.get_wind_collection()
        json_winds = [json.dumps(x.__dict__) for x in winds]

        # Assert
        self.assertIsInstance(winds[0], Wind)
        print(",\n".join(json_winds))
        return

