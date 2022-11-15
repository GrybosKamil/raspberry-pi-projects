import argparse
from flask import Flask
from components.SHTC3.SHTC3 import SHTC3

app = Flask(__name__)

component = SHTC3()

@app.route('/')
def index():
    return component.read_data()
    # return 'Hello world\n'

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