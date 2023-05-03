FROM ubuntu:23.04 as base
WORKDIR /app
RUN apt update
RUN apt install gcc build-essential fakeroot python3-full python3-pip -y

FROM base as final
WORKDIR /app
COPY ../ .

ENTRYPOINT ["python3", "masterService.py"]