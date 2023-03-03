#Reference:https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
import sys

# input comes from STDIN (standard input)
for l in sys.stdin:
    # remove leading and trailing whitespace
    l = l.strip()
    # split the line into words
    words = l.split()
    # increase counters
    for word in words:

        print '%s\t%s' % (word, 1)