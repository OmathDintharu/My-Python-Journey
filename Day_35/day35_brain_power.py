# Python Day 36 - Multi-Skill Brain Power

def calculate_brain_power(logic_skill, language_count, maths_focus):
    # Logic is the base, Language multiplies it
    power = (logic_skill * language_count) + (maths_focus * 10)
    return power

name = "Omath Dintharu"
# High logic (9), 3 Languages, 100% Maths focus
total_power = calculate_brain_power(9, 3, 1)

print(f"--- {name} Brain Status ---")
print(f"Current Power Level: {total_power}/40")
print(f"\nLogic: Diversity in skills leads to innovation! 🚀")
