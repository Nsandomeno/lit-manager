import os
import base64
import logging
from enum import Enum
from dotenv import load_dotenv, find_dotenv

# TODO straggling constant
class Env(Enum):
    REGTEST  = "regtest"
    TESTNET  = "testnet"
    MAINNET  = "mainnet"


def configure_environment():
    """
        Use local ~/.polar data directory if NETWORK = REGTEST
    """
    # Collect main settings to determine env specific settings
    # to load
    load_dotenv()
    # load env specific settings - regtest
    if os.environ["NETWORK"] == Env.REGTEST.value:
        logging.warning("Loading regtest environment variables.")
        load_dotenv(find_dotenv(".env.local"))
    # load env specific settings - testnet
    elif os.environ["NETWORK"] == Env.TESTNET.value:
        logging.warning("Loading testnet environment variables.")
        load_dotenv(find_dotenv(".env.test"))


def base64_to_bytes(base64_str: str) -> bytes:
    try:
        encoded = base64_str.encode("ascii")
        return base64.decodebytes(encoded)
    except Exception as e:
        logging.error(f"Failed to format base64 string from parsed gRPC Message with error: {e}")
        raise e
