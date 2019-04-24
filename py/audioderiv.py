import pygame
import numpy as np
import scipy.io.wavfile

infile = 'test.wav'
outfile = 'test_derivert.wav'
rate, data = scipy.io.wavfile.read(infile)

def deriver(data):
    samples = len(data)
    derivert_array = np.zeros(samples - 1)
    i = 0
    while i < samples - 1:
        derivert_array[i] = data[i+1][0] - data[i][0]
        i += 1
    return derivert_array

def cast(data, cast_type=np.int16):
    return data.astype(np.int16)

print('Starting...')
scipy.io.wavfile.write(outfile, rate, cast(deriver(data)))
print('Finished...')
