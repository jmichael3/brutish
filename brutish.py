#!/usr/bin/env python3

import logging
import string
import argparse
import sys


def generate_nums(someword, startnum=0, endnum=2019):
    '''takes a word and an optional startnum and endnum ...returns a list of words with the numbers appended to the end ...default (startnum=0,endnum=2019)'''
    mangle_l = []
    for _ in range(startnum, endnum):
        mangle_l.append(someword + str(_))
    return mangle_l


def combine(w1, w2):
    '''takes word1 and word2 and returns a string of w1+w2'''
    return (str(w1) + str(w2))


def add_punctuation(someword, aggressive=False):
    '''takes someword and an opptional arg, aggressive which is set to False by default...returns a list of words with punctuation at the end'''
    if aggressive == False:
        return [someword + "!"]
    else:
        [someword + _ for _ in string.punctuation]


def read_f(dic):
    '''takes a textfile and just returns an f.read() '''
    with open(dic, "r") as f:
        return f.read()


if __name__ == "__main__":
    # initialize some schtuff

    wordlist = []
    DATA = ""
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename=".brutish_log",
                        level=logging.DEBUG, format=LOG_FORMAT, filemode="w")
    logger = logging.getLogger()
    print("[*]Logging at level {}".format(logger.level))
    logger.info("[*]Logging at level {}".format(logger.level))

    if len(sys.argv) != 2:
        print("[*]Usage : {} wordlist".format(sys.argv[0]))
        sys.exit()

    # dictionary is set to last positional arg
    logger.debug("dictionary is set to last positional arg")
    dictionary = sys.argv[-1]
    print("[*]Using dictionary : {}".format(dictionary))
    logger.info("dictionary = {} ".format(dictionary))

    # read dictionary and create wordlist
    logger.debug("read dictionary and create wordlist")
    w = read_f(dictionary)
    wordlist = w.split("\n")
    for _ in wordlist:
        if _ == "\n":
            wordlist.remove("\n")

    # generate_nums
    logger.debug("generate_nums")
    for _ in wordlist.copy():
        wordlist = wordlist + (generate_nums(_))

    # add_punctuation
    logger.debug("add_punctuation")
    for _ in wordlist.copy():
        wordlist = wordlist + add_punctuation(_)

    # convert wordlist to \n separated string
    logger.debug("convert wordlist to \\n separated string")
    DATA = "\n".join(wordlist)

    # write data to file
    logger.debug("write data to file")
    with open("brutish.dic", "a+") as f:
        f.write(DATA)
