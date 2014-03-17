#!/usr/bin/env python3

import variance as var
import numpy as np

file = open('tests')
l = []
for line in file:
	l.append(float(line.strip()))

var = var.variance(l)
print(var)
print(np.mean(np.mat(l)) / len(l))
