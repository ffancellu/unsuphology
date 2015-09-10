__author__ = 'Fortress'

import Cons
import pickle
import os
import random


def generateFixes(vocabulary, generateNew=False):
    if os.path.isfile(Cons.FIXESFILENAME) and not generateNew:
        with open(Cons.FIXESFILENAME, 'r') as f:
            fixes = pickle.load(f)
            return fixes[0], fixes[1]
    else:
        return generateNewFixes(vocabulary)


def generateNewFixes(vocabulary):
    prefixes = {}
    suffixes = {}

    for i in range(0, len(vocabulary)):
        if i % 100 == 0:
            print "creating _prefixes and suffixes, progress: " + str(i) + " out of " + str(len(vocabulary))
        for j in range(0, len(vocabulary)):
            if i < j:
                if len(vocabulary[i]) < len(vocabulary[j]):
                    w1 = vocabulary[i]
                    w2 = vocabulary[j]
                else:
                    w1 = vocabulary[j]
                    w2 = vocabulary[i]
                # extract prefixes
                for fix in range(1, len(w1) + 1):
                    if w1[len(w1) - fix] != w2[len(w2) - fix]:
                        if fix == 1:
                            break

                        pre1 = w1[:-fix + 1]
                        pre2 = w2[:-fix + 1]
                        if len(pre2) <= Cons.MAXFIX:
                            if (len(pre1) == len(pre2)) and pre1 > pre2:
                                tmp = pre1
                                pre1 = pre2
                                pre2 = tmp
                                tmp = w1
                                w1=w2
                                w2=tmp

                            if pre1 not in prefixes:
                                prefixes[pre1] = {}
                            if pre2 not in prefixes[pre1]:
                                prefixes[pre1][pre2] = [[w1, w2]]
                            else:
                                prefixes[pre1][pre2].append([w1, w2])
                        break

                # extract suffixes
                for fix in range(0, len(w1)):
                    if w1[fix] != w2[fix]:
                        if fix == 0:
                            break

                        pre1 = w1[fix:]
                        pre2 = w2[fix:]
                        if len(pre2) <= Cons.MAXFIX:
                            if (len(pre1) == len(pre2)) and pre1 > pre2:
                                tmp = pre1
                                pre1 = pre2
                                pre2 = tmp
                                tmp = w1
                                w1=w2
                                w2=tmp

                            if pre1 not in suffixes:
                                suffixes[pre1] = {}
                            if pre2 not in suffixes[pre1]:
                                suffixes[pre1][pre2] = [[w1, w2]]
                            else:
                                suffixes[pre1][pre2].append([w1, w2])
                        break

    # remove rare prefix rules
    prefixes2 = {}
    for pre1, r in prefixes.iteritems():
        for pre2, support in r.iteritems():
            # print pre1 + " "+pre2+": "+str(len(support))
            if len(support) >= Cons.RARERULES:
                if pre1 not in prefixes2:
                    prefixes2[pre1] = {}
                prefixes2[pre1][pre2] = downsample(support)

    prefixes = prefixes2

    # remove rare suffix rules
    suffixes2 = {}
    for pre1, r in suffixes.iteritems():
        for pre2, support in r.iteritems():
            # print pre1 + " "+pre2+": "+str(len(support))
            if len(support) >= Cons.RARERULES:
                if pre1 not in suffixes2:
                    suffixes2[pre1] = {}
                suffixes2[pre1][pre2] = downsample(support)

    suffixes = suffixes2

    # save in to the file
    with open(Cons.FIXESFILENAME, 'w') as f:
        pickle.dump([prefixes, suffixes], f)

    return prefixes, suffixes


def downsample(supportset):
    if len(supportset) < Cons.MAXSUPPORTSIZE:
        return supportset
    return random.sample(supportset, Cons.MAXSUPPORTSIZE)
