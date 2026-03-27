mansion_members = ["Subaru", "Emilia", "Rem", "Ram", "Beatrice", "Roswaal"]

print("--- Mansion Security Scan Start ---")

for person in mansion_members:

    if person == "Rem":
        print(f"{person}: The Most Loyal Maid (Priority Support !)")

    elif person == "Roswaal":
        print(f"{person}: Suspicious Mastermind (Watch closely...)")

    elif person == "Subaru":
        print(f"\n{person}: The Hero (Return by Death Active)")

    else:
        print(f"{person}: Mansion Resident")

print("\n--- Scan Complete: Systems Secure ---")
print("\nPress Enter to Eixt...")
