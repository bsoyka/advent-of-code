from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    seats = [line.strip() for line in f.readlines()]

seat_ids = []
trans = str.maketrans("FBLR", "0101")

for seat in seats:
    seat_ids.append(int(seat.translate(trans),2))

print(max(seat_ids))
