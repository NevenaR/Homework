# Just some helper functions used in the homework

def getAbr(name):
    try:
        return name.split(" - ")
    except IndexError:
        return numpy.array[""]

def convertToNum(x):
    try:
        return float(x)
    except ValueError:
        return 0
