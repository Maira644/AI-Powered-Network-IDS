from fastapi import APIRouter

from services.block_service import get_blocked_ips

router = APIRouter()


@router.get("/blocked-ips")
def blocked_ips():

    return get_blocked_ips()