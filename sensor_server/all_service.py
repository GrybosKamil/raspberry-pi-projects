import argparse
from flask import Flask, request
from components.ADS1015.ADS1015 import ADS1015
from components.ICM20948.ICM20948 import ICM20948
from components.LPS22HB.LPS22HB import LPS22HB
from components.SHTC3.SHTC3 import SHTC3
from components.TCS34725.TCS34725 import TCS34725

app = Flask(__name__)

components = {
    # 'ADS1015'   : ADS1015(),
    'ICM20948'  : ICM20948(), 
    # 'LPS22HB'   : LPS22HB(),
    'SHTC3'     : SHTC3(),
    'TCS34725'  : TCS34725()
}

@app.route('/')
def index():
    return "Hello World!\n"

@app.route('/all')
def get_all():
    return {
        # 'ADS1015'   : components['ADS1015'].read_data(),
        'ICM20948'  : components['ICM20948'].read_data(),
        # 'LPS22HB'   : components['LPS22HB'].read_data(),
        'SHTC3'     : components['SHTC3'].read_data(),
        'TCS34725'  : components['TCS34725'].read_data()
    }

@app.route('/component')
def get_component_value():
    args = request.args
    if args.get('name') in components:
        return components[args.get('name')].read_data()
    else:
        return {'message': 'component name "{0}" does not exist!'.format(args.get('name'))}


def create_app():
   return app
   # waitress-serve --port=9101 --call one-service:create_app

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, required=False, default="localhost", help="Host")
    parser.add_argument("--port", type=int, required=False, default=9101, help="Port")
    parser.add_argument("--env", type=str,  required=False, choices=["dev","prod"], default="dev", help="Environment")
    args = parser.parse_args()

    host = args.host
    port = args.port

    if args.env == "prod":
        from waitress import serve
        serve(app, host=host, port=port)
    else:
        app.run(host=host, port=port, debug=True)
    # python3 one-service.py --host="localhost"     --port=9101 --env='dev'
    # python3 one-service.py --host="192.168.0.x"   --port=8080 --env='prod'