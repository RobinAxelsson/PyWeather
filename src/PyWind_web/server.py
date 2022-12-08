import json

from flask import Flask, render_template
from src.PyWind import PyWind

app = Flask(__name__)


@app.route('/')
def bjorko_forecast():
    forecast = PyWind.get_bjorko_farjan_wind_forecasts()[1]
    return render_template('index.html', direction=forecast.direction, mean_wsp=forecast.mean_wsp,
                           max_wsp=forecast.max_wsp, target_time=__format_time(forecast.target_time))


@app.route('/api')
def bjorko_forecast_json():
    wind_forecasts = PyWind.get_bjorko_farjan_wind_forecasts()
    json_winds = [json.dumps(x.__dict__) for x in wind_forecasts]
    json_response = '[' + ",".join(json_winds) + ']'

    response = app.response_class(
        response=json_response,
        status=200,
        mimetype='application/json'
    )
    return response


def __format_time(time):
    [hour, minutes, _] = time.split('T')[1].split(':')
    return f'{hour}:{minutes}'


if __name__ == '__main__':
    app.run()
