def main():
    amount_due = 50
    accepted_coins = [25, 10, 5]

    # Keep asking until amount_due is 0 or less
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        try:
            coin = int(input("Insert Coin: "))
            
            # If coin is valid, subtract from amount due
            if coin in accepted_coins:
                amount_due -= coin
                
        except ValueError:
            # Ignore non-integer inputs
            continue

    # Output how many cents in change the user is owed
    print(f"Change Owed: {abs(amount_due)}")

if __name__ == "__main__":
    main()
