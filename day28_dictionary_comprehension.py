planets_temp_c = {
    "Mercury": 167,
    "Venus": 464,
    "Earth": 15,
    "Mars": -65,
    "Jupiter": -110
}

planets_temp_f = {planet: (temp * 9/5) + 32 for(planet, temp) in planets_temp_c.items()}

print("Temperatures in Fahrenheit:")
print(planets_temp_f)

hot_planets = {planet: temp for (planet, temp) in planets_temp_f.items() if temp > 100}
print("\nHot Planets (>100°F):")
print(hot_planets)

input("\nPress Enter to Exit...")