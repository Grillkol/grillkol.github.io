from http.server import HTTPServer, BaseHTTPRequestHandler
import api
import ssl
import json

htmlPages = {
    "index": "templates\index.html",
    "portfolio": "templates\main.html",
    "works": "templates\works.html",
}

ssl_certfile = r"C:\Certbot\live\grillkol.net\fullchain.pem"
ssl_keyfile = r"C:\Certbot\live\grillkol.net\privkey.pem"

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            print(self.path)
            if self.path == "/":
                self.path = "/index"

            if self.path.startswith("/api"):
                if self.path[4:] in api.data:
                    self.send_response(200)
                    response_json = json.dumps(api.data[self.path[4:]])
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(response_json.encode("utf-8"))
                else:
                    self.send_response(404)
                    self.send_header("Content-type", "text/plain")
                    self.end_headers()
                    self.wfile.write(b"404 - Not Found ")
                
            else:
                returnString = None

                if self.path.endswith(".png"):
                    image_path = self.path[1:]  # Remove the leading slash
                    try:
                        with open(image_path, "rb") as image_file:
                            self.send_response(200)
                            self.send_header("Content-type", "image/png")
                            self.end_headers()
                            self.wfile.write(image_file.read())
                    except FileNotFoundError:
                        self.send_response(404)
                        self.send_header("Content-type", "text/plain")
                        self.end_headers()
                        self.wfile.write(b"404 - Image Not Found")

                elif self.path.endswith(".css"):
                    returnString = open("static/css/style.css", mode="r", encoding="utf-8").read()
                    self.send_response(200)
                    self.send_header("Content-type", "text/css")

                elif self.path[1:] in htmlPages:
                    returnString = open(htmlPages[self.path[1:]], mode="r", encoding="utf-8").read()
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                
                else:
                    returnString = "File Not Found"
                    self.send_response(404)
                    self.send_header("Content-type", "text/plain")

                if returnString is not None:
                    self.end_headers()
                    self.wfile.write(bytes(returnString, "utf-8"))
        except Exception as e:
            print("Error", e)
            self.send_response(500)

httpDaemon = HTTPServer(("192.168.1.5", 443), Server)
httpDaemon.socket = ssl.wrap_socket(httpDaemon.socket, certfile = ssl_certfile, keyfile = ssl_keyfile, server_side = True)

httpDaemon.serve_forever()