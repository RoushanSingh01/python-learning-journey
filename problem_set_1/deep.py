# deep.py

def main():
    # Prompt user for input and normalize it: remove whitespace and lowercase
    answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

    # Check for correct answers
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")

main()