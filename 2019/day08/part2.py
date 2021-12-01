from pathlib import Path

from advent_of_code_ocr import convert_6  # pip install advent-of-code-ocr

width = 25
length = 6

with (Path(__file__).parent / "input.txt").open() as f:
    start = f.readlines()[0].strip()
pixels = width * length
layers = [start[i : i + pixels] for i in range(0, len(start), pixels)]
final_pixels = []
for pixel_index in range(pixels):
    layer_pixel = "2"
    for layer in layers:
        if layer[pixel_index] == "1":
            layer_pixel = "#"
            break
        elif layer[pixel_index] == "0":
            layer_pixel = "."
            break
    final_pixels.append(layer_pixel)
final_chunks = [
    final_pixels[i : i + width] for i in range(0, len(final_pixels), width)
]

print(convert_6("\n".join("".join(chunk) for chunk in final_chunks)))
