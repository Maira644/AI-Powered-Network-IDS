import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "database")
    )
)

from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import insert
from datetime import datetime

from models import engine, blocked_ips

router = APIRouter()


class BlockIPRequest(BaseModel):
    ip_address: str
    reason: str


@router.post("/block-ip")
def block_ip(request: BlockIPRequest):

    query = insert(blocked_ips).values(
        ip_address=request.ip_address,
        reason=request.reason,
        blocked_at=datetime.now()
    )

    with engine.begin() as connection:
        connection.execute(query)

    return {
        "message": "IP blocked successfully",
        "ip_address": request.ip_address
    }