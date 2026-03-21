def check_access(username, security_level):
    if security_level >= 5:
        return f"Access GRANTED for {username}. Welcome to the Secure Server."
    elif security_level >= 3:
        return f"WARNING: {username}, you have LIMITED access. Be careful !"
    else:
        return f"Access DENIED for {username}. High Security Clearence required !"
    

user = "Omath_Admin"
level = 4

print(check_access(user, level))

input("Press ENTER to exit...")