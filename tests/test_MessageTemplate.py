from issue_closed_notification import MessageTemplates

def test_templateFormat():
    message_templates = MessageTemplates.messageTemplates
    for message_template in message_templates:
        assert "[repo_name#issue_number](issue_url)" in message_template
        assert "assignee" in message_template
