from scapy.all import sniff
from packet_processor import process_packet

print("Capturing packets...\n")

sniff(
    prn=process_packet,
    filter="ip",
    count=10
)

print("\nCapture Complete")