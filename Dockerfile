FROM python:3.8.2

COPY . /work
WORKDIR /work

RUN pip3 install -r requirements.txt

CMD pytest test/test_order.py
