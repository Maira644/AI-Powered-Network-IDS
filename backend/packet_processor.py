from scapy.layers.inet import IP, TCP, UDP
from flow_tracker import update_flow

def process_packet(packet):

    if IP in packet:

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        protocol = "Other"

        if TCP in packet:
            protocol = "TCP"

        elif UDP in packet:
            protocol = "UDP"

        packet_length = len(packet)
        update_flow(
        source_ip,
        destination_ip,
        packet_length
      )

        print("\n=================================")
        print(f"Source IP      : {source_ip}")
        print(f"Destination IP : {destination_ip}")
        print(f"Protocol       : {protocol}")
        print(f"Packet Length  : {packet_length}")
        print("=================================")