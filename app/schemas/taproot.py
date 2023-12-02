from pydantic import BaseModel
from typing import Optional
from app.schemas.mint import AssetVersion, AssetType

class ListAssetRequest(BaseModel):
    with_witness   : bool = False
    include_spent  : bool = False
    include_leased : bool = False


class AssetGroup(BaseModel):
    """
        TODO add validation to ensure one of
        raw_group_key and tweaked_group_key are present.
    """
    raw_group_key     : Optional[bytes] = None
    tweaked_group_key : Optional[bytes] = None
    asset_witness     : Optional[bytes] = None


class GenesisInfo(BaseModel):
    genesis_point: str
    name         : str
    meta_hash    : Optional[bytes] = None
    asset_id     : Optional[bytes] = None
    asset_type   : Optional[AssetType] = None
    output_index : Optional[int] = None
    version      : Optional[int] = None


class Asset(BaseModel):
    """
        TODO not using all fields in the RPC message itself
        so it should have extra fields enabled.
    """
    script_key_is_local : Optional[bool] = True
    version             : Optional[AssetVersion] = AssetVersion.ASSET_VERSION_V1.value
    asset_group         : Optional[AssetGroup] = None


