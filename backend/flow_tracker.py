from datetime import datetime

flows = {}

def update_flow(source_ip, destination_ip, packet_length):

    flow_key = (source_ip, destination_ip)

    if flow_key not in flows:

        flows[flow_key] = {
            "packet_count": 0,
            "total_bytes": 0,
            "start_time": datetime.now()
        }

    flows[flow_key]["packet_count"] += 1
    flows[flow_key]["total_bytes"] += packet_length


def print_flows():

    print("\n========== ACTIVE FLOWS ==========\n")

    for flow, data in flows.items():

        duration = (
            datetime.now()
            - data["start_time"]
        ).total_seconds()

        print(f"Flow: {flow[0]} -> {flow[1]}")
        print(f"Packets     : {data['packet_count']}")
        print(f"Total Bytes : {data['total_bytes']}")
        print(f"Duration    : {duration:.2f} sec")
        print("--------------------------------")