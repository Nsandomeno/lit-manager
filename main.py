import grpc
import os
import logging
import codecs

import api.lightning_pb2 as ln
import api.taprootassets_pb2 as taproot
import api.universe_pb2 as universe
import api.mint_pb2 as mint
import api.assetwallet_pb2 as assetwallet

import api.lightning_pb2_grpc as lnrpc
import api.taprootassets_pb2_grpc as taprootrpc
import api.universe_pb2_grpc as universerpc
import api.mint_pb2_grpc as mintrpc
import api.assetwallet_pb2_grpc as assetwalletrpc

# class MintServicer(mintrpc.MintServicer):
#     def MintAsset(self, request, context):
#         pass

#     def FinalizeBatch(self, request, context):
#         pass

#     def ListBatches(self, request, context):
#         pass

#     def CancelBatch(self, request, context):
#         pass

    
###
LND_CERT       = "./security/tls.cert"
LND_MACAROON = "./security/admin.macaroon"
LND_URI        = "node.fulminologylabs.co:10009"
TAPD_MACAROON = "./security/taproot/admin.macaroon"
###
# Due to updated ECDSA generated tls.cert we need to let gprc know that
# we need to use that cipher suite otherwise there will be a handhsake
# error when we communicate with the lnd rpc server.
os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'
# Create LND gRPC Stub
def lnd_tls_auth(path: str = LND_CERT):
    """
        Given a path to a tls.cert that was generated from a remote LND instance
        that is configured with `tlsextraip` or `tlsextradomain` for the IP or domain
        this client code is running from.

        returns ssl channel credentials
    """
    try:
        cert = open(os.path.expanduser(path), 'rb').read()
        return grpc.ssl_channel_credentials(cert)
    except Exception as e:
        logging.error(f"Error creating ssl channel credentials: {e}")
        raise e
    
# create secure channel 
def create_secure_channel(lnd_uri: str, creds):
    """
        Create secure gRPC channel.

        return secure channel
    """
    return grpc.secure_channel(LND_URI, creds)

# get admin macaroon
def get_macaroon(path: str = LND_MACAROON):
    """
        Provides the macaroon to attach to metadata
        of each request. This macaroon is created automatically by a remote
        LND/LiT instance and downloading for local access to the client code

        [ TODO ] find the proper way to handle macaroons and tls certificates.

        returns macaroon read from file.
    """
    with open(os.path.expanduser(path), 'rb') as f:
        macaroon_bytes = f.read()
        return codecs.encode(macaroon_bytes, 'hex')

# create lnd stub
def create_lnd_stub(channel):
    return lnrpc.LightningStub(channel)

# create taproot stub
def create_tapd_stub(channel):
    return taprootrpc.TaprootAssetsStub(channel)

if __name__ == "__main__":
    creds = lnd_tls_auth()
    channel = create_secure_channel(LND_URI, creds)
    # TODO can you use same channel twice like this?
    stub = create_lnd_stub(channel)
    tap_stub = create_tapd_stub(channel=channel)
    lnd_macaroon = get_macaroon()
    tapd_macaroon = get_macaroon(path=TAPD_MACAROON)
    # get wallet balance
    response = stub.WalletBalance(ln.WalletBalanceRequest(), metadata=[('macaroon', lnd_macaroon)])
    print(response.total_balance)
    # tapd getinfo
    response = tap_stub.GetInfo(taproot.GetInfoRequest(), metadata=[('macaroon', tapd_macaroon)])
    print(response.lnd_identity_pubkey)