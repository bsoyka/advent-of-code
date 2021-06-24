from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    seats = [line.strip() for line in f.readlines()]

trans = str.maketrans("FBLR", "0101")

seat_ids = [int(seat.translate(trans), 2) for seat in seats]
print(list(set(range(min(seat_ids), max(seat_ids) + 1)) - set(seat_ids))[0])
