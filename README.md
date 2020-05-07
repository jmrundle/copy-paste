# Copy-Paste
copy text from one server, paste to another

## Installation
1. Make sure python3 and pip are installed
2. Install source files or clone repo on **both** servers, then download dependencies
##### Copy Server
```bash
$ git clone https://github.com/jmrundle/copy-paste.git
$ pip3 install -r requirements.txt
```
##### Paste Server
```bash
$ git clone https://github.com/jmrundle/copy-paste.git
$ pip3 install -r requirements.txt
```

## Usage
##### Copy Server
- Default SERVER IP is localhost
- Default port is specified in constants.py
- Run with following:
```bash
$ python3 client.py [SERVER_IP] [-p PORT]
```
##### Paste Server
- Default port is specified in constants.py
- Run with following:
```bash
$ python3 server.py [-p PORT]
```