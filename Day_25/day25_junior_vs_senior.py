def junior_way(number):
    """How a Junior Developer writes code"""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def senior_way(number):
    """How a Senior Developer writes code"""
    return "Even" if number % 2 == 0 else "Odd"

num = 24

print(f"Junior Way: {num} is {junior_way(num)}")
print(f"Senior Way: {num} is {senior_way(num)}")

input("\nPress Enter to Exit...")
