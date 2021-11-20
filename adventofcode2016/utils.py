import fileinput

def readLines():
    return [line.strip() for line in fileinput.input()]