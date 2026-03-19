correct_password = "japan_mext_2028"
password_list = ["123456" , "admin123" , "password" , "japan_mext_2028" , "qwerty"]

print("--- Starting Brute Force Attack Simulation ---")
print()

for attempt in password_list:
    print(f"Testing password: {attempt}...")

    if attempt == correct_password:
        print(f"\n[SUCCESS] Password Found: {attempt} ")
        print("System Access Granted!")
        break

    else:
        print("[FAILED] Incorrect password. Trying next...")

print("\n--- Simulation Ended ---")

input("\nPress Enter to exit...")