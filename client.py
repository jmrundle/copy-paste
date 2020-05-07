"""
client.py

- Constantly poll clipboard for changes (clipboard module)
    - Upon change, send clipboard state to server
"""
import sys
import time
import requests
import pyperclip
from config import PROTOCOL, PORT, ENDPOINT, KEY


def usage(status):
    print(f"Usage: {sys.argv[0]} [SERVER] [-p PORT]")
    sys.exit(status)


def test_connection(url):
    try:
        requests.get(url)
        return True
    except requests.exceptions.ConnectionError:
        return False


def post_clipboard(url, clipboard):
    data = {
        KEY: clipboard
    }
    resp = requests.post(url, json=data)

    return resp.ok


if __name__ == "__main__":
    """
    Parse Command Line args
    """
    SERVER = None
    argind = 1
    argc   = len(sys.argv)

    while argind < argc:
        arg = sys.argv[argind]

        if arg == "-p":
            if argind+1 >= argc:
                usage(1)
            PORT = sys.argv[argind+1]
            argind += 1
        else:
            SERVER = arg

        argind += 1

    if not SERVER or SERVER == "":
        SERVER = input("Server IP: ")

    """
    Verify connection
    """
    url = f"{PROTOCOL}://{SERVER}:{PORT}{ENDPOINT}"

    print(f"Attempting to connect to {SERVER} with {url}")

    if not test_connection(url):
        print(f"Unable to connect to {url}")
        sys.exit(2)
    else:
        print(f"Connection successful")

    """
    Read for clipboard updates
    """
    old_clip = pyperclip.paste()
    while True:
        curr_clip = pyperclip.paste()

        if curr_clip != old_clip:
            if post_clipboard(url, curr_clip):
                print("Sent:", curr_clip)
                print("-----------------")
            else:
                print(f"Error posting clipboard to {url}")

        old_clip = curr_clip

        time.sleep(0.1)
