from .wind_forecast import get as get_wind_forecast


def get_ockero_farjan_forecasts():
    return get_wind_forecast()
