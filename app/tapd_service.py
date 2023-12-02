import logging # TODO note ensure setup properly
import codecs, grpc, os
from google.protobuf.json_format import MessageToDict
from app.schemas.error import Error, ErrorIds
from app.schemas.taproot import ListAssetRequest
from app.lit import taprootassets_pb2_grpc as taprootstub
from app.lit import taprootassets_pb2 as taprootrpc
"""
    NOTE for application efficiency consider a pattern where these parent
    types are initialized at startup and passed to children in api path
    handlers for each request
"""
class Tapd:
    def __init__(self):
        try:
            # TODO consider privacy / security of these instance
            self.uri = os.environ["LND_URI"] # NOTE do we ever need the Tapd URI direct or only the LiT URI?
            self.tls_path = os.environ["TLS_CERT"]
            self.macaroon_path = os.environ["TAPD_MACAROON"]
            self.channel = self._create_secure_channel()

        except Error as e:
            detail = "Tapd parent init failed"
            logging.critical(f"{detail} : {e.message} : {e.error_id}")
            e.detail = detail
            raise e
        except Exception as e:
            # NOTE unknown error occurred
            message = f"Tapd parent init failed with an unknown error. Error: {e}"
            logging.critical(message)
            raise Error(message=message, error_id=ErrorIds.UNKNOWN.value)
    
    def _create_taproot_stub(self):
        try:
            return taprootstub.TaprootAssetsStub(self.channel)
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
        
    def list_assets(self, req: ListAssetRequest):
        try:
            stub = self._create_taproot_stub()
            request = taprootrpc.ListAssetRequest(
                with_witness=req.with_witness, 
                include_spent=req.include_spent, 
                include_leased=req.include_leased
            )
            response: taprootrpc.ListAssetResponse = stub.ListAssets(request ,metadata=[('macaroon', self._read_macaroon())])
            # TODO work in progress - handle error
            logging.critical("Received asset list.")
            #logging.critical(response)
            # TODO requires error handling and mapping
            #return response
            return self.agg_list_assets_by_name(response)
        except Error as err:
            # NOTE logging required, this is a macaroon read error
            logging.critical(err.message)
            raise err
        except Exception as e:
            # NOTE logging of unknown exception required
            msg = f"Failed to retrive list of known assets with error: {e}"
            logging.critical(msg)
            raise Error(message=msg, error_id=ErrorIds.UNKNOWN.value)
        

    def list_groups(self):
        """
            TODO unimplemented
        """
        pass
    
    # NOTE could be static
    def agg_list_assets_by_name(self, res: taprootrpc.ListAssetResponse) -> list:
        """
            TODO create a schema for the items in the list,
                 this should also be used as the response type for list-assets
        """
        asset_map = dict()
        data = MessageToDict(res)
        assets = data.get("assets", [])

        if len(assets) == 0:
            # TODO create an error_id
            raise Error(message="No assets found.", error_id=ErrorIds.UNKNOWN.value)
        
        for asset in assets:
            name = asset["assetGenesis"]["name"]
            if name in asset_map:
                # NOTE existing asset found in map -- asset id is unique to a group however the rawGroupKey is shared
                asset_map[name]["groups"] += 1
                asset_map[name]["supply"] += float(asset["amount"])

            else:
                # NOTE new asset added to map
                asset_map[name] = dict()
                asset_map[name]["supply"] = float(asset["amount"])
                asset_map[name]["groups"] = 1

        return [{"name": key, "supply": asset_map[key]["supply"], "groups": asset_map[key]["groups"]} for key in asset_map.keys()]

        
        