PORT = 8000


class TestHandler(http.server.SimpleHTTPRequestHandler):
    """The test example handler."""

    def do_POST(self):
        """Handle a post request by returning the square of the number."""
        print(self.headers)
        length = int(self.headers.get_all('content-length')[0])
        print(self.headers.get_all('content-length'))
        data_string = self.rfile.read(length)
        print(data_string)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.flush_headers()
        self.wfile.write("I got it!".encode())


def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = http.server.HTTPServer(server_address, TestHandler)
    server.serve_forever()

start_server()
