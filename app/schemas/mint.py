from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class AssetVersion(Enum):
    """
        As of: v0.3.1
    """
    ASSET_VERSION_V0 = 0
    ASSET_VERSION_V1 = 1


class AssetType(Enum):
    """
        As of: v0.3.1
    """
    NORMAL      = 0
    COLLECTIBLE = 1


class AssetMetaType(Enum):
    """
        As of: v0.3.1
    """
    META_TYPE_OPAQUE = 0


class AssetMeta(BaseModel):
    """
        As of: v0.3.1
    """
    data: bytes
    type: AssetMetaType
    meta_hash: Optional[bytes]


class MintAssetRequest(BaseModel):
    """
        As of: v0.3.1
    """
    asset_version     : AssetVersion = AssetVersion.ASSET_VERSION_V1
    asset_type        : AssetType = AssetType.NORMAL
    name              : str
    amount            : int
    asset_meta        : Optional[AssetMeta] = None
    group_key         : Optional[bytes] = None
    group_anchor      : Optional[str] = None

    # NOTE enable_emissions deprecated in v0.3.2
    enable_emissions  : Optional[bool] = None

    # NOTE coming in v0.3.2-beta
    #new_grouped_asset : bool = True
    #grouped_asset     : Optional[bool] = None


class ListBatchesRequest(BaseModel):
    batch_key     : Optional[bytes] = None
    batch_key_str : Optional[str] = None



class FinalizeBatchRequest(BaseModel):
    short_response : bool = False
    fee_rate       : Optional[int] = None


class AddBatchRequest(BaseModel):
    """
        NOTE one of the two fields is required ( I think )
        TODO confirm if group_anchor is simply the name of the
             asset that is going to have another batch minted for it.
        TODO confirm if group_anchor is a pure alternative to passing
             the group_key bytes
        TODO confirm if there is any work in handling the group_key
                bytes over HTTP
        
        genesis_point: "fb0a4eb10d2d228ceb0b73fd86fc92885992675a5e8d484d1662f500b76707ba:1"
        id: "#P\305\215\271\203\230\323\177\210:\370+\016\356*\340\314\213\2003\207l\246\336%\330\020b\212(\003"
        name: "O53A0U"
        anchor_tx: "\002\000\000\000\000\001\001\272\007g\267\000\365b\026MH\215^Zg\222Y\210\222\374\206\375s\013\353\214\"-\r\261N\n\373\001\000\000\000\000\377\377\377\377\002\350\003\000\000\000\000\000\000\"Q h\372Ijr\337zG\365\2271\035b\332\005\262x=\341\220A\3518\2559\326=L\366\303]\005j3\000\000\000\000\000\000\"Q \321F\244$\261\031\325c\232 \335\216\251\271+\303`\360:\250|\2106\216\003\277\221\312\255\230r]\001@\3243\002\214ayE\032\256u\233\302\223\022\017\310\364rO\214Xw\302\223\3755\273\235\332}\311\363\266\234rpm\330\006\275\326(O\336\206\253\030\330\017\274\346\355\216\"\244\204\213\017\266N\374\334J\360\000\000\000\000"               
        anchor_block_hash: "0000000001be1aab99afb81cb76cc279be0aaa9da9ce21336651340f7b0331cf"
        anchor_outpoint: "14f30de2d505db7ca84a93b8409f6bdf8e81c42b3c76a410209de9a21f30eec6:0"
        raw_group_key: "\003\365\213<\002\214\225\021\327\246\322\262\277H|\010\204\350\222B\363\352\302*AP\363o@.\355j>"
        tweaked_group_key: "\003\t\360\001\377\252\020\020.\351\005\246z\220\240\027f\334\260\321\252\332w9\322\315\'6\334\251\322V+"
    """
    name         : str =  "O53A0U"
    amount       : int

