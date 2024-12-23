def book_seat(available_seats, booked_seats, seat_number):
    if seat_number in available_seats:
        available_seats.remove(seat_number)
        booked_seats.append(seat_number)
        print(f"Seat {seat_number} successfully booked.")
    else:
        print(f"Seat {seat_number} is already booked or invalid.")

def cancel_seat(available_seats, booked_seats, seat_number):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        available_seats.append(seat_number)
        print(f"Seat {seat_number} booking successfully cancelled.")
    else:
        print(f"Seat {seat_number} is not booked or invalid.")

total_seats = 10
available_seats = list(range(1, total_seats + 1))
booked_seats = [2, 5, 7] 

for seat in booked_seats:
    available_seats.remove(seat)

book_seat(available_seats, booked_seats, 3)  
cancel_seat(available_seats, booked_seats, 5) 

print(f"Available seats: {available_seats}")
