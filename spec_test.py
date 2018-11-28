# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:19:53 2018

@author: aq
"""
import matplotlib.pyplot as plt
#https://github.com/ap--/python-seabreeze
import seabreeze.spectrometers as sb
import time
import numpy as np
devices = sb.list_devices()
print(devices)
spec = sb.Spectrometer(devices[0])
#время накопления
spec.integration_time_micros(0.5e6)
wavelengths = spec.wavelengths()

list_of_intensities = []
#измерение времени между последовательными накоплениями спектра
#минимум - 5 мс 
n = 20
start = time.time()
for i in range(n):
	list_of_intensities.append(spec.intensities(correct_dark_counts = True))
dt = (time.time() - start)/n
print(dt)

mean_int = sum(list_of_intensities)/len(list_of_intensities)
err = np.zeros(mean_int.shape)

f = open('zero_count.txt', 'r')
s = f.readline()
f.close()
zero_count = np.array([float(x) for x in s.split()])

for i in range(n):
	err += (mean_int - list_of_intensities[i])**2
	err /= n
	
for i in range(n):
	plt.plot(wavelengths, list_of_intensities[i])
	
plt.plot(wavelengths, err)

spec.close()

