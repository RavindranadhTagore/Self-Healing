from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    print("Received alert:", data)
    os.system("ansible-playbook restart_nginx.yml")
    return 'Alert received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

