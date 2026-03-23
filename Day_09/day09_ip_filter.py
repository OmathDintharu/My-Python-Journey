all_ips = ["192.168.1.1", "8.8.8.8", "192.168.1.100", "1.1.1.1"]

local_ips = [ip for ip in all_ips if ip.startswith("192.")]

print(local_ips)

input("Press Enter to exit...")
