from __future__ import absolute_import
import json
import grpc
import os
import logging
import codecs
import string
import random
from random import randint
from google.protobuf.json_format import MessageToDict, MessageToJson
from app.lit import lightning_pb2 as ln
from app.lit import taprootassets_pb2 as taproot
from app.lit import universe_pb2 as universe
from app.lit import mint_pb2 as mint
from app.lit import assetwallet_pb2 as assetwallet

from app.lit import lightning_pb2_grpc as lnrpc
from app.lit import taprootassets_pb2_grpc as taprootrpc
from app.lit import universe_pb2_grpc as universerpc
from app.lit import mint_pb2_grpc as mintrpc
from app.lit import assetwallet_pb2_grpc as assetwalletrpc

from app.mint_service import Mint
from app.schemas.mint import MintAssetRequest as MintRequest, \
    ListBatchesRequest, FinalizeBatchRequest
from app.schemas.taproot import ListAssetRequest
from app.utils import configure_environment, base64_to_bytes
# configure env
configure_environment()  
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

# NOTE this function is straddling v0.3.1 and v0.3.2
def mock_mint_request(
        asset_version: int = 1,
        asset_type: int = 0,
        enable_emissions: bool = False,
        new_grouped_asset: bool = True,
        grouped_asset: bool = True,
        group_key: bytes = None,
):
    random_name = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    random_amt  = int(randint(0, 100))
    # TODO handle bytes types
    # TODO handle new group / follow-on group
    req = MintRequest(
        name=random_name,
        amount=random_amt,
        asset_version=asset_version,
        asset_type=asset_type,
        enable_emissions=True,
        #new_grouped_asset=new_grouped_asset,
        #grouped_asset=grouped_asset,
        #group_key=group_key
    )
    return req

def mock_list_assets_request(
        with_witness: bool = False,
        include_spent: bool = False,
        include_leased: bool = False,
    ):
    return ListAssetRequest(
        with_witness=with_witness,
        include_spent=include_spent,
        include_leased=include_leased,
    )

if __name__ == "__main__":
    try:
        mint = Mint()
        # create new batch
        #mock_req = mock_mint_request()
        #asset = mint.mint_grouped_asset(req=mock_req)
        #print(asset)

        # list all prepped batches
        # batches = mint.list_batches(req=ListBatchesRequest())
        # print(batches)

        # finalize batch
        # minted = mint.finalize_batch(req=FinalizeBatchRequest())
        # print(minted)

        # get transactions relevant to the node
        # TODO check if this lnrpc service captures
        # taproot assets relevant transactions as well
        # this will require an ln_service.py

        # list assets
        req = mock_list_assets_request()
        test1 = mint.list_assets(req)
        #print(f"gRPC Message: {test1}")
        tweaked = test1.assets[0].asset_group.tweaked_group_key
        print(f"TWEAKED GROUP KEY GRPC MESSAGE: {tweaked}")
        #tweaked_a = "\003\t\360\001\377\252\020\020.\351\005\246z\220\240\027f\334\260\321\252\332w9\322\315\'6\334\251\322V+"
        #m2json = MessageToJson(test1)
        #print(f"JSON FMT: {m2json}")
        # TODO try MessageToJson on nested message asset group directly

        m2dict = MessageToDict(test1)
        #print(f"Dict FMT: {m2dict}")
        tweaked2 = m2dict["assets"][0]["assetGroup"]["tweakedGroupKey"]
        print(f"BEFORE: {tweaked2}")
        after = base64_to_bytes(tweaked2)
        print(f"AFTER: {after}")
        # TODO try MessageToDict on nested message asset group directly

        # TODO mint with group key
        # mint_req = MintRequest(
        #     name="O53A0U",
        #     amount=10,
        #     group_key=tweaked
        # )

        # NOTE mint second
        # second_batch = mint.mint_grouped_asset(mint_req)
        # print(second_batch)

        # NOTE finalize second
        # second_final = mint.finalize_batch(req=FinalizeBatchRequest())
        # print(second_final)
            
    except Exception as e:
        print("Failed to init Mint.")

    # creds = lnd_tls_auth()
    # channel = create_secure_channel(LND_URI, creds)
    # # TODO can you use same channel twice like this?
    # stub = create_lnd_stub(channel)
    # tap_stub = create_tapd_stub(channel=channel)

    # lnd_macaroon = get_macaroon()
    # tapd_macaroon = get_macaroon(path=TAPD_MACAROON)
    # # get wallet balance
    # response = stub.WalletBalance(ln.WalletBalanceRequest(), metadata=[('macaroon', lnd_macaroon)])
    # print(response.total_balance)
    # # tapd getinfo
    # response = tap_stub.GetInfo(taproot.GetInfoRequest(), metadata=[('macaroon', tapd_macaroon)])
    # print(response.lnd_identity_pubkey)