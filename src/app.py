import json
import os
from flask import Flask
from flask import render_template
from dotenv import load_dotenv
from PyWind import get_ockero_farjan_forecasts

load_dotenv()
server = Flask(__name__)

if os.getenv('APP_ENVIRONMENT') == "DEVELOPMENT":
    server.debug = True


@server.route('/')
def bjorko_forecast():
    forecast = get_ockero_farjan_forecasts()[1]
    return render_template('index.html', direction=forecast.direction, mean_wsp=forecast.mean_wsp,
                           max_wsp=forecast.max_wsp, target_time=__format_time(forecast.target_time))


@server.route('/api')
def ockero_forecast_json():
    wind_forecasts = get_ockero_farjan_forecasts()
    json_winds = [json.dumps(x.__dict__) for x in wind_forecasts]
    json_response = '[' + ",".join(json_winds) + ']'

    response = server.response_class(
        response=json_response,
        status=200,
        mimetype='application/json'
    )
    return response


def __format_time(time):
    [hour, minutes, _] = time.split('T')[1].split(':')
    return f'{hour}:{minutes}'


if __name__ == '__main__':
    server.run()
