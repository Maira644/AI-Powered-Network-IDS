from fastapi import FastAPI

from routes.alerts import router as alerts_router
from routes.statistics import router as statistics_router
from routes.blocked_ips import router as blocked_ips_router
from routes.block_ip import router as block_ip_router

app = FastAPI(
    title="AI-Powered Network IDS",
    version="1.0.0"
)

app.include_router(alerts_router)
app.include_router(statistics_router)
app.include_router(blocked_ips_router)
app.include_router(block_ip_router)


@app.get("/")
def home():

    return {
        "message": "AI-Powered Network IDS API is Running"
    }