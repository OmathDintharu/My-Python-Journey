def secure_login_system():
    try:
        # Taking numeric input from the user
        access_code = int(input("Enter Security Access Code: "))
        
        # Simple authentication logic
        if access_code == 1234:
            print("[+] Access Granted. System Unlocked. ")
        else:
            print("[-] Access Denied. Invalid Credentials! ")
            
    except ValueError:
        # Triggered if the user enters letters instead of numbers
        print("[!] Security Alert: Invalid input type detected! Input must be numeric.")
        
    except Exception as e:
        # Catch-all for any other unexpected system errors
        print(f"[!] A system error occurred. Session logged for review.")
        
    finally:
        # This block always executes to ensure the session is cleared
        print("[*] Security Session Terminated.")

# Execute the system
if __name__ == "__main__":
    secure_login_system()

    input("Press Enter to exit...")
