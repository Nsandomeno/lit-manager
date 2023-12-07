from pydantic import BaseModel
from enum import Enum
from typing import Optional

class SortDirection(Enum):
    SORT_DIRECTION_ASC  = 0
    SORT_DIRECTION_DESC = 1


class ProofType(Enum):
    PROOF_TYPE_UNSPECIFIED = 0
    PROOF_TYPE_ISSUANCE    = 1
    PROOF_TYPE_TRANSFER    = 2


class AssetRootRequest(BaseModel):
    with_amounts_by_id: bool = True
    offset            : int = 0
    limit             : int = 50
    direction         : SortDirection = SortDirection.SORT_DIRECTION_DESC



class AssetLeavesRequest(BaseModel):
    asset_id      : Optional[str] = None
    #asset_id_str  : Optional[str] = None
    group_key     : Optional[str] = None
    #group_key_str : Optional[str] = None
    proof_type    : int = ProofType.PROOF_TYPE_ISSUANCE.value

