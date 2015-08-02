import os
import logging
import socket
import sys
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

from endpoints.interface.simple import Server

s=Server()
s.serve_forever()
