from flask import Flask
from flask import jsonify
import requests
import os

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'token '+os.environ['GITHUB_TOKEN'],
}

data = '{"event_type": "fetch-deals"}'

app = Flask(__name__)
port_app = int(os.environ.get('PORT', 33507))

@app.route('/sendAction')
def hello_world():
    response_out = requests.post('https://api.github.com/repos/dineshpabbi10/github-action-deals/dispatches', headers=headers, data=data)
    return jsonify(
        message="Action Sent"
    )

if __name__ == '__main__':
   app.run(port=port_app)