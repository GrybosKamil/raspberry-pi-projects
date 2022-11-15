import argparse
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world\n'

def create_app():
   return app
   # waitress-serve --port=9101 --call one-service:create_app

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, required=False, default=9101, help="Port")
    parser.add_argument("--env", type=str, choices=["dev","prod"], required=False, default="dev", help="Environment")
    args = parser.parse_args()

    host = "localhost"
    port = args.port

    if args.env == "prod":
        from waitress import serve
        serve(app, host=host, port=port)
    else:
        app.run(host=host, port=port, debug=True)
    # python3 one-service.py --port=9101 --env='dev'
    # python3 one-service.py --port=8080 --env='prod'