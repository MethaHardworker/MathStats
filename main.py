import pyglobus
import numpy as np
import matplotlib.pyplot as plt
import calibration
import os
import sys
import scipy.stats as sc

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

SHT_PATH = "sht/"
CALIBR_PATH = "calibr/"
RES_PATH = "results/"
NUM_SIGNAL_FROM_SHT = {
    80: b'SXR 80 mkm\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    50: b'SXR 50 mkm\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    27: b'SXR 27 \xec\xea\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    15: b'SXR 15 \xec\xea\xec\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

}
SIGNAL_SAMPLING_RATE = int(1e6)
LOW_PASS_CUTOFF = 5000
LEFT = 0.12
RIGHT = 0.23


# plotting
def plot(x, y, label_x, label_y, label, new_fig=True):
    if new_fig:
        plt.figure(figsize=(15, 10))

    plt.plot(x, y, label=label)
    plt.xlabel(label_x, fontsize=14)
    plt.ylabel(label_y, fontsize=14)


# the alignment of the intervals
# INPUT: signal1 - first signal
#       signal2 - second signal
# OUTPUT:    result vectors
def makeInterval(signal1, signal2):
    l = max(min(signal1[0]), min(signal2[0]))
    r = min(max(signal1[0]), max(signal2[0]))

    res1 = [[], []]
    for i in range(len(signal1[0])):
        if l <= signal1[0][i] <= r:
            res1[0].append(signal1[0][i])
            res1[1].append(signal1[1][i])

    res2 = [[], []]
    for i in range(len(signal2[0])):
        if l <= signal2[0][i] <= r:
            res2[0].append(signal2[0][i])
            res2[1].append(signal2[1][i])

    return res1, res2


# setting borders
# INPUT: signal - signal
#       left - left border
#       right - right border
# OUTPUT:    result vectors
def setBorders(signal, left, right):
    x = []
    y = []
    for i in range(len(signal[0])):
        if signal[0][i] >= left and signal[0][i] <= right:
            x.append(signal[0][i])
            y.append(signal[1][i])

    return x, y


# division of vectors
# INPUT: op1 - first operand
#       op2 - second operand
# OUTPUT:    result vector
def div(op1, op2):
    res = []
    for i in range(len(op1)):
        res.append(op1[i] / op2[i])
    return res


# getting results using two signals
# INPUT: signal1 - first signal
#       signal2 - second signal
#       table - table created from the calibration file
# OUTPUT:    result vectors
def process(signal1, signal2, table):
    sign1 = signal1.copy()
    sign2 = signal2.copy()

    sign1, sign2 = makeInterval(sign1, sign2)

    r_val, p_v = sc.spearmanr(sign1[1], sign2[1])

    result = div(sign1[1], sign2[1])

    result = calibration.getTemperature(table, result)

    return sign1[0], result, r_val


# getting a signal
# INPUT: nums - sxr numbers
#       sht_reader - generated shtReader
#       RIO - region of interest
#       borders - manual border adjustment
#       left - left border
#       right - right border
# OUTPUT:    list of signals
def makeSignals(nums, shtReader, ROI=True, borders=False, left=LEFT, right=RIGHT):
    signals = []
    for i in range(len(nums)):
        signal = shtReader.get_signals(NUM_SIGNAL_FROM_SHT[nums[i]])

        data = np.array((signal[0].get_data_x(), signal[0].get_data_y()))

        if ROI:
            roi = pyglobus.sawtooth.get_signal_roi(data[1], mean_scale=1)
            x = np.copy(data[0][roi[0]:roi[1]])
            y = np.copy(data[1][roi[0]:roi[1]])
            data = np.array((x, y))

        if borders:
            x, y = setBorders(data, left, right)
            data = np.array((x, y))

        pyglobus.dsp.low_pass_filter(data[1], LOW_PASS_CUTOFF, SIGNAL_SAMPLING_RATE)

        signals.append(data)

    return signals


# getting results from sht file
# INPUT: shtNum - sht file number
#       nums - sxr numbers
#       RIO - region of interest
#       borders - manual border adjustment
#       left - left border
#       right - right border
#       graphics - output of graphs
def mainProcess(shtNum, nums, ROI=True, borders=False, left=LEFT, right=RIGHT, graphics=False):
    nums.sort(reverse=True)

    shtReader = pyglobus.util.ShtReader(SHT_PATH + "sht" + str(shtNum) + ".sht")

    signals = makeSignals(nums, shtReader, ROI=ROI, borders=borders, left=left, right=right)

    printShtCorrelationFile("SHT" + str(shtNum))

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            filename = 'R' + str(nums[i]) + '-' + str(nums[j]) + '.txt'

            table = calibration.getCalibration(CALIBR_PATH + filename)

            x, y, r = process(signals[i], signals[j], table)

            if graphics:
                plot(x, y, "Time (ms)", "T (eV)", "R" + str(nums[i]) + "-" + str(nums[j]), new_fig=False, )

            # outputResults("Temperature" + "_" + "SHT" + str(shtNum) + "_" + str(nums[i]) + "-" + str(nums[j]) + ".txt",
            #              x, y)

            outputCorrelations(nums[i], nums[j], r)

    if graphics:
        plt.title("SHT" + str(shtNum))
        plt.legend()
        plt.show()


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def openCorrelationFile():
    f = open(RES_PATH + "Correlation.txt", 'w')
    f.write('')
    f.close()


def printShtCorrelationFile(fileSht):
    f = open(RES_PATH + "Correlation.txt", 'a')
    f.write(fileSht + '\n')
    f.close()


def outputCorrelations(size1, size2, corr):
    f = open(RES_PATH + "Correlation.txt", 'a')
    f.write('r-' + str(size1) + '_' + str(size2) + '   ' + str(corr) + '\n')
    f.close()


# output results to a file
# First column - time (ms)
# Second column - temperature (eV)
def outputResults(filename, column1, column2):
    f = open(RES_PATH + filename, 'w')
    for i in range(len(column1)):
        f.write(str(toFixed(column1[i], 7)) + "\t" + str(toFixed(column2[i], 1)) + "\n")
    f.close()


if __name__ == "__main__":
    openCorrelationFile()
    SHT_NUMBERS = [38515, 38516, 38916, 38851, 38852, 38853]
    SHT_FIRST_NUMBER = 38851
    SHT_NUMBER = 38916
    NUM_SXR = [80, 50, 15]
    NUM_SXR_COR = [80, 50, 27, 15]
    # for number in range(38851, 38865):
    #     mainProcess(number, NUM_SXR_COR, graphics=True, borders=False, ROI=True)
    # for number in range(38866, 38891):
    #     mainProcess(number, NUM_SXR_COR, graphics=True, borders=False, ROI=True)
    # for number in range(38901, 38908):
    #     mainProcess(number, NUM_SXR_COR, graphics=True, borders=False, ROI=True)
    # for number in range(38909, 38944):
    #     mainProcess(number, NUM_SXR_COR, graphics=True, borders=False, ROI=True)
    # for number in range(38988, 38997):
    #     mainProcess(number, NUM_SXR_COR, graphics=True, borders=False, ROI=True)
    # for number in range(38998, 39060):
    #     mainProcess(number, NUM_SXR_COR, graphics=True, borders=False, ROI=True)
    # for number in range(39061, 39064):
    mainProcess(38880, NUM_SXR_COR, graphics=True, borders=False, ROI=True)

