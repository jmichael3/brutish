#!/usr/bin/env python3

import logging
import string

def generate_dates_long(someword,startdate=1600,enddate=2019):
    mangle_l = []
    for _ in range(startdate,enddate):
        mangle_l.append(someword + str(_))
    return mangle_l

def generate_dates_short(someword):
    mangle = ""
    return mangle

def combine(w1,w2):
    return (w1 + w2)

def add_punctuation(someword):
    for _ in add_punctuation

def read_f(dic):
    with open(dic,"r") as f:
        return f.read()


if __name__=="__main__":
    # do the things
    
    usage = \
'''
    #######################################
    #           brutish.py                #
    #######################################

        Usage : ./{} [options] [wordlist]

-o, --output    ...specify filename to write mangled wordlist to
-c, --combine   ...call the combine func (combine all the words in your wordlist together)

'''.format(sys.argv[0])

    if len(sys.argv) < 2:
        print(usage)
        sys.exit()
    else:
        # wordlist is set to last positional arg
        wordlist = sys.argv[-1]

    # take a positional arg (wordlist)

    # if the wordlist is the only thing provided then do all the things

    # provide an option parser for each specific function

    # if someone provides x number of options then do all x

    # ignore any repeat arguments
