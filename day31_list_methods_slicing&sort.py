languages = ["Japanese", "French", "Russian", "Greman", "Spanish"]

#1.S Slicing (Cut a piece from list)
#Let's get first third languages
top_priority = languages[0:3]

#Sorting
languages.sort()

#Adding And Removing
languages.append("Greek")
languages.remove("Spanish")

print(f"Top 3: {top_priority}")
print(f"Sorted List: {languages}")
