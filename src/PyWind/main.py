import json
from service_smhi import SmhiGateway


def get_wind_collection() -> None:
    winds = SmhiGateway.get_bjorko_farjan_wind_forecasts()
    json_winds = [json.dumps(x.__dict__) for x in winds]
    print(",\n".join(json_winds))


get_wind_collection()
