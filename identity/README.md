# Identity configurations

## Docker

The dockerfile builds an image for generating genesis block and accounts.

Expected env vars:
* `GENESIS_DIR`: Output directory. Defaults to `/work/out`.
* `GENESIS_STRING`: genesis string

### Example build command

```shell
docker build -t generate-test-ip .
```

### Example run command

```shell
docker run -e GENESIS_STRING="Identity Test genesis parameters." -v "$PWD:/work" generate-test-ip
```

The files are created with owner `root` so one might want to update their ownership:

```shell
chown -R <id>:<group> ./out
```

