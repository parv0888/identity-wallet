FROM concordium/testnet-node:latest
ENV CONCORDIUM_NODE_CONSENSUS_GENESIS_DATA_FILE /identity-testnet-genesis.dat
ENV CONCORDIUM_NODE_BAKER_CREDENTIALS_FILE /baker-0-credentials.json
COPY ./identity-testnet-files/genesis.dat ${CONCORDIUM_NODE_CONSENSUS_GENESIS_DATA_FILE}
COPY ./identity-testnet-files/bakers-out/baker-0-credentials.json ${CONCORDIUM_NODE_BAKER_CREDENTIALS_FILE}

ENTRYPOINT [ "./concordium-node" ]
# CMD [ "--no-bootstrap", "--debug", "--baker-credentials-file ${CONCORDIUM_NODE_BAKER_CREDENTIALS_FILE}" ]
