my_vault =  {
    "name": "Omath Ditharu",
    "hobby": "Cursive Handwriting",
    "target_country": "Le Japon",
    "special_status": "Top Secret",
    "coding_level": 10
}

print(f"My current hobby: {my_vault['hobby']}")

my_vault["exam_status"] = "O/L Results Pending"

my_vault["coding_level"] = 11

print("\n--- ACCESSING PRIVATE VAULT ---")
for key, value in my_vault.items():
    print(f"{key.upper()}: {value}")

print("\nSystem Encrypted. Happy Ajalah !")