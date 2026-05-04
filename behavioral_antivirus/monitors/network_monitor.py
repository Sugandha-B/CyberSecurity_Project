from scapy.all import sniff

def packet_callback(packet):
    print(f"[NETWORK] {packet.summary()}")

def start_network_monitor():
    sniff(prn=packet_callback, store=False)
