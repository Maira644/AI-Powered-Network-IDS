from detect_and_log import detect_flow

sample_flow = {
    "packet_count": 5000,
    "total_bytes": 500000,
    "duration": 100
}

detect_flow(
    sample_flow,
    "192.168.1.10",
    "8.8.8.8"
)