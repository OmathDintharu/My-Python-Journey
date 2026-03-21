def check_access(username, security_level):
    if security_level >= 5:
        return f"Access GRANTED for {username}. Welcome to the Secure Server."
    elif:
        return f"Access DENIED for {username}. High Security Clearance required !"
    
user = "Omath_Admin"
level = 7

result = check_access(user, level)
print(result)


input("\nPress Enter to Exit...")
