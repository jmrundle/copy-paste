#Copy-Paste
copy files from one server, paste to another

## Installation
Install source files or clone repo on both servers, then download dependencies
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
```bash
$ python3 client.py [SERVER_IP] [-p PORT]
```
##### Paste Server
```bash
$ python3 server.py [-p PORT]
```