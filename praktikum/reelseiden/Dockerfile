FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y --no-install-recommends socat && \
    rm -rf /var/cache/apt/archives /var/lib/apt/lists

COPY dist/main /app/main
COPY src/flag.txt /app/flag.txt

RUN chmod 755 /app/main

WORKDIR /app

CMD socat -T30 -t30 tcp-l:1337,reuseaddr,fork EXEC:"./main",stderr,su=nobody
