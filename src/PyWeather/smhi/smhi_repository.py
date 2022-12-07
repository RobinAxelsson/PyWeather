import requests


class SmhiRepository:
    @staticmethod
    def get_json_point_request() -> object:
        request = requests.get('https://opendata-download-metfcst.smhi.se/api/'
                               'category/pmp3g/version/2/geotype/point/lon/16/lat/58/data.json')
        return request.json()
