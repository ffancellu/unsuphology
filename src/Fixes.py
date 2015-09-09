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
            print "creating _fixes, progress: " + str(i) + "/" + str(len(vocabulary))
        for j in range(0, len(vocabulary)):
            if i < j:
                if len(vocabulary[i]) < len(vocabulary[j]):
                    w1 = vocabulary[i]
                    w2 = vocabulary[j]
                else:
                    w1 = vocabulary[j]
                    w2 = vocabulary[i]
                # extract prefixes
                for fix in range(len(w1) + 1, max(1, len(w1) - Cons.MAXFIX), -1):
                    if w1[-fix:] == w2[-fix:]:
                        if len(w2[:-fix]) <= Cons.MAXFIX:
                            if (len(w1[:-fix]) == len(w2[:-fix])) and w1[:-fix] > w2[:-fix]:
                                pre1 = w2[:-fix]
                                pre2 = w1[:-fix]
                            else:
                                pre1 = w1[:-fix]
                                pre2 = w2[:-fix]

                            if pre1 not in prefixes:
                                prefixes[pre1] = {}
                            if pre2 not in prefixes[pre1]:
                                # prefixes[pre1][pre2] = 1
                                prefixes[pre1][pre2] = [[w1, w2]]
                            else:
                                # prefixes[pre1][pre2] += 1
                                prefixes[pre1][pre2].append([w1, w2])
                        break

                # extract suffixes
                for fix in range(len(w1) + 1, max(1, len(w1) - Cons.MAXFIX), -1):
                    if w1[:fix] == w2[:fix]:
                        if len(w2[fix:]) <= Cons.MAXFIX:
                            if (len(w1[fix:]) == len(w2[fix:])) and w1[fix:] > w2[fix:]:
                                pre1 = w2[fix:]
                                pre2 = w1[fix:]
                            else:
                                pre1 = w1[fix:]
                                pre2 = w2[fix:]

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
    if len(supportset)<Cons.MAXSUPPORTSIZE:
        return supportset
    return random.sample(supportset, Cons.MAXSUPPORTSIZE)