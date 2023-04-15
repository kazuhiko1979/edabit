#!/usr/bin/env python
from http.server import CGIHTTPRequestHandler, HTTPServer

# Set the port number for the server
PORT = 8000

# Create a CGI handler object and set the directory for CGI scripts
handler = CGIHTTPRequestHandler
handler.cgi_directories = ["/cgi-bin"]

# Start the server
httpd = HTTPServer(("", PORT), handler)
print("CGI server running on port", PORT)
httpd.serve_forever()
