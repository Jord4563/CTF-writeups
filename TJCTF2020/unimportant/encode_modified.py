#!/usr/bin/env python3

from PIL import Image
import binascii

def encode(img, bits):
	pixels = img.load()
	i = 0
	for x in range(img.width):
		for y in range(img.height):
			pixel = pixels[x,y]
			pixel = (pixel[0], pixel[1]&~0b10|(bits[i]<<1), pixel[2], pixel[3])
			pixels[x,y] = pixel
			i += 1
			if i == len(bits):
				return

img = Image.open("source.png")

with open("flag.txt", "rb") as f:
	flag = f.read()
print(flag)
binstr = bin(int(binascii.hexlify(flag), 16))
print(binstr)
bits = [int(x) for x in binstr[2:]]
sb = ''

for bit in bits[:8 * len(flag)]:
	sb += str(bit)

print(sb)

encode(img, bits)

img.save("unimportant2.png")
