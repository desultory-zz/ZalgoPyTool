#Zalgoes your text and copies it to your clipboard
#uses text in clipboard with default values if no arguments are passed

import argparse
import random
import pyperclip

DEFAULT_UP = 5
DEFAULT_THROUGH = 5
DEFAULT_DOWN = 5
CURRENT_CLIPBOARD = pyperclip.paste()

parser = argparse.ArgumentParser(description='Zalgoes text')
parser.add_argument('--input', '-i', type=str, help="Text you want to ruin", default=CURRENT_CLIPBOARD)
parser.add_argument('--up', '-u', type=int, help="Distance up", default=DEFAULT_UP)
parser.add_argument('--through', '-t', type=int, help="Number through", default=DEFAULT_THROUGH)
parser.add_argument('--down', '-d', type=int, help="Distance down", default=DEFAULT_DOWN)
parser.add_argument('--to-ascii', action='store_true', help="Converts input to normal ASCII", default=False)

def hex_to_unicode(hex_list):
	return [chr(hex) for hex in hex_list]

def build_above_pool():
	a = [
		0x031A, 0x031B, 0x0346, 0x0357, 0x0358, 0x035B, 0x035D, 0x035E, 0x0360, 0x0361,
		*range(0x0300, 0x0316), *range(0x033D, 0x0345), *range(0x034A, 0x034D),
		*range(0x0350, 0x0353), *range(0x0363, 0x0370)
	]
	a = hex_to_unicode(a)
	return a

def build_below_pool():
	b = [
		0x0345, 0x034D, 0x034E, 0x0359, 0x035A, 0x035C, 0x035F, 0x0362,
		*range(0x0316, 0x031A), *range(0x031C, 0x0334), *range(0x0339, 0x033D),
		*range(0x0347, 0x034A), *range(0x0353, 0x0357)
	]
	b = hex_to_unicode(b)
	return b

def build_through_pool():
	t = list(range(0x0334, 0x0339))
	t = hex_to_unicode(t)
	return t

def build_normal_ascii():
	n = list(range(0x020, 0x07F))
	n = hex_to_unicode(n)
	return n

def get_zalgo(pool, count):
	out = []
	for i in range(count):
		out.append(random.choice(pool))
	return out

def ruin(string, up, inside, down):
	split = list(string)
	above = build_above_pool()
	through = build_through_pool()
	below = build_below_pool()
	for n in range(len(split)):
		temp = split[n]
		temp += ''.join(get_zalgo(above, up))
		temp += ''.join(get_zalgo(through, inside))
		temp += ''.join(get_zalgo(below, down))
		split[n] = temp
	joined = ''.join(split)
	return joined

def clean(string):
	normal_ascii = build_normal_ascii()
	temp = ''
	for c in string:
		if c in normal_ascii:
			temp += c
	return temp

if __name__ == "__main__":
	args = parser.parse_args()

	unmodified = args.input
	n_up = args.up
	n_through = args.through
	n_down = args.down
	mode = args.to_ascii

	if mode:
		modified = clean(unmodified)
	else:
		modified = ruin(unmodified, n_up, n_through, n_down)

	pyperclip.copy(modified)
	print(modified)