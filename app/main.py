import logging
from app.mint_service import Mint
from app.lnd_service import Lnd
from app.utils import configure_environment
from app.schemas.taproot import ListAssetRequest
from app.schemas.mint import MintAssetRequest, AddBatchRequest
from app.schemas.error import Error, ErrorIds
from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from google.protobuf.json_format import MessageToDict

configure_environment()

logger = logging.getLogger("fastapi")

app = FastAPI()
origins = ["*"] # TODO address security

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"success": True}

@app.get("/wallet-balance")
async def wallet_balance():
    # TODO authenticated (?); list assets
    try:
        lnd = Lnd()
        balance = lnd.wallet_balance()
        return {"success": True, "data": MessageToDict(balance)}
    
    except Error as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=err.message
        )
    except Exception as e:
        # NOTE unknown, likely connectivity/CORS, issue
        # logging required
        msg = f"Failed to handle request with error: {e}."
        logger.error(msg)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=msg
        )

@app.get("/list-batches")
async def list_batches():
    try:
        mint = Mint()
        prepared_batches = mint.list_batches()

        return {"success": True, "data": MessageToDict(prepared_batches)}
    except Error as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=err.message
        )
    except Exception as e:
        # NOTE unknown, likely connectivity/CORS, issue
        # logging required
        msg = f"Failed to handle request with error: {e}."
        logger.error(msg)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=msg
        )


@app.get("/list-assets")
async def list_assets(
    with_witness   : bool = False,
    include_spent  : bool = False,
    include_leased : bool = False,
):
    # TODO authenticated (?); list assets
    try:
        params = ListAssetRequest(with_witness=with_witness, include_spent=include_spent, include_leased=include_leased)
        mint = Mint()
        assets = mint.list_assets(params)

        return {"success": True, "data": assets}
    
    except Error as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=err.message
        )
    except Exception as e:
        # NOTE unknown, likely connectivity/CORS, issue
        # logging required
        msg = f"Failed to handle request with error: {e}."
        logger.error(msg)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=msg
        )
    
@app.post("/mint-asset")
async def mint_asset(
    payload: MintAssetRequest
):
    try:
        logger.warning(f"Handled request: {payload.asset_version}")
        # TODO authenticated; mint asset
        # TODO determine whether or not to handle asset metadata separately
        mint = Mint()
        prepared_batch = mint.mint_grouped_asset(payload)
        return {"success": True, "data": MessageToDict(prepared_batch)}
    except Error as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=err.message
        )
    except Exception as e:
        # NOTE unknown, likely connectivity/CORS, issue
        # logging required
        msg = f"Failed to handle request with error: {e}."
        logger.error(msg)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=msg
        )
    

@app.post("/mint-new-group")
async def mint_new_group(
    payload: AddBatchRequest,
):
    try:
        mint = Mint()
        data = mint.get_tweaked_group_key_by_name(payload.name)

        asset = MintAssetRequest(
            name=payload.name, 
            amount=payload.amount, 
            group_key=data["group_key"]
        )

        prepared_batch = mint.mint_grouped_asset(asset)
        return {"success": True, "data": MessageToDict(prepared_batch)}
    
    except Error as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=err.message
        )
    except Exception as e:
        # NOTE unknown, likely connectivity/CORS, issue
        # logging required
        msg = f"Failed to handle request with error: {e}."
        logger.error(msg)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=msg
        )   

@app.post("/finalize-batches")
async def finalize_batches():
    # TODO authenticated; finalize mint asset batch
    # TODO if enable_emission is this endpoint used for a follow-on batches?
    try:
        mint = Mint()

        broadcast_assets = mint.finalize_batch()
        return {"success": True, "data": broadcast_assets}
    except Error as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=err.message
        )
    except Exception as e:
        # NOTE unknown, likely connectivity/CORS, issue
        # logging required
        msg = f"Failed to handle request with error: {e}."
        logger.error(msg)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=msg
        )

@app.post("/sign-in")
async def sign_in():
    # TODO authenticate a node
    # TODO MVP auth: tls.cert, tls.key, node IP
    return {"success": True, "note": "unimplemented."}

@app.post("/cancel-batch")
async def cancel_batch():
    # TODO authenticated; cancel specific batch
    return {"success": True, "note": "unimplemented."}

