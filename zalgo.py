#Zalgoes your text and copies it to your clipboard
#uses text in clipboard with default values if no arguments are passed

import argparse
import random
import pyperclip

defUp = 5
defThrough = 5
defDown = 5

parser = argparse.ArgumentParser(description='Zalgoes text')
parser.add_argument('--input', '-i', type=str, help="Text you want to ruin", default=pyperclip.paste())
parser.add_argument('--up', '-u', type=int, help="Distance up", default=defUp)
parser.add_argument('--through', '-t', type=int, help="Number through", default=defThrough)
parser.add_argument('--down', '-d', type=int, help="Distance down", default=defDown)
parser.add_argument('--to-ascii', action='store_true', help="Converts input to normal ASCII", default=False)

def hexToUnicode(hex_list):
	return [chr(hex) for hex in hex_list]

def buildAbovePool():
	a = [
		0x031A, 0x031B, 0x0346, 0x0357, 0x0358, 0x035B, 0x035D, 0x035E, 0x0360, 0x0361,
		*range(0x0300, 0x0316), *range(0x033D, 0x0345), *range(0x034A, 0x034D),
		*range(0x0350, 0x0353), *range(0x0363, 0x0370)
	]
	a = hexToUnicode(a)
	return a

def buildBelowPool():
	b = [
		0x0345, 0x034D, 0x034E, 0x0359, 0x035A, 0x035C, 0x035F, 0x0362,
		*range(0x0316, 0x031A), *range(0x031C, 0x0334), *range(0x0339, 0x033D),
		*range(0x0347, 0x034A), *range(0x0353, 0x0357)
	]
	b = hexToUnicode(b)
	return b

def buildThroughPool():
	t = list(range(0x0334, 0x0339))
	t = hexToUnicode(t)
	return t

def buildNormalAscii():
	n = list(range(0x020, 0x07F))
	n = hexToUnicode(n)
	return n

def getZalgo(pool, count):
	out = []
	for i in range(count):
		out.append(random.choice(pool))
	return out

def ruin(string, up, inside, down):
	split = list(string)
	above = buildAbovePool()
	through = buildThroughPool()
	below = buildBelowPool()
	for n in range(len(split)):
		temp = split[n]
		temp += ''.join(getZalgo(above, up))
		temp += ''.join(getZalgo(through, inside))
		temp += ''.join(getZalgo(below, down))
		split[n] = temp
	joined = ''.join(split)
	return joined

def clean(string):
	normalAscii = buildNormalAscii()
	temp = ''
	for c in string:
		if c in normalAscii:
			temp += c
	return temp

if __name__ == "__main__":
	args = parser.parse_args()

	unmodified = args.input
	nUp = args.up
	nThrough = args.through
	nDown = args.down
	mode = args.to_ascii

	if mode:
		modified = clean(unmodified)
	else:
		modified = ruin(unmodified, nUp, nThrough, nDown)

	pyperclip.copy(modified)
	print(modified)