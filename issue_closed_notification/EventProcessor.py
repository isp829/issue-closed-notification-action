import os
import json


def getIssueData():
    with open(os.environ.get("GITHUB_EVENT_PATH"), "r") as event_file:
        event_data=json.load(event_file)
        if 'issue' not in event_data:
            raise TypeError("This action should be used only with issue type workflows")
        if event_data['action'] == "closed":
            return event_data['issue']

def getIssueURL(issue_data):
    return issue_data['html_url']

def getIssueNumber(issue_data):
    return str(issue_data['number'])

def getReopName():
    return os.environ.get("GITHUB_REPOSITORY")

def getIssueDetails():
    issue_data=getIssueData()
    return getIssueNumber(issue_data),getIssueURL(issue_data),getReopName()
