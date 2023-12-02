import json
import logging
from app.lit import mint_pb2 as mintrpc

import app.schemas.mint as schema
from app.lit import mint_pb2_grpc as mintstub
from app.utils import base64_to_bytes
from app.tapd_service import Tapd
from app.schemas.error import Error, ErrorIds
from google.protobuf.json_format import MessageToDict

class MintError(Error):
    """
        NOTE not to be used in initialization method.
    """
    category: str = "mintrpc"


class Mint(Tapd):
    def __init__(self):
        try:
            Tapd.__init__(self)
            self.stub = self._create_stub()

        except Error as err:
            if err.error_id == ErrorIds.FAILED_TO_CREATE_GRPC_STUB.value:
                # NOTE if otherwise, detail field is populated by an error initializing Tapd.
                err.detail = "Failed to init Mint (child) after successful init of Tapd (parent)"
                logging.critical(f"{err.detail} : {err.message} : {err.error_id}")

            raise err
        except Exception as e:
            # NOTE an unknown error occurred
            msg = f"Failed to init Mint (child) after successful init of Tapd (parent). Error: {e}"
            logging.critical(msg)
            raise Error(message=msg, error_id=ErrorIds.UNKNOWN.value)
        
    def _create_stub(self):
        try:
            return mintstub.MintStub(self.channel)
        except Exception as e:
            # NOTE no logging, init is caller
            msg = f"Failed to create Mint RPC stub after successful parent Tapd init. Error: {e}"
            raise Error(message=msg, error_id=ErrorIds.FAILED_TO_CREATE_GRPC_STUB.value)
        
    def mint_grouped_asset(self, req: schema.MintAssetRequest, short_res: bool = False):
        try:
            asset = Mint._build_grouped_asset(req)
            # NOTE must change in v0.3.2 - enable_emissions is deprecated
            request = mintrpc.MintAssetRequest(asset=asset, enable_emission=req.enable_emissions)
            res: mintrpc.MintAssetResponse = self.stub.MintAsset(request, metadata=[('macaroon', self._read_macaroon())])
            # TODO work in progress - handle error
            logging.critical("Mint Asset Response Received!")

            return res
        except Error as err:
            # NOTE logging required, api handler is caller
            logging.critical(err.message)
            raise err
        except Exception as e:
            # NOTE logging of unknown exception required
            msg = f"Failed to prepare grouped asset for mint with an unknown error. {e}."
            logging.critical(msg)
            raise MintError(message=msg, error_id=ErrorIds.UNKNOWN.value)

    @staticmethod  
    def _build_grouped_asset(
        req: schema.MintAssetRequest,
        use_meta: bool = False,
        ) -> mintrpc.MintAsset:
        """
            maps MintAssetRequest schema to the gRPC type for the
            MintAsset nested message of MintAssetRequest.
        """
        try:
            if use_meta:
                # TODO build asset meta data
                pass

            return mintrpc.MintAsset(
                asset_version=req.asset_version.value,
                asset_type=req.asset_type.value,
                name=req.name,
                amount=req.amount,
                #new_grouped_asset=req.new_grouped_asset,
                #grouped_asset=req.grouped_asset,
                group_key=req.group_key
            )
        except Exception as e:
            raise MintError(
                message=f"Failed to map schema.MintAssetRequest to mintrpc.MintAsset with error: {e}",
                error_id=ErrorIds.FAILED_TO_MAP_REQUEST_TO_TYPE.value
            )

    def finalize_batch(self, req: schema.FinalizeBatchRequest = schema.FinalizeBatchRequest()):
        try:
            request = mintrpc.FinalizeBatchRequest(short_response=req.short_response, fee_rate=req.fee_rate)
            res: mintrpc.FinalizeBatchResponse = self.stub.FinalizeBatch(request, metadata=[('macaroon', self._read_macaroon())])
            # TODO work in progress - handle error
            logging.critical("Asset batch minted/broadcast!")
            logging.critical(res)
            data = self.handle_finalize_batch_response(res)
            return data
        except Error as err:
            # NOTE logging required, api handler is caller
            logging.critical(err.message)
            raise err
        except Exception as e:
            # NOTE logging of unknown exception required
            msg = f"Failed to [ finalize / mint / broadcast ] prepared asset batches with an unknown error. {e}."
            logging.critical(msg)
            raise MintError(message=msg, error_id=ErrorIds.UNKNOWN.value)
    
    # NOTE could be static
    def handle_finalize_batch_response(self, res: mintrpc.FinalizeBatchResponse) -> dict:
        # TODO create schema
        broadcast_batches = dict()

        data = MessageToDict(res)
        state = data.get("batch", {}).get("state", None)
        batch_tx_id = data.get("batch", {}).get("batchTxid", None)
        # TODO straggling constant
        if state != "BATCH_STATE_BROADCAST":
            raise MintError(message=f"Failed to broadcast assets in batch. State: {state}", error_id=ErrorIds.FAILED_TO_BROADCAST_MINTED_BATCHES.value)
        
        assets = data.get("batch", {}).get("assets", [])
        for asset in assets:
            # NOTE can only broadcast one batch per asset at a time i.e. no need to check for multiple of
            # one asset
            name = asset["name"]
            broadcast_batches[name] = dict()
            broadcast_batches[name]["amount"] = asset["amount"]
            broadcast_batches[name]["txid"] = batch_tx_id

        return broadcast_batches

    def list_batches(self, req: schema.ListBatchesRequest = schema.ListBatchesRequest()):
        try:
            request = mintrpc.ListBatchRequest(batch_key=req.batch_key, batch_key_str=req.batch_key_str)
            res: mintrpc.ListBatchResponse = self.stub.ListBatches(request, metadata=[('macaroon', self._read_macaroon())])
            # TODO work in progress - handle error
            logging.critical("Asset batches retrived.")
            logging.critical(res)

            return res
        except Error as err:
            # NOTE logging required, api handler is caller
            logging.critical(err.message)
            raise err
        except Exception as e:
            # NOTE logging of unknown exception required
            msg = f"Failed to retrive prepared asset batches with an unknown error. {e}."
            logging.critical(msg)
            raise MintError(message=msg, error_id=ErrorIds.UNKNOWN.value)


    def get_tweaked_group_key_by_name(self, name: str) -> dict:
        batches = self.list_batches()
        # TODO will break if list batches returns anything other than rpc Response
        data = MessageToDict(batches)

        batches = data.get("batches", [])
        if len(batches) > 0:
            # NOTE find BATCH_STATE_FINALIZED and name match
            for batch in batches:
                # TODO straggling constant
                if batch["state"] == "BATCH_STATE_FINALIZED":
                    for asset in batch.get("assets", []):
                        if asset.get("name", "") == name:
                            key_fmt =  base64_to_bytes(asset["groupKey"])
                            logging.critical(f"KEY DECODED FROM LIST BATCHES: {key_fmt}")

                            asset["group_key"] = base64_to_bytes(asset["groupKey"])
                            return asset
        
        # TODO should have an error_id
        raise MintError(message="Tweaked key not found for asset", error_id=ErrorIds.UNKNOWN.value)

    def cancel_batch(self):
        """
            TODO unimplemented
        """
        try:
            pass
        except Exception as e:
            # NOTE logging requried. api endpoint handler is caller
            raise MintError()

