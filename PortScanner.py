#!/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '137.74.187.102'

port = 443

def portScanner(port):
  if s.connect_ex((host, port)):
    print("Port is closed")
  else: 
    print("Port is open")

    portScanner(port) 
