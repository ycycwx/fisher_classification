#!/usr/bin/env python3

import numpy as np

def open_file(data, header = True):
	dataset = {}

	file = open(data)
	for line in file:
		if header == True:
			header = False
			continue
		result = line.split()
		dataset[(result[0], result[1])] = result[2]
	return dataset

if __name__ == '__main__':
	train = open_file('synth.tr')
	# print(train)
