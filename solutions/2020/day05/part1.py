from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    seats = [line.strip() for line in f.readlines()]

trans = str.maketrans("FBLR", "0101")

seat_ids = [int(seat.translate(trans), 2) for seat in seats]
print(max(seat_ids))
