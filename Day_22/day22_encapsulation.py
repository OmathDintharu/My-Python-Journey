class SecurityVault:
    def __init__(self, owner, secret_key):
        self.owner = owner
        self.__secret_key = secret_key

    def get_vault_access(self):
        return f"\nAccess Granted for {self.owner}! Key is secure."
    

my_vault = SecurityVault ("Omath Dintharu", "SECRET_BY_2034")

print(my_vault.owner)
print(my_vault.get_vault_access())

input("\nPress Enter to exit...")
