width = 25
length = 6

with open("input.txt") as f:
    start = f.readlines()[0].strip()
pixels = width * length
layers = [start[i:i+pixels] for i in range(0, len(start), pixels)]
final_pixels = []
for pixel_index in range(pixels):
    layer_pixel = "2"
    for layer in layers:
        if layer[pixel_index] == "1":
            layer_pixel = "█"
            break
        elif layer[pixel_index] == "0":
            layer_pixel = " "
            break
    final_pixels.append(layer_pixel)
final_chunks = [final_pixels[i:i+width] for i in range(0, len(final_pixels), width)]
for chunk in final_chunks:
    print("".join(chunk))