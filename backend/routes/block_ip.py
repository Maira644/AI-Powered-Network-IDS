from fastapi import APIRouter
from pydantic import BaseModel

from services.block_service import block_ip

router = APIRouter()


class BlockIPRequest(BaseModel):
    ip_address: str
    reason: str


@router.post("/block-ip")
def block_ip_route(request: BlockIPRequest):

    return block_ip(
        request.ip_address,
        request.reason
    )