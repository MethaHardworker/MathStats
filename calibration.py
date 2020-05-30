

#finding the temperature
#INPUT: table - calibration table
#       arr - values
#OUTPUT:    temperature
def getTemperature(table, arr):
    num = [i for i in range(len(arr))]
    ptr = sorted(zip(arr, num))
    num = [x for _, x in ptr]
    marr = arr.copy()
    marr.sort()

    res = []

    j = 0
    i = 0
    while i < len(marr):
        while j < len(table[0]):
            if table[0][j] >= marr[i]:
                break
            j += 1

        if j == len(table[0]):
            j -= 1
            break

        res.append(table[1][j])
        i += 1

    while i < len(marr):
        res.append(table[1][j])
        i += 1

    ptr = sorted(zip(num, res))
    res = [x for _, x in ptr]
    return res


#creating a calibration table
#INPUT: filename - a file with the calibration
#OUTPUT:    calibration table
def getCalibration(filename):
    table = [ [], [] ]
    f = open(filename)
    while True:
        str = f.readline().split()

        if not str: break

        if len(table[0]) > 0 and float(str[0]) == table[0][len(table[0]) - 1]:
            continue

        table[0].append(float(str[0]))
        table[1].append(float(str[1]))
    return table

if __name__ == "__main__":
    table= [ ]
    filename = "R80-50.txt"
    f = open(filename)
    while True:
        str = f.readline().split()
        if not str: break
        table.append( [float(str[0]) , float(str[1])] )
    print(table)