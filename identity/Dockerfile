FROM concordium/genesis-tools:latest
RUN apt-get update && \
    apt-get -y install python3 && \
    rm -rf /var/lib/apt/lists/*

# Use globally installed tools.
ENV CLIENT_TOOL=client

WORKDIR /work
ENV GENESIS_DIR=/work/out

COPY ./generate-test-ip.py /
ENTRYPOINT [ "/generate-test-ip.py" ]