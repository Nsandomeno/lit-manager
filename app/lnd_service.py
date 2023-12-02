import logging # TODO note ensure setup properly
import codecs, grpc, os
from app.lit import lightning_pb2 as ln
from app.lit import lightning_pb2_grpc as lnrpc
from app.schemas.error import Error, ErrorIds

class Lnd:
    def __init__(self):
        try:
            self.uri = os.environ["LND_URI"]
            self.tls_path = os.environ["TLS_CERT"]
            self.macaroon_path = os.environ["LND_MACAROON"]
            self.channel = self._create_secure_channel()

        except Error as e:
            detail = "Lnd service init failed"
            logging.critical(f"{detail} : {e.message} : {e.error_id}")
            e.detail = detail
            raise e
        except Exception as e:
            # NOTE unknown error occurred
            message = f"Lnd init failed with an unknown error. Error: {e}"
            logging.critical(message)
            raise Error(message=message, error_id=ErrorIds.UNKNOWN.value)

    def _create_lnd_stub(self):
        try:
            return lnrpc.LightningStub(self.channel)
        except Exception as e:
            msg = f"Failed to create TaprootAssets RPC stub with error: {e}"
            raise Error(message=msg, error_id=ErrorIds.FAILED_TO_CREATE_GRPC_STUB.value)
        
    def _read_macaroon(self):
        try:
            with open(os.path.expanduser(self.macaroon_path), 'rb') as f:
                macaroon_bytes = f.read()
                return codecs.encode(macaroon_bytes, 'hex')
        except Exception as e:
            message = f"Failed to read admin macaroon. Error: {e}"
            logging.critical(message)
            raise Error(
                error_id=ErrorIds.FAILED_TO_READ_MACAROON,
                message=message
            )

    def _create_secure_channel(self):
        try:
            creds = self._read_cert()
            if creds:
                return grpc.secure_channel(self.uri, creds)
            else:
                raise Error(message="Could not read TLS certificate.", error_id=ErrorIds.FAILED_TO_FIND_TLS_CERT.value)
        except Error as err:
            raise err
        except Exception as e:
            msg = f"Failed to create ssl channel credentials from TLS cert. {e}"
            raise Error(message=msg, error_id=ErrorIds.FAILED_TO_READ_TLS_CERT.value)

    def _read_cert(self):
        try:
            cert = open(os.path.expanduser(self.tls_path), "rb").read()
            return grpc.ssl_channel_credentials(cert)
        except Exception:
            return None
        
    def wallet_balance(self):
        try:
           stub = self._create_lnd_stub() 
           res = stub.WalletBalance(ln.WalletBalanceRequest(), metadata=[('macaroon', self._read_macaroon())])
           logging.critical("Received wallet balances")
           logging.critical(res)
           # TODO error handling, validation, and mapping
           return res
        except Error as err:
            # NOTE logging required, this is a macaroon read error
            logging.critical(err.message)
            raise err
        except Exception as e:
            # NOTE logging of unknown exception required
            msg = f"Failed to retrive wallet balance with error: {e}"
            logging.critical(msg)
            raise Error(message=msg, error_id=ErrorIds.UNKNOWN.value)