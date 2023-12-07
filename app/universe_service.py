import logging
from app.tapd_service import Tapd
from app.utils import base64_to_bytes
from app.lit import universe_pb2 as universerpc
from app.lit import universe_pb2_grpc as  universestub
from app.schemas.universe import AssetRootRequest, ProofType, AssetLeavesRequest
from app.schemas.error import Error, ErrorIds
from google.protobuf.json_format import MessageToDict

class UniverseError(Error):
    """
        NOTE not to be used in initialization method.
    """
    category: str = "universerpc"


"""
    NOTE for application efficiency consider a pattern where these parent
    objects (Tapd) are initialized at startup and passed to children in api path
    handlers for each request

    NOTE consider passing Tapd to services via endpoint dependency injection (it still must be initialized once)
    then it will be received as an initialization parameter instead of
    via inheritance.
"""
class Universe(Tapd):
    def __init__(self):
        try:
            Tapd.__init__(self)
            self.stub = self._create_stub()
        except Error as err:
            if err.error_id == ErrorIds.FAILED_TO_CREATE_GRPC_STUB.value:
                # NOTE if otherwise, detail field is populated by an error initializing Tapd.
                err.detail = "Failed to init Universe (child)."
                logging.critical(f"{err.detail} : {err.message} : {err.error_id}")
            raise err
        except Exception as e:
            # NOTE an unknown error occurred
            msg = f"Faild to init Universe (child). Error: {e}"
            logging.critical(msg)
            raise Error(message=msg, error_id=ErrorIds.UNKNOWN.value)

    def _create_stub(self):
        try:
            return universestub.UniverseStub(self.channel)
        except Exception as e:
            # NOTE no logging, init is caller
            msg = f"Failed to create Universe RPC stub after successful parent Tapd init. Error: {e}"
            raise Error(message=msg, error_id=ErrorIds.FAILED_TO_CREATE_GRPC_STUB.value)
        

    def get_info(self):
        try:
            request = universerpc.InfoRequest()
            res: universerpc.InfoResponse = self.stub.Info(request, metadata=[('macaroon', self._read_macaroon())])
            # TODO work in progress - handle for error
            logging.critical("Universe Info Received!")
            return res
        except Error as err:
            # NOTE logging required, api handler is caller
            logging.critical(err.message)
            raise err
        except Exception as e:
            # NOTE logging of unknown exception required
            msg = f"Failed to get universe info with an unknown error: {e}"
            logging.critical(msg)
            raise UniverseError(message=msg, error_id=ErrorIds.UNKNOWN.value)
    
    def list_federation_servers(self):
        try:
            request = universerpc.ListFederationServersRequest()
            res: universerpc.ListFederationServersResponse = self.stub.ListFederationServers(request, metadata=[('macaroon', self._read_macaroon())])
            # TODO work in progress - handle error
            logging.critical("Universe federation servers received!")
            return res
        except Error as err:
            # NOTE logging required, api handler is caller
            logging.critical(err.message)
            raise err
        except Exception as e:
            # NOTE logging required, api handler is caller
            msg = f"Failed to get universe federation servers with an unknown error: {e}"
            logging.critical(msg)
            raise UniverseError(message=msg, error_id=ErrorIds.UNKNOWN.value)
    
    def get_stats(self):
        try:
            request = universerpc.StatsRequest()
            res: universerpc.StatsResponse = self.stub.UniverseStats(request, metadata=[('macaroon', self._read_macaroon())])
            # TODO work in progress - handle error
            logging.critical("Universe stats received!")
            return res
        except Error as err:
            # NOTE logging required, api handler is caller
            logging.critical(err.message)
            raise err
        except Exception as e:
            # NOTE logging required, api handler is caller
            msg = f"Failed to get universe stats with unknown error: {e}"
            logging.critical(msg)
            raise UniverseError(message=msg, error_id=ErrorIds.UNKNOWN.value)

    def get_asset_roots(self, req: AssetRootRequest = AssetRootRequest()):
        try:
            request = universerpc.AssetRootRequest(
                with_amounts_by_id=req.with_amounts_by_id,
                offset=req.offset,
                limit=req.limit,
                direction=req.direction.value
            )
            res: universerpc.AssetRootResponse = self.stub.AssetRoots(request, metadata=[('macaroon', self._read_macaroon())])
            # TODO work in progress - handle error
            logging.critical("Universe asset roots received!")
            return res
        except Error as err:
            # NOTE logging required, api handler is caller
            logging.critical(err.message)
            raise err
        except Exception as e:
            # NOTE logging required, api handler is caller
            msg = f"Failed to get universe asset roots with unknown error: {e}"
            logging.critical(msg)
            raise UniverseError(message=msg, error_id=ErrorIds.UNKNOWN.value)
    
    #def get_asset_leaves_by_proof_type(self, asset_id_str: str):
    def get_asset_leaves_by_proof_type(self, req: AssetLeavesRequest):
        try:
            #asset_id_bytes = base64_to_bytes(asset_id_str)
            asset_id_bytes = base64_to_bytes(req.asset_id)
            group_key_bytes = base64_to_bytes(req.group_key)
            #logging.critical(asset_id_bytes)
            logging.critical(req.group_key)
            request = universerpc.ID(group_key=group_key_bytes, proof_type=req.proof_type)
            res: universerpc.AssetLeafResponse = self.stub.AssetLeaves(request, metadata=[('macaroon', self._read_macaroon())])
            # TODO work in progress - handle error
            logging.critical(f"Universe asset leaves received! {MessageToDict(res)}")
            return res
        except Error as err:
            # NOTE logging required, api handler is caller
            logging.critical(err.message)
            raise err
        except Exception as e:
            # NOTE logging required, api handler is caller
            msg = f"Failed to get universe asset leaves with unknown error: {e}"
            logging.critical(msg)
            raise UniverseError(message=msg, error_id=ErrorIds.UNKNOWN.value)
        
    def asset_stats_query(self, asset_name_filter: str):
        """
            NOTE query can be expanded significantly beyond
            asset_name_filter
        """
        try:
            request = universerpc.AssetStatsQuery(asset_name_filter=asset_name_filter)
            res: universerpc.UniverseAssetStats = self.stub.QueryAssetStats(request, metadata=[('macaroon', self._read_macaroon())])
            # TODO work in progress - handle error
            logging.critical(f"Asset stats received from query for {asset_name_filter}!")
            return res
        except Error as err:
            # NOTE logging required, api handler is caller
            logging.critical(err.message)
            raise err
        except Exception as e:
            # NOTE logging required, api handler is caller
            msg = f"Failed to get assets stats with unknown error: {e}."
            logging.critical(msg)
            raise UniverseError(message=msg, error_id=ErrorIds.UNKNOWN.value)