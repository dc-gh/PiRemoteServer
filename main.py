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
    app.run(ssl_context=('selfsigned.crt', 'selfsigned.key'), host='0.0.0.0', port=5000)

