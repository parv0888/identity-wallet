#!/usr/bin/env python3
import os
import subprocess
import shutil

# Runner that uses native binaries
class HostRunner:

    def run_client(self, *args):
        res = subprocess.run(CLIENT_TOOL + list(args))
        return res.returncode


# The tool to generate identity providers, parameters, and anonymity revokers
CLIENT_TOOL=os.environ.get("CLIENT_TOOL", default = "./client").split()

runner = HostRunner()

# If used with docker genesis tools image GENESIS_DIR must be a path under the current working directory.
GENESIS_DIR = os.environ.get("GENESIS_DIR", default = "./genesis_data")

GENESIS_STRING = os.environ.get("GENESIS_STRING", default = "Concordium Testnet IP Test")

# Number of identity providers that will be generated.
NUM_IPS = os.environ.get("NUM_IPS", default = "1")
# Number of anonymity revokers that will be generated.
NUM_ARS = os.environ.get("NUM_ARS", default = "0")

# Helper defined constants
GLOBAL_FILE = os.path.join("/work", "global.json")

# Create cryptographic parameters, identity providers, and anonymity revokers
def create_base_parameters():
    if os.path.exists(GENESIS_DIR):
        raise Exception(f"Refusing to overwrite genesis directory {GENESIS_DIR}")
    else:
        os.makedirs(GENESIS_DIR)

    ips = runner.run_client("generate-ips", "--global", GLOBAL_FILE, "--num", NUM_IPS, "--num-ars", NUM_ARS, "--out-dir", GENESIS_DIR)
    if ips != 0:
        raise Exception(f"Could not create identity providers {ips.stderr}")

# If the PURGE environment variable is set then delete the genesis directory before starting anything else
def clean():
    if os.environ.get("PURGE") is not None:
        if os.path.exists(GENESIS_DIR):
            shutil.rmtree(GENESIS_DIR)
        else:
            print(f"PURGE set, but no {GENESIS_DIR} does not exist, so nothing was deleted.")


clean()
# Create identity providers, anonymity revokers, and cryptographic parameters
create_base_parameters()
# Create all the bakers