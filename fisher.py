#!/usr/bin/env python3
import numpy as np

# Open file return class0, class1
def open_file(data, header = True):
    data0 = {}
    data1 = {}

    file = open(data)
    for line in file:
        if header == True:
            header = False
            continue
        result = line.split()
        if int(result[2]) == 0:
            data0[(float(result[0]), float(result[1]))] = int(result[2])
        else:
            data1[(float(result[0]), float(result[1]))] = int(result[2])

    return data0, data1

# Return mean of each vector
def avg_vector(data):
    sum = np.mat([0.0, 0.0])
    cnt = 0

    for key in data:
        sum += np.mat(key)
        cnt += 1

    avg = sum / cnt
    return avg.transpose()

# Return within-class scatter
def within_class_scatter(data, avg):
    sum = np.zeros((2, 2))
    for coord in data:
        coord = np.mat(coord).transpose()
        sum += (coord - avg) * (coord - avg).transpose()
    return sum

# Get direction of w-vector
def direct_vector(wcs, avg0, avg1):
    # print(wcs)
    print(wcs ** (-1))
    print(wcs / 3 ** (-1))
    print(np.linalg.inv(wcs))
    # print(wcs ** (-1) * (avg0 - avg1))
    return np.linalg.inv(wcs) * (avg0 - avg1)

# Get threshold 
def threshold(direct, avg0, avg1, data0, data1, sw0 = None, sw1 = None):
    cnt0 = len(data0)
    cnt1 = len(data1)
    # return direct.transpose() * (cnt0 * avg0 + cnt1 * avg1) / (cnt0 + cnt1)
    # return direct.transpose() * (cnt1 * avg0 + cnt0 * avg1) / (cnt0 + cnt1)
    # return 0.5 * direct.transpose() * ((cnt1 * avg0 + cnt0 * avg1) / (cnt0 + cnt1) + (sw0 * avg0 + sw1 * avg1) / (sw0 + sw1))
    return direct.transpose() * (avg0 + avg1) / 2

def train(file):
    (data0, data1) = open_file(file)
    avg0, avg1 = avg_vector(data0), avg_vector(data1)
    wcs0 = within_class_scatter(data0, avg0)
    print('s0')
    print(wcs0)
    wcs1 = within_class_scatter(data1, avg1)
    print('s1')
    print(wcs1)
    wcs = wcs0 + wcs1
    print('sw')
    print(wcs)
    direct = direct_vector(wcs, avg0, avg1)
    # sw0 = sw(direct, wcs0)[0, 0]
    # sw1 = sw(direct, wcs1)[0, 0]
    # theta = threshold(direct, avg0, avg1, data0, data1, sw0, sw1)
    theta = threshold(direct, avg0, avg1, data0, data1)
    return direct, theta

def test(file, direct, theta):
    (data0, data1) = open_file(file)
    num = len(data0) + len(data1)
    hit = 0
    classification = 0

    for data in data0:
        if np.mat(data) * direct > theta:
            classification = 0
        else:
            classification = 1
        if classification == data0[data]:
            hit += 1

    for data in data1:
        if np.mat(data) * direct > theta:
            classification = 0
        else:
            classification = 1
        if classification == data1[data]:
            hit += 1
    return hit / num

def sw(direct, wcs):
    return direct.transpose() * wcs * direct

if __name__ == '__main__':
    # (direct, theta) = train('synth.tr')
    (direct, theta) = train('train')
    # print(direct)
    # print(theta)
    # presicion = test('synth.te', direct, theta)
    presicion = test('train', direct, theta)
    print(presicion)
