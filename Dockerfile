FROM debian:latest

SHELL ["/bin/bash", "-c"]

RUN apt update; apt upgrade -y;apt install python3 python3-pip -y

RUN useradd -m -s /bin/bash nightlife-system

USER nightlife-system

WORKDIR /home/nightlife-system

COPY requirements.txt .

RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

CMD ["python3", "src/manage.py"]
