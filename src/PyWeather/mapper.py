from src.PyWeather.models.wind import Wind
from src.PyWeather.smhi.dto import SmhiTimeSeries, SmhiParameter, SmhiPointRequest


class SmhiMapper:

    @staticmethod
    def map_wind_list(point_request: SmhiPointRequest) -> list[Wind]:
        return [SmhiMapper.__map_smhi_series_wind(x) for x in point_request.time_series]

    @staticmethod
    def __map_smhi_series_wind(series: SmhiTimeSeries) -> Wind:
        return Wind(
            get_parameter_value(series.parameters, "ws"),
            get_parameter_value(series.parameters, "gust"),
            get_parameter_value(series.parameters, "wd")
        )


def get_parameter_value(parameters: list[SmhiParameter], name: str) -> list:
    return [x for x in parameters if x.name == name][0].values[0]
