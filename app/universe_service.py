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
            asset_name_filter - but goal for now requires returning one asset
        """
        try:
            request = universerpc.AssetStatsQuery(asset_name_filter=asset_name_filter)
            res: universerpc.UniverseAssetStats = self.stub.QueryAssetStats(request, metadata=[('macaroon', self._read_macaroon())])
            # TODO work in progress - handle error
            logging.critical(f"Asset stats received from query for {asset_name_filter}!")
            logging.critical(f"response from query assets: {res}")
            return self.fmt_asset_stats_query(res=res)
        except Error as err:
            # NOTE logging required, api handler is caller
            logging.critical(err.message)
            raise err
        except Exception as e:
            # NOTE logging required, api handler is caller
            msg = f"Failed to get assets stats with unknown error: {e}."
            logging.critical(msg)
            raise UniverseError(message=msg, error_id=ErrorIds.UNKNOWN.value)
    
    def fmt_asset_stats_query(self, res: universerpc.UniverseAssetStats):
        """
        # TODO type response

            NOTE per asset_stats_query, using asset_name_filter to return exactly
                 one match. That is why we are performing len check of 2 (this seems like an odd quirk in how the Response is structured IMHO)
        """
        output = dict()
        data = MessageToDict(res)
        group_data = data.get("assetStats", [])

        if len(group_data) != 2:
            raise UniverseError(message="filter on Universe Asset Stats returned more than one asset. Unable to handle.", error_id=ErrorIds.UNKNOWN.value)
        
        subsequent_groups = group_data[0]
        init_mint_group = group_data[1].get("asset", None)
        # NOTE this should always be 1
        init_mint_proofs = int(group_data[1].get("totalProofs", "1"))

        if init_mint_group is None:
            raise UniverseError(message="Initial group not found. This could indicate an asset where enable_emissions is False.", error_id=ErrorIds.UNKNOWN.value)

        output["name"] = init_mint_group["assetName"]
        output["genesis_point"] = init_mint_group["genesisPoint"]
        # TODO determine exactly how sensitive this is as an issuer? as an non-issuer owner?
        output["group_key"] = subsequent_groups["groupKey"]
        output["total_supply"] = int(subsequent_groups["groupSupply"]) + int(init_mint_group["totalSupply"])
        output["total_proofs"] = int(subsequent_groups["totalProofs"]) + init_mint_proofs
        output["group_anchor"] = subsequent_groups["groupAnchor"]

        return output