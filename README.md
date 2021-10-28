# Issue Closed Notification Github Action
This action can be used to post a celebration message to discord channels when an issue is closed. The messages are randomly generated from MessageTemplates

## Usage
This action requires a discord webhook to be created. For reference on creating webhooks please have a look [here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).

After creating the webhook, copy the URL and set it as a secret in repository settings.

## Example
```yaml
name: Issue Closed Notification

# This workflow runs whenever an issue is closed
on:
  issues:
    types: ["closed"]

jobs:
  post-message:
    name: Post Celebration Message
    runs-on : ubuntu-latest
    steps:
      - name: Post message
        uses: mohan-13/issue-closed-notification-action@v1.0.0
        with:
          discord-webhook-url: ${{ secrets.DISCORD_WEBHOOK_URL }}
```

## Extending Template Messages
When you want more customised messages, please fork this repo and add your templates to `issue_closed_notification/MessageTemplates.py`. When you want to use your fork, make sure to update `uses` line in your workflow with your username.
