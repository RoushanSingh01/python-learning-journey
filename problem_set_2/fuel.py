def main():
    while True:
        fuel = input("Fraction: ")
        try:
            # Split the string and convert to integers
            numerator, denominator = fuel.split("/")
            x = int(numerator)
            y = int(denominator)
            
            # Check for invalid fraction logic
            if x > y:
                continue
                
            # Calculate percentage
            percentage = round((x / y) * 100)
            
            # Determine output label
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            
            # Exit loop on success
            break
            
        except (ValueError, ZeroDivisionError):
            # Reprompt user if input is not integer or Y is 0
            pass

if __name__ == "__main__":
    main()
