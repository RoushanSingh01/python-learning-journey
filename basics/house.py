name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindo")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
