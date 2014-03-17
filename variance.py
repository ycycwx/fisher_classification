#!/usr/bin/env python3

import math

def variance(list):
	avg = sum(list) / len(list)
	tmp = [ pow((i - avg), 2) for i in list ]
	return (sum(tmp)) / len(list)

if __name__ == "__main__":
	data = [1,2,3,4,5]
	print(variance(data))
