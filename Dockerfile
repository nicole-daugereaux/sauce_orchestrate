FROM python:3
WORKDIR /sauce_orchestrate
COPY requirements.txt /sauce_orchestrate
RUN pip3 install -r requirements.txt
COPY puppySearch.py /sauce_orchestrate
