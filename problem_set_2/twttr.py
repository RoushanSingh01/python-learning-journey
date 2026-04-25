def main():
    # Prompt the user for input
    user_input = input("Input: ")
    
    # Process and output the result
    print("Output: ", end="")
    
    # Define vowels (uppercase and lowercase)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    # Iterate and omit vowels
    for char in user_input:
        if char not in vowels:
            print(char, end="")
    print()

if __name__ == "__main__":
    main()
