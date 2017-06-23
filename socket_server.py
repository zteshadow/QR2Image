#!/user/bin/env python3
#-*- coding:utf8 -*-

import threading
import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
  def handle(self):
    data = self.request.rect(1024)
    current_thread = threading.current_thread()
    response = "{}:{}".format(current_thread.name, data)
    self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
  pass

if (__name__ == '__main__'):
  HOST, PORT = "0.0.0.0", 8081
  server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
  server.serve_forever
