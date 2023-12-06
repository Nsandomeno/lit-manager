from enum import Enum
from typing import Optional
from pydantic import BaseModel

class ErrorIds(Enum):
    """
        use str.starts_with
    """
    # general
    FAILED_NODE_CONNECT     = "g0"
    # funding
    INSUFFICIENT_FUNDS      = "f0"
    # transfer
    INVALID_RECEIVE_ADDR    = "t0"
    INVALID_SEND_ADDR       = "t1"
    # security / auth
    FAILED_TO_READ_MACAROON = "s0"
    FAILED_TO_FIND_MACAROON = "s1"
    FAILED_TO_READ_TLS_CERT = "s2"
    FAILED_TO_FIND_TLS_CERT = "s3"
    # application
    FAILED_TO_CREATE_GRPC_STUB         = "a0"
    FAILED_TO_MAP_REQUEST_TO_TYPE      = "a1"
    FAILED_TO_BROADCAST_MINTED_BATCHES = "a2"
    # NOTE add additional error IDs for specific handling
    UNKNOWN                 = "u0"


class Error(Exception):
    def __init__(
            self, 
            message: str = None, 
            detail: str = None, 
            error_id: int = None
        ):
        self.message = message
        self.detail  = detail
        self.error_id = error_id

