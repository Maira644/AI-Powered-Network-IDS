def display_alert(result, source_ip, destination_ip):

    print("\n" + "=" * 50)
    print("           SECURITY ALERT")
    print("=" * 50)

    print(f"Source IP      : {source_ip}")
    print(f"Destination IP : {destination_ip}")
    print(f"Prediction     : {result['prediction']}")
    print(f"Risk Score     : {result['risk_score']}")
    print(f"Severity       : {result['severity']}")
    print(f"Recommendation : {result['action']}")

    print("=" * 50)