from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080

class AppHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html = """<!DOCTYPE html>
<html>
<head><title>CI/CD Automated Server</title></head>
<body style="font-family: sans-serif; text-align: center; margin-top: 10%;">
    <h1>🚀 DevOps Automated Deployment Active</h1>
    <p>Status: <strong>Online</strong></p>
    <p>Version: <code>2.0.0</code></p>
</body>
</html>"""
        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    print(f"[*] Starting server on port {PORT}...")
    server = HTTPServer(('0.0.0.0', PORT), AppHandler)
    server.serve_forever()
