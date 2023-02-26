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
  docker-compose build
  docker-compose up
  ```
  * Change the genesis hash in the [browser wallet](./deps/concordium-browser-wallet/packages/browser-wallet/src/shared/constants/networkConfiguration.ts)

  - //TODO: Should we change leadershipElectionNonce in `genesis4.toml`? What does it mean?
  - //TODO: Create a genesis-assemble file for artifacts created from `genesis4.toml`.


## Random Notes
1. Verifier sends Statement with Global Attributes in string
2. Wallet has access to Global Parameters, And Identity Provider Selected Parameters
  * Wallet reads Global Parameter Statement. Should statement here have a schema url?
  * Converts them to Identity Provider Attributes
  * Generates Proofs based on Identity Provider Attributes
  * Sends back to the verifier which already knows the Identity Provider and Verifies the proofs using the Identity Provider Attributes Via the Chain Posted Commitments.
