# Import the required libraries
from math import ceil
from essential_generators import DocumentGenerator
from time import time

# Function to print the header
def head():
    for i in range(80):
        print('*', end='')
    print()
    print('Speed Typing Test'.center(80))
    for i in range(80):
        print('*', end='')
    print()


# Function to generate random paragraph
def genpara():
    para = DocumentGenerator()
    return para.paragraph()


# Function to calculate the time taken by user to type
def timetaken():
    print()
    print('Enter the above paragraph.', end = '\n')
    start = time()
    inp = input()
    end = time()
    return inp, ceil(end - start), len(inp)


# Function to calculate the errors made by the user
def validate(a, b):
    e = 0
    a = list(a.split())
    b = list(b.split())
    t = min(len(a), len(b))
    for i in range(t):
        if a[i] != b[i]:
            e += 1
    return e


# Function to calculate WPM and Accuracy
def calculatestats(t, l, errors):
    mins = t/60
    gwpm = (l // 5)
    nwpm = (gwpm - errors) // mins
    accuracy = (nwpm / (gwpm / mins)) * 100
    return nwpm, accuracy


# Function to print the result
def tail(nwpm, accuracy):
    print()
    for i in range(80):
        print('*', end='')
    print()
    txt1 = 'No.of words per minute (WPM): ' + str(nwpm)
    txt2 = 'Accuracy: ' + str(accuracy)
    print(txt1.center(80))
    print(txt2.center(80))
    for i in range(80):
        print('*', end='')
    print()


# Main
def main():
    head()
    print()
    para = genpara()[:300] + '.'
    print(para)
    inp, t, l = timetaken()
    while t < 60:
        print('Type the paragraph for at least a minute')
        inp, t, l = timetaken()

    errors = validate(para, inp)
    nwpm, accuracy = calculatestats(t, l, errors)
    tail(nwpm, accuracy)


# Calling main
if __name__ == '__main__':
    main()
