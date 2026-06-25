from scapy.all import sniff
from packet_processor import process_packet
from flow_tracker import print_flows

print("Capturing packets...\n")

sniff(
    prn=process_packet,
    filter="ip",
    count=20
)

print_flows()

print("\nCapture Complete")