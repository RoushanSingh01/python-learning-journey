# nutrition.py

def main():
    # Dictionary of 20 fruits and their calories based on FDA poster
    fruits_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    # Prompt user for input and normalize to lowercase
    user_input = input("Fruit: ").lower()

    # Output calories if the fruit exists in the dictionary
    if user_input in fruits_calories:
        print("Calories:", fruits_calories[user_input])

if __name__ == "__main__":
    main()
