from src.PyWeather.smhi.resource_models import SmhiPointRequest, SmhiGeometry, SmhiTimeSeries, SmhiParameter


def parse_point_request(request_json: dict) -> SmhiPointRequest:
    return SmhiPointRequest(
        request_json["approvedTime"],
        request_json["referenceTime"],
        SmhiGeometry(
            request_json["geometry"]["type"],
            request_json["geometry"]["coordinates"]
        ),
        __parse_time_series(request_json["timeSeries"])
    )


def __parse_time_series(timeseries_dict: list[dict]) -> list[SmhiTimeSeries]:
    series_list = []
    for series_json in timeseries_dict:
        series_list.append(
            SmhiTimeSeries(
                series_json["validTime"],
                __parse_parameters(series_json["parameters"])
            )
        )
    return series_list


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
