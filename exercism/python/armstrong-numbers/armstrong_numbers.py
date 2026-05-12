def is_armstrong_number(number):
    digit_string = str(number)
    digit_count = len(digit_string)

    return (
        sum(int(digit) ** digit_count for digit in digit_string)
        == number
    )