""" script.py
"""
from pyfiguration import conf
from flask import Flask


@conf.addIntField(
    field="server.port",
    description="The port on which the server will start",
    default=8000,
    minValue=80,
    maxValue=9999,
)
def startServer():
    app = Flask(__name__)
    port = conf["server"]["port"]
    print(f"Starting on port {port}")
    app.run(port=port)


if __name__ == "__main__":
    startServer()
