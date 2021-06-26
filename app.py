import json
from flask import Flask
from scrapper.coins import get_currency_info, get_all_currencies

app = Flask(__name__)


@app.route('/currencies/<currency>')
def get_currency(currency=None):
    response = {}
    if currency:
        data = get_currency_info(currency)
        payload = {
            'asset': currency,
            'values': {data.pop('updated_at'): data}
        }
        response = app.response_class(
            response=json.dumps(payload).encode('utf-8'),
            status=200,
            mimetype='application/json'
        )
    return response


@app.route('/currencies/all')
def get_currencies():
    data = get_all_currencies()
    response = app.response_class(
        response=json.dumps(data).encode('utf-8'),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()
