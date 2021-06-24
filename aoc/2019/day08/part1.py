from pathlib import Path

width = 25
length = 6

with (Path(__file__).parent / 'input.txt').open() as f:
    start = f.readlines()[0].strip()
pixels = width * length
layers = [start[i : i + pixels] for i in range(0, len(start), pixels)]
layer_zeros = [layer.count('0') for layer in layers]
min_zeroes = min(layer_zeros)
res_layer = layers[layer_zeros.index(min_zeroes)]
res = res_layer.count('1') * res_layer.count('2')
print(res)
