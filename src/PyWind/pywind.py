from PyWind.domain.entities.windforecast import WindForecast
from PyWind.services.smhi import SmhiGateway


class PyWind:
    @staticmethod
    def get_bjorko_farjan_wind_forecasts() -> list[WindForecast]:
        return SmhiGateway.get_bjorko_farjan_wind_forecasts()
