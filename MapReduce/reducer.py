#Reference:https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

present_word = None
present_count = 0
word = None

# input comes from STDIN
for l in sys.stdin:
    # remove leading and trailing whitespace
    l = l.strip()

    # parse the input we got from mapper.py
    word, count = l.split('\t', 1)


    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue


    if present_word == word:
        present_count += count
    else:
        if present_word:
            # write result to STDOUT
            print '%s\t%s' % (present_word, present_count)
        present_count = count
        present_word = word
if present_word == word:
    print '%s\t%s' % (present_word, present_count)