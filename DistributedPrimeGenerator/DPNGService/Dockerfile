FROM ubuntu:23.04 as base
WORKDIR /app
RUN apt update
RUN apt install gcc build-essential fakeroot python3-full python3-pip -y

FROM base as final
EXPOSE 1337
WORKDIR /app
COPY ../ .

RUN python3 -m pip install psutil --break-system-packages
ENTRYPOINT ["python3", "DPNGServer.py"]