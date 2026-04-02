"""
File: Day19_Documenting_Progress.py
Author: Omath Dintharu
Description: Organizing Hiragana letters and Restaurant items using Lists with proper documentation.

"""
#--- TOPIC: JAPANESE HIRAGANA PROGRESS ---
#Storing the first 10 characters learned today 
hiragana_list = ["a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko"]

def display_progress(data_lsit):
    """

    This function calculates the length of the list and displays the items.
    Usage: Call this to see how many items you've mastered.

    """
    print(f"Mastery Count: {len(data_lsit)}")
    print(f"Items: {data_lsit}")

#--- TOPIC: RESTURANT MENU DREAMS ---
# My dream menu items for my resturant by age 30.
menu_list = ["Special Fried Rice", "Kottu Supreme", "Japanese Ramen"]

# Calling the function to see output
display_progress(hiragana_list)
display_progress(menu_list)

# To stop the flashing bug in python
input("\nPress Enter to Exit...")
