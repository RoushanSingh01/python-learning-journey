from itertools import cycle


def generate_seat_letters(number):
    seat_letters = cycle(["A", "B", "C", "D"])

    for seat_index in range(number):
        yield next(seat_letters)


def generate_seats(number):
    current_row = 1
    generated_seats = 0

    while generated_seats < number:
        if current_row == 13:
            current_row += 1
            continue

        for seat_letter in ["A", "B", "C", "D"]:
            if generated_seats >= number:
                break

            yield f"{current_row}{seat_letter}"
            generated_seats += 1

        current_row += 1


def assign_seats(passengers):
    available_seats = generate_seats(len(passengers))

    return {
        passenger: next(available_seats)
        for passenger in passengers
    }


def generate_codes(seat_numbers, flight_id):
    for seat_number in seat_numbers:
        ticket_code = f"{seat_number}{flight_id}"
        yield ticket_code.ljust(12, "0")