import socket
import paramiko
import time
from datetime import datetime
import json

HOST = "0.0.0.0"
PORT = 2222
host_key = paramiko.RSAKey.generate(2048)

class ssh_server(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        return paramiko.AUTH_SUCCESSFUL
    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    def get_allowed_auths(self, username):
        return 'password'
    def check_channel_shell_request(self, channel):
        return True
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

conn, addr = server.accept()

transport = paramiko.Transport(conn)
transport.add_server_key(host_key)
ssh_handler = ssh_server()
transport.start_server(server=ssh_handler)

channel = transport.accept(20)
channel_r = channel.makefile('r')
time.sleep(0.5)

channel.send("Welcome to ssh \r\n")
while True:
    channel.send('root@ubuntu-$ ')
    cmd = channel_r.readline().strip().lower()

    if not cmd:
        continue
    if cmd == "whoami":
        channel.send("root \r\n")
    elif cmd == "pwd":
        channel.send("root/ubuntu/home/ambot-lang \r\n")
    elif cmd == "ls":
        channel.send("secret.txt \r\n")
    elif cmd == "cat secret.txt":
        channel.send("cute si james \r\n")
    elif cmd == "exit":
        channel.send("Exiting... \r\n")
        time.sleep(1)
        break
    else:
        channel.send(f"{cmd}: Command not found \r\n")

    data = {
        'Timestamp': str(datetime.now()),
        'Command': cmd
    }
    with open('server/logs/ssh_logs.json', 'a') as f:
        json.dump(data, f, indent=4)
        f.write("\n")

channel_r.close()
channel.close()
conn.close()
server.close()

