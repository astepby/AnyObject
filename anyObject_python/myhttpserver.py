
import http.server

import ssl



httpd = http.server.HTTPServer(('0.0.0.0', 8765), http.server.SimpleHTTPRequestHandler)

#httpd.socket = ssl.wrap_socket(httpd.socket, certfile='newcert.pem', keyfile='newkey.pem')

httpd.serve_forever()
