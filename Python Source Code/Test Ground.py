import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    active_devices = []
    for element in answered_list:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        active_devices.append(device_info)

    return active_devices


ip_range = "192.168.1.1/24"  # Adjust the IP range to match your local network

active_devices = scan(ip_range)

for device in active_devices:
    print(f"IP: {device['ip']}   MAC: {device['mac']}")