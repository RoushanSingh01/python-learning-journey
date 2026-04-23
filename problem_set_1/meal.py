def main():
    # Prompt the user for a time
    time = input("What time is it? ")
    
    # Convert time to a float (hours.minutes)
    hours = convert(time)
    
    # Determine meal time
    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")

def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = time.split(":")
    
    # Convert to float and calculate total hours
    return float(hours) + (float(minutes) / 60)

if __name__ == "__main__":
    main()
