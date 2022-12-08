import json
from unittest import TestCase

from src.PyWind.service_smhi.resource_models import SmhiPointRequest, SmhiGeometry, SmhiTimeSeries, SmhiParameter
from src.PyWind.service_smhi.parser import parse_point_request


class SmhiRequestParserTests(TestCase):
    def test_parse_point_request(self):
        request_dict = SmhiRequestParserTests.__load_smhi_point_request_dict()
        request = parse_point_request(request_dict)
        self.assertIsInstance(request, SmhiPointRequest)
        self.assertIsInstance(request.geometry, SmhiGeometry)
        self.assertEqual("2022-12-01T14:00:00Z", request.reference_time)
        self.assertEqual("2022-12-01T14:07:08Z", request.approved_time)
        self.assertEqual(5, len(request.time_series))

    def test_parse_point_request_geometry(self):
        request_dict = SmhiRequestParserTests.__load_smhi_point_request_dict()
        geometry = parse_point_request(request_dict).geometry
        self.assertIsInstance(geometry, SmhiGeometry)
        self.assertEqual("Point", geometry.smhi_type)
        self.assertEqual([[15.990068, 57.997072]], geometry.coordinates)

    def test_parse_point_request_time_series(self):
        request_dict = SmhiRequestParserTests.__load_smhi_point_request_dict()
        time_series0 = parse_point_request(request_dict).time_series[0]
        self.assertIsInstance(time_series0, SmhiTimeSeries)
        self.assertEqual("2022-12-01T15:00:00Z", time_series0.valid_time)
        self.assertEqual(19, len(time_series0.parameters))

    def test_parse_point_request_wind_speed(self):
        request_dict = SmhiRequestParserTests.__load_smhi_point_request_dict()
        time_series0 = parse_point_request(request_dict).time_series[0]
        parameter_ws = [x for x in time_series0.parameters if x.name == "ws"][0]
        self.assertIsInstance(parameter_ws, SmhiParameter)
        self.assertEqual("ws", parameter_ws.name)
        self.assertEqual("m/s", parameter_ws.unit)
        self.assertEqual(10, parameter_ws.level)
        self.assertEqual("hl", parameter_ws.level_type)
        self.assertEqual([1.2], parameter_ws.values)

    __json_dict = None

    @staticmethod
    def __load_smhi_point_request_dict() -> dict:
        if SmhiRequestParserTests.__json_dict is None:
            with open("smhi.point-request.json", 'r') as f:
                SmhiRequestParserTests.__json_dict = json.load(f)
        return SmhiRequestParserTests.__json_dict
