import socket

target = "127.0.0.1"

def port_scanner(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))
    if result == 0:
          print(f"Port {port}: OPEN")
    else:
         print(f"Port {port}: CLOSED")

    s.close()

print(f"Scanning target: {target}")
for p in range(75, 86):
     port_scanner(p)

input("Press Enter to exit...")
