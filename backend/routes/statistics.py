from fastapi import APIRouter

from services.statistics_service import get_statistics

router = APIRouter()


@router.get("/statistics")
def statistics():

    return get_statistics()