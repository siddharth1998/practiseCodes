'''
This is an example of how to send data to Slack webhooks in Python with the
requests module.
Detailed documentation of Slack Incoming Webhooks:
https://api.slack.com/incoming-webhooks
'''

import json
import requests

# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
webhook_url = 'url'
slack_data = {'text': "Model finished <@U05AETXN1B2>"}

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
