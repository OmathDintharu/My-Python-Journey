password = "secure_password123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter Security Token: ")
    
    if user_input == password:
        print("Access Granted! Welcome to the Secure-Tech Hub.")
        break  
    else:
        attempts += 1
        print(f"Access Denied. Attempts remaining: {max_attempts - attempts}")

if attempts == max_attempts:
    print("SYSTEM LOCKED! Unauthorized access detected.")

input("\nPress Enter to exit...")
