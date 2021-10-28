FROM python:3.8-slim

COPY run.py /run.py
COPY issue_closed_notification/ /issue_closed_notification/

RUN pip install requests

ENTRYPOINT ["python","/run.py"]
