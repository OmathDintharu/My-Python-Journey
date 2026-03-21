stored_username = "Omath_Admin"
stored_password = "Japan2026"
stored_level = 5

def secure_login():
    print("--- WELCOME TO SECURE TERMINAL ---")
    
    input_user = input("Enter Username: ")
    input_pass = input("Enter Password: ")


    if input_user == stored_username and input_pass == stored_password:
        print("\nLogin Successful! Checking Security Clearance...")
        
        if stored_level >= 7:
            return "ACCESS GRANTED: Full System Control."
        elif stored_level >= 5:
            return "WARNING: Limited Access. System Monitoring Enabled."
        else:
            return "ACCESS DENIED: Insufficient Security Level."
    else:
        return "ERROR: Invalid Username or Password. System Locked!"


status = secure_login()
print(status)

input("\nPress Enter to exit...")