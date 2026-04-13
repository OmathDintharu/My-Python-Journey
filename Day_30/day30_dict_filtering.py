# Day 30: Dictionary Comprehension (Filtering) 🛡️
# Goal: Filter students who scored more than 75

scores = {
    "Omath": 95,
    "Amal": 60,
    "Nimal": 82,
    "Kamal": 45,
    "Saman": 88
}

# Filtering logic: {key: value for (key, value) in dict.items() if condition}
top_students = {name: score for name, score in scores.items() if score > 75}

print(f"All Scores: {scores}")
print(f"Top Students (>75): {top_students}")
