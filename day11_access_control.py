user_role = "Admin"
password_attempt = "Python123"

if user_role == "Admin" and password_attempt == "Python123":
    print("Welcome Omath ! Full System Access Granted.")
elif user_role == "User" and password_attempt == "Python123":
    print("Welcome User ! Limited Access Granted.")
elif user_role == "Guest" and password_attempt == "Python123":
    print("Welcome Guest ! View-only Access Granted.")
else:
    print("Access Denied ! Intruder Alert!")

input("\nPress Enter for more...")