from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import os

# Set port number
PORT = 8011

# Set handler
handler = SimpleHTTPRequestHandler

# Create server
server = HTTPServer(('', PORT), handler)

print(f"Server started at http://localhost:{PORT}")
print("Press Ctrl+C to stop the server")

# Automatically open website in default browser
webbrowser.open(f'http://localhost:{PORT}')

# Start server
try:
    server.serve_forever()
except KeyboardInterrupt:
    server.server_close()
    print("\nServer stopped") 