from src.PyWeather.models.wind import Wind
from src.PyWeather.smhi.smhi_dto import SmhiPointRequest, SmhiGeometry, SmhiTimeSeries, SmhiParameter


class SmhiParser:
    @staticmethod
    def point_request(request_json: dict) -> SmhiPointRequest:
        return SmhiPointRequest(
            request_json["approvedTime"],
            request_json["referenceTime"],
            SmhiGeometry(
                request_json["geometry"]["type"],
                request_json["geometry"]["coordinates"]
            ),
            SmhiParser.__parse_time_series(request_json["timeSeries"])
        )

    @staticmethod
    def __parse_time_series(timeseries_dict: list[dict]) -> list[SmhiTimeSeries]:
        series_list = []
        for series_json in timeseries_dict:
            series_list.append(
                SmhiTimeSeries(
                    series_json["validTime"],
                    SmhiParser.__parse_parameters(series_json["parameters"])
                )
            )
        return series_list

    @staticmethod
    def __parse_parameters(parameters_dict: list[dict]) -> list[SmhiParameter]:
        parameters = []
        for parameter in parameters_dict:
            parameters.append(
                SmhiParameter(
                    parameter["name"],
                    parameter["levelType"],
                    parameter["level"],
                    parameter["unit"],
                    parameter["values"]
                )
            )
        return parameters