FROM python:latest

RUN git clone https://github.com/sahansandaruwan/bigboss /root/bigboss
WORKDIR /root/Alita/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]
