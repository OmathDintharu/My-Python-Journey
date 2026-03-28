def protect_subaru(*tasks):
    print("Rem is starting her protection routine:")
    for task in tasks:
        print(f"Task Completed: {task}")

protect_subaru("Fighting Cultists", "Healing Subaru", "Cooking Dinner", "Cleaning Mansion")

def character_stats(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

character_stats(Name="Rem", Role="Maid/Protector", Level="High", Weapon="Morning Star")

input("\nMisson Complete Press Enter to exit...")