#!.venv/bin/python3

import argparse
from ast import dump
from ctypes import sizeof         # argument parsing
import struct           # data unpacking
from PIL import Image   # image processing

def main():
	# parse cli arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('FILE', help='input image file')
	parser.add_argument('--dst', help='data destination',
		default='/dev/fb0', metavar='/dev/fb*')
	parser.add_argument('--width', help='screen width [px]',
		type=int, default=1920, metavar=' INT')
	parser.add_argument('--height', help='screen height [px]',
		type=int, default=1080, metavar='INT')
	parser.add_argument('--hoff', help='horizontal offset [px]',
		type=int, default=0, metavar=' INT')
	parser.add_argument('--voff', help='vertical offset [px]',
		type=int, default=0, metavar='INT')
	cfg = parser.parse_args()

	img = Image.open(cfg.FILE)
	px  = img.load()

	l = []
	for i in range(cfg.hoff, cfg.height):
		for j in range(cfg.voff, cfg.width):
			temp = tuple(reversed(px[j, i]))
			temp += (0,)
			for k in range(4):
				l.append(temp[k])

	f = open(cfg.dst, "wb")
	buff = bytearray(l)
	f.write(buff)
	f.close()

	img.close()

if __name__ == '__main__':
	main()