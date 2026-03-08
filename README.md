# MALEVORA HONEYPOT
 - A simple honeypot created in python. It can detect web attacks and simulate terminal interactions via Telnet and SSH.
 - [🚀YouTube Video](https://youtu.be/N9-5rp_OlYM?si=p196oOXpTA8VxROV)
## Http/Webpage:
1. Fuzz Detection:
    * Routes like `/anything/here` log attempts.
    * Logged Data:
        - Ip Address
        - User-Agent
        - Directory: `/test/test1/test3`
    * Stored in: `http/logs/fuzz_logs.json`

2. Injection Attacks Detection:
    * Search form `(/search)` can detect:
        - SQL Injection
        - XSS
        - Other malicious payloads
    * Logged Data: 
        - Timestamp
        - Ip Address
        - User-Agent
        - Payload
    * Stored in: `http/logs/injection_logs.json`
    * All malicious inputs get a fake `404.html` response.

3. Login Page:
    * Fake `/admin` login
    * Collects login credentials for attackers
    * Logged Data:
        - Timestamp
        - Ip Address
        - User-Agent
        - Username
        - Password
    * Stored in: `http/logs/login_logs.json`
    * Attackers get a fake alert `Wrong Username/Password`.


## Server:
1. Telnet:
    * Fake terminal on port 5000
    * Attackers can execute basic commands: `whoami, pwd, ls, cat`
    * Can log attackers information:
        - Timestamp
        - Command
    * Stored in: `server/logs/telnet_logs.json`

2. SSH:
    * Fake SSH server on port 2222
    * No username/password needed
    * Attackers can execute basic commands: `whoami, pwd, ls, cat`
    * Can log attackers information:
        - Timestamp
        - Command
    * Stored in: `server/logs/ssh_logs.json`


## Installation:
```bash
git clone https://github.com/T3rr8us-P4nk/malovera-honeypot.git
cd malovera-honeypot
python -m venv venv
pip install -r requirements.txt
```
## Usage:
### Run Web Honeypot:
```bash
python app.py
```

### Run Telnet Honeypot:
```bash
python telnet.py
```
#### access: `telnet 127.0.0.1 50000`

### Run SSH Honeypot:
```bash
python ssh.py
```
#### access: `ssh -p 2222 user@127.0.0.1`
