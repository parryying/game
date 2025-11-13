#!/usr/bin/env python3
"""
Simple HTTP server to serve the game website.
Run this script to start a local web server.
"""
import http.server
import socketserver
import os
import sys
from pathlib import Path

# Set the port for the server
PORT = 8000

# Change to the directory containing index.html
script_dir = Path(__file__).parent
os.chdir(script_dir)

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers to prevent caching during development
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == "__main__":
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"Serving HTTP on port {PORT}")
            print(f"Open your browser and go to: http://localhost:{PORT}")
            print("Press Ctrl+C to stop the server")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)