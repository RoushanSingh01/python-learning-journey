#Asking the user for their name
name = input("What's your name? ").strip().title()

#splits user's name into first name and last name
first, last  = name.split(" ")

#Say hello to use
print(f"Hello, {first}")
