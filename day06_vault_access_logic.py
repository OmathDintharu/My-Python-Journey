has_keycard = True
knows_pin = False
is_admin = True


if (has_keycard and knows_pin) or is_admin:
    print("Vault Access Granted !")

else:
    print("Security Alert ! Access Denied !")

input("\nPress Enter to exit...") 