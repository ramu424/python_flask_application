# Save this as webapp.py
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleApp(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set the response status code to 200 (OK)
        self.send_response(200)

        # Set the headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # HTML content to send to the browser
        message = """
        <html>
        <head><title>My Web App</title></head>
        <body>
            <h1>Hello, this is my web app without Flask or Django!</h1>
        </body>
        </html>
        """

        # Send HTML content to client
        self.wfile.write(bytes(message, "utf8"))

# Set server address (localhost, port 8000)
host = "localhost"
port = 8000
server = HTTPServer((host, port), SimpleApp)

print(f"Server started at http://{host}:{port}")
server.serve_forever()
