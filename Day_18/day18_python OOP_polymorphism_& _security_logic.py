class SecurityTool:
    def scan(self):
        print("Generic security scan is started...")

class Firewall(SecurityTool):
    def scan(self):
        print("Firewall Scan: Network packets are currently checking...")

class Antivirus(SecurityTool):
    def scan(self):
        print("Antivirus Scan: Malicious files are checking...")


def start_protection(tool):
    tool.scan() 

my_firewall = Firewall()
my_antivirus = Antivirus()

start_protection(my_firewall)  
start_protection(my_antivirus) 

input("\n -----Scan Completed----- Press Enter to exit...")
