def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Length check: 2 to 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Must start with at least two letters
    if not s[0:2].isalpha():
        return False

    # Check characters are alphanumeric (no punctuation/spaces)
    if not s.isalnum():
        return False

    # Number logic
    found_number = False
    for i in range(len(s)):
        if s[i].isdigit():
            # The first number cannot be '0'
            if not found_number and s[i] == '0':
                return False
            
            found_number = True
        
        # Numbers cannot be in the middle (no letters after a number starts)
        if found_number and s[i].isalpha():
            return False

    return True


if __name__ == "__main__":
    main()
