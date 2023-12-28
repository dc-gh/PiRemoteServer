import configparser
from flask import Flask, request
import json
from py_irsend import irsend

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_json():
    if request.is_json:
        data = request.get_json()
        print("Received JSON:", data)
        
        device = data.get("device", "unknown")
        commands = data.get("commands", [])
        irsend.send_once(device, commands)

        return json.dumps({ "success": True})
    else:
        print("Failed to parse request!")
        response = {"success": False}
        return json.dumps(response)

if __name__ == '__main__':
    settings = configparser.ConfigParser()
    settings.read("settings.ini")
    serverAddress = settings.get("network", "address")
    serverPort = settings.get("network", "port")

    sslEnabled = settings.get("ssl", "ssl_enabled")
    publicKey = settings.get("ssl", "public_key")
    privateKey = settings.get("ssl", "private_key")
    if sslEnabled:
        app.run(ssl_context=(publicKey, privateKey), host=serverAddress, port=serverPort)
    else:
        app.run(host=serverAddress, port=serverPort)

