from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = 'localhost'
serverPort = 8080
filename = 'index.html'

class MyServer (BaseHTTPRequestHandler ):

    def __get_content (self):
        with open (filename, 'r', encoding="utf-8") as file:
            result = file.read()
            return result

    def do_GET (self):
        query_components = parse_qs (urlparse(self.path).query)
        page_content = self.__get_content()
        self.send_response(200)
        self.send_header ("Content-type","text/html")
        self.end_headers()
        self.wfile.write(bytes (page_content, "utf-8"))


if __name__ == '__main__':
    webServer = HTTPServer ((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer. serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
