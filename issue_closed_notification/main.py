from issue_closed_notification import Messages
from issue_closed_notification import EventProcessor
import requests
import os

def getWebhookURL():
    url=os.environ.get("INPUT_DISCORD_WEBHOOK_URL")
    if url is None or url == "None" or url == "":
        raise ValueError("Webhook URL not provided.")
    return url

def getPayload():
    print("Getting Issue Details")
    assignee,issue_number,issue_url,repo_name = EventProcessor.getIssueDetails()
    print("Generating Message")
    message = Messages.getMessage(assignee,repo_name,issue_number,issue_url)
    payload = {"content" : message}
    return payload

def postMessage():
    print("Posting Message")
    response = requests.post(getWebhookURL(),getPayload())
    if(response.status_code == 204):
        print("Message posted successfully")
    else:
        print("Message sending failed failed")
