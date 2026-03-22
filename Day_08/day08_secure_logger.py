import datetime

def log_security_event(username, status):
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{current_time}] User: {username} | Status: {status}\n"

    
    with open("security_logs.txt", "a") as log_file:
        log_file.write(log_entry)
    
    print(f"Successfully logged event for: {username}")



log_security_event("Omath_Admin", "Successful Login")
log_security_event("Unknown_User", "Failed Login Attempt")

input("Press Enter to exit...")
