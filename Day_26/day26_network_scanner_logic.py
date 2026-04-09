# Day 25 වල ඉගෙන ගත්තු String Analytics සහ Day 26 වල Logic පාවිච්චි කරමු
log_data = [
    "192.168.1.1 - Login Success",
    "10.0.0.5 - ERROR: Unauthorized Access",
    "192.168.1.50 - Login Success",
    "172.16.0.10 - ERROR: Multiple Failed Attempts",
    "8.8.8.8 - Login Success"
]

# Senior-level Logic: 'List Comprehension' පාවිච්චි කරලා එක පේළියෙන් වැඩේ කරමු
threats = [data for data in log_data if "ERROR" in data]

print("--- 🚨 THREAT ANALYSIS REPORT ---")
if threats:
    for t in threats:
        print(f"[THREAT DETECTED]: {t}")
else:
    print("[SAFE]: No threats found.")

# Day 26 Advance: 'return' පාවිච්චි කරලා summary එකක් ගමු
def get_threat_count(found_threats):
    return len(found_threats)

print(f"\nTotal threats found: {get_threat_count(threats)}")
