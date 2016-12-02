import socket as sock

host = sock.gethostname()

try:
  sock.bind()
  sock.listen()
  
  sock.connect(host, 1234)
  print("Connecting to socket...\n")
  
  sock.recv(100)
  print("Receiving...\n")
  
  sock.close()
  print("Closing the socket...\n")
  
except Exception:
  print("Could not connect.")
