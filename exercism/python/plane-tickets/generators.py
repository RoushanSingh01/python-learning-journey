from itertools import cycle


def generate_seat_letters(number):
    seats = cycle(["A", "B", "C", "D"])

    for _ in range(number):
        yield next(seats)


def generate_seats(number):
    row = 1
    generated = 0

    while generated < number:
        if row == 13:
            row += 1
            continue

        for seat in ["A", "B", "C", "D"]:
            if generated >= number:
                break

            yield f"{row}{seat}"
            generated += 1

        row += 1


def assign_seats(passengers):
    seats = generate_seats(len(passengers))

    return {
        passenger: next(seats)
        for passenger in passengers
    }


def generate_codes(seat_numbers, flight_id):
    for seat in seat_numbers:
        ticket = f"{seat}{flight_id}"
        yield ticket.ljust(12, "0")