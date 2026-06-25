from alert_logger import save_alert

save_alert(
    source_ip="192.168.1.10",
    destination_ip="8.8.8.8",
    attack_type="Port Scan",
    risk_score=95,
    severity="Critical",
    action="Recommend Blocking"
)