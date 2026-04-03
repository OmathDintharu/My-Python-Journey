# Function to check if the user is eligible
def check_access():
    
    try:
        print("--- System Login Access ---")
        # Taking input from the user
        age = int(input("\nPlease enter your age: "))

        if age >= 18:
            print("Access Granted ! Welcome to secure system.")
        
        elif age < 0:
            print("Error: Age cannot be a negative number.")

        else:
            print("Access Denied: You must be 18 or older.")

    except ValueError:
        # This handles cases where the user enters text instead of numbers
        print("Invalid Input: Please enter a numeric value (e.g., 25)")

    finally:
        # This part always runs regardless of errors
        print("Verification process completed.")


check_access()
input("\nPress enter to exit...")