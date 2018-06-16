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

ABOVE_POOL = [chr(dec) for dec in [
			768, 769, 770, 771, 772, 773, 774, 775, 776, 777,
			778, 779, 780, 781, 782, 783, 784, 785, 786, 787,
			788, 789, 794, 795, 829, 830, 831, 832, 833, 834,
			835, 836, 838, 842, 843, 844, 848, 849, 850, 855,
			856, 859, 861, 862, 864, 865, 867, 868, 869, 870,
			871, 872, 873, 874, 875, 876, 877, 878, 879
			]]
THROUGH_POOL = [chr(dec) for dec in [820, 821, 822, 823, 824]]
BELOW_POOL = [chr(dec) for dec in [
			790, 791, 792, 793, 796, 797, 798, 799, 800, 801,
			802, 803, 804, 805, 806, 807, 808, 809, 810, 811,
			812, 813, 814, 815, 816, 817, 818, 819, 825, 826,
			827, 828, 837, 839, 840, 841, 845, 846, 851, 852,
			853, 854, 857, 858, 860, 863, 866
			]]

def get_zalgo(pool, count):
	zalgo_string = []
	for i in range(count):
		zalgo_string.append(random.choice(pool))
	return zalgo_string

def ruin(string, up, inside, down):
	split = list(string)
	for n in range(len(split)):
		temp = split[n]
		temp += ''.join(get_zalgo(ABOVE_POOL, up))
		temp += ''.join(get_zalgo(THROUGH_POOL, inside))
		temp += ''.join(get_zalgo(BELOW_POOL, down))
		split[n] = temp
	joined = ''.join(split)
	return joined

def clean(string):
	temp = ''
	for c in string:
		if 32 <= ord(c) <= 126:
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