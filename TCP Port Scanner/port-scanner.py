import socket
target = input("Enter your target: ")
target_ip = socket.gethostbyname(target)

ports = [22, 80, 443, 8080]

for port in ports:
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)

    if s.connect_ex((target_ip, port)) == 0:
        print(f"Port {port} is OPEN!")
    else:
        print(f"Port {port} is closed.")

    s.close()
