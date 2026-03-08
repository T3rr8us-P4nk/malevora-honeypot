import socket
import time
import json
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

conn, addr = server.accept()
conn_r = conn.makefile('r')

conn.sendall(b'Welcome to telnet \r\n')
time.sleep(0.5)
while True:
    conn.sendall(b'root@ubuntu-$ ')
    cmd = conn_r.readline().strip().lower()

    if not cmd:
        continue
    if cmd == "whoami":
        response = "root \r\n"
    elif cmd == "pwd":
        response = "root/ubuntu/home/ambot-lang \r\n"
    elif cmd == "ls":
        response = "secret.txt \r\n"
    elif cmd == "cat secret.txt":
        response = "pogi si james haha \r\n"
    elif cmd == "exit":
        conn.sendall(b'Exiting... \n\r')
        break
    else:
        response = f"{cmd}: Command not found \r\n"
    conn.sendall(response.encode())

    data = {
        'Timestamp': str(datetime.now()),
        'Command': cmd
    }
    with open('server/logs/telnet_logs.json', 'a') as f:
        json.dump(data, f, indent=4)
        f.write("\n")


conn_r.close()
conn.close()
server.close()