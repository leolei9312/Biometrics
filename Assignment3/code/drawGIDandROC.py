# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 14:18:10 2017

@author: Meidi
"""
import matplotlib.pyplot as plt

genuine = {3: 3, 4: 59, 5: 102, 6: 82, 7: 74, 8: 49, 9: 50, 10: 65, 11: 54, 12: 61, 13: 60, 14: 55, 15: 36, 16: 38, 17: 23, 18: 20, 19: 13, 20: 9, 21: 5, 22: 3, 23: 4, 24: 1, 25: 2, 26: 1, 27: 3, 28: 4, 29: 2, 30: 1, 31: 1, 33: 2, 35: 3, 36: 1, 37: 2, 38: 2, 39: 2, 44: 2, 45: 2, 47: 2, 48: 1, 49: 4, 50: 2, 51: 1, 52: 1, 53: 1, 54: 2, 55: 1, 56: 1, 88: 1}
imposter = {10: 3, 11: 1, 12: 6, 13: 2, 14: 6, 15: 7, 16: 12, 17: 24, 18: 31, 19: 43, 20: 73, 21: 110, 22: 145, 23: 224, 24: 296, 25: 401, 26: 476, 27: 620, 28: 783, 29: 948, 30: 1132, 31: 1333, 32: 1493, 33: 1612, 34: 1844, 35: 2059, 36: 2257, 37: 2518, 38: 2570, 39: 3027, 40: 2925, 41: 3156, 42: 3268, 43: 3461, 44: 3458, 45: 3679, 46: 3834, 47: 4014, 48: 4079, 49: 4060, 50: 4264, 51: 4347, 52: 4306, 53: 4338, 54: 4345, 55: 4420, 56: 4458, 57: 4344, 58: 4348, 59: 4184, 60: 4233, 61: 4223, 62: 4062, 63: 3950, 64: 3781, 65: 3731, 66: 3554, 67: 3442, 68: 3364, 69: 3021, 70: 2841, 71: 2646, 72: 2486, 73: 2301, 74: 2083, 75: 1961, 76: 1622, 77: 1494, 78: 1209, 79: 1005, 80: 871, 81: 685, 82: 576, 83: 433, 84: 330, 85: 226, 86: 182, 87: 96, 88: 75, 89: 42, 90: 16, 91: 10, 92: 6}

# plot genuine and imposter distribution
gen = sorted(genuine.items())
x, y = zip(*gen)
imp = sorted(imposter.items())
w, z = zip(*imp)

plt.plot(x, y)
plt.plot(w, z)
plt.show()

#plot ROC curve
TMR = []
FMR = []

sum_gen = sum(y)
sum_imp = sum(z)

for threshold in range(101):
    true_match = 0
    false_match = 0
    for i in range(threshold + 1):
        if i in genuine.keys():
            true_match += genuine[i]
        if i in imposter.keys():
            false_match += imposter[i]
    print true_match/float(sum_gen), false_match/float(sum_imp)
    TMR.append(true_match/float(sum_gen))
    FMR.append(false_match/float(sum_imp))

plt.plot(FMR, TMR)