print("--- SECURE VAULT SYSTEM ---")

keycard = input("Do you have the keycard ? (y/n): ").lower()
pin = input("Enter the 4-digit PIN: ")
admin_status = input("Are you an admin ? (y/n): ").lower()

has_keycard = (keycard == 'y')
knows_pin = (pin == '1234')
is_admin = (admin_status == 'y')


if(has_keycard and knows_pin) or is_admin:
    print("\n[SUCCESS] Valut Access Granted !")

else:
    print("\n[DENIED] Security Alert ! Intruders detected.")


input("\nPress Enter to exit...")