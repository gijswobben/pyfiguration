""" script.py
"""
import http.server
import socketserver

from pyfiguration import conf


# Create a request handler
Handler = http.server.SimpleHTTPRequestHandler


@conf.addIntField(
    field="server.port",
    description="The port on which the server will start",
    default=8000,
    minValue=80,
    maxValue=9999,
)
def startServer():
    port = conf["server"]["port"]
    print(f"Starting on port {port}")
    with socketserver.TCPServer(("", port), Handler) as httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    startServer()
