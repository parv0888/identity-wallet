# Identity Wallet

## Setup Permissioned Blockchain

- Using Docs at [Local Chain](https://github.com/Concordium/concordium-node/blob/main/docs/local-chain.md)
- Build [genesis-creator](./deps/concordium-misc-tools/genesis-creator/README.md)
- Execute

  ```bash
  cargo build --release --manifest-path ../deps/concordium-misc-tools/genesis-creator/Cargo.toml
  cp ../deps/concordium-misc-tools/genesis-creator/target/release/genesis-creator ./genesis-creator
  ./genesis-creator generate --config ./genesis4.toml
  ```
  *Change Url of the Identity Provider to have localhost as the Url so its easier to debug*
  ```bash
  docker-compose build node
  docker-compose up node
  ```
  - //TODO: Should we change leadershipElectionNonce in `genesis4.toml`? What does it mean?
  - //TODO: Create a genesis-assemble file for artifacts created from `genesis4.toml`.

