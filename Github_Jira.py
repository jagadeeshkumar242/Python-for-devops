from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json
# Creating a flask instance
app = Flask(__name__)

@app.route("/createJIRA", methods=['POST'])
def createJIRA():
    url = "https://bondarishi.atlassian.net/rest/api/3/issue"

    API_TOKEN = "ATATT3xFfGF0QADb05Bq6ZHHxAsPRz-rMDO92kzDKQh2rlJQJJLn78tnbDGHhmCzVvmI5CWfX1djg6Uycfh-qOTO1qaU22fsJyH-tdAoviUodMicW7RSll--uT_O76RFwYwTQmmdHYf2a4Ihin0sfJwKWkYNdNCTymLJd5TxQjgDoYV3F_GjDGY=2AE1CDCD"

    auth = HTTPBasicAuth("jagadeeshkumar242@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "project": {
        "key": "MP"
        },
        "issuetype": {
        "id": "10004"
        },
        "summary": "First JIRA Ticket",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return (json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

app.run('0.0.0.0')
