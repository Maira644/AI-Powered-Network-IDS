from fastapi import APIRouter

from services.alert_service import get_all_alerts

router = APIRouter()


@router.get("/alerts")
def get_alerts():

    return get_all_alerts()