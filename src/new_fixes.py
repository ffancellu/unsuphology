__author__ = 'Fortress'

import codecs
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


def generateNewFixes(vocabulary,output=["pickle","write_file","return"]):
    prefixes = {}
    suffixes = {}
    reduplications = {}
    infixes = {}

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
                addRule = True
                f = 0
                for fix in range(1, len(w1) + 1):
                    if w1[len(w1) - fix] != w2[len(w2) - fix]:
                        if fix == 1:
                            addRule = False
                        break
                    f+=1

                if addRule:
                    if f==len(w1):
                        pre1 = ""
                        pre2 = w2[:-f]
                    else:
                        pre1 = w1[:-f]
                        pre2 = w2[:-f]


                    if len(pre2) <= Cons.MAXFIX:
                        if (len(pre1) == len(pre2)) and pre1 > pre2:
                            tmp = pre1
                            pre1 = pre2
                            pre2 = tmp
                            tmp = w1
                            w1 = w2
                            w2 = tmp

                        if pre1 not in prefixes:
                            prefixes[pre1] = {}
                        if pre2 not in prefixes[pre1]:
                            prefixes[pre1][pre2] = [[w1, w2]]
                        else:
                            prefixes[pre1][pre2].append([w1, w2])

                # extract suffixes
                addRule = True
                f=0
                for fix in range(0, len(w1)):
                    if w1[fix] != w2[fix]:
                        if fix == 0:
                            addRule = False
                        break
                    f+=1
                if addRule:
                    if f==len(w1):
                        pre1 = ""
                        pre2 = w2[f:]
                    else:
                        pre1 = w1[f:]
                        pre2 = w2[f:]
                    if len(pre2) <= Cons.MAXFIX:
                        if (len(pre1) == len(pre2)) and pre1 > pre2:
                            tmp = pre1
                            pre1 = pre2
                            pre2 = tmp
                            tmp = w1
                            w1 = w2
                            w2 = tmp

                        if pre1 not in suffixes:
                            suffixes[pre1] = {}
                        if pre2 not in suffixes[pre1]:
                            suffixes[pre1][pre2] = [[w1, w2]]
                        else:
                            suffixes[pre1][pre2].append([w1, w2])

                # extract reduplication pattern
                # w1,w2
                if w1 in w2:



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

    if "pickle" in output:
        pickle_results(prefixes,suffixes)
    elif "write_file" in output:
        print_rules_to_file(prefixes,suffixes)
    elif "return" in output:
        return prefixes,affixes

def pickle_results(prefixes,suffixes):
    print "Pickling results!"
    with open(Cons.FIXESFILENAME, 'w') as f:
        pickle.dump([prefixes, suffixes], f)

def print_rules_to_file(prefixes,suffixes):
    with open(Cons.RULESFILENAME,'w') as f:
        # print suffixes
        for t in [prefixes,suffixes]:
            sorted_keys = sorted(t.keys())
            for k in sorted_keys:
                sorted_nested_keys = sorted(t[k].keys())
                for kn in sorted_nested_keys:
                    w = "prefixes" if t==prefixes else "suffixes"
                    f.write("%s:%s:%s %d\n" % (w,k,kn,len(t[k][kn])))
                    for item in t[k][kn]:
                        f.write("\t%s-%s\n" % (item[0],item[1]))
                    f.write("\n")


def downsample(supportset):
    if len(supportset) < Cons.MAXSUPPORTSIZE:
        return supportset
    return random.sample(supportset, Cons.MAXSUPPORTSIZE)

def gets_vocabulary(filepath):
    f = codecs.open(filepath,'rb','utf8')
    vocabulary = []
    i = 0
    for line in f:
        print "Considering line %d", i
        if len(vocabulary)>60000:
            break
        else:
            words = line.strip().split()
            vocabulary.extend(words)
        i+=1
    return list(set(vocabulary))

def wrapper(filepath):
    print "Fetch vocabulary..."
    voc = gets_vocabulary(filepath)
    print "Vocabulary fecthed!"
    print "vocabulary length: ",len(voc)
    print "Dealing with suffixes..."
    generateFixes(voc)
    print "Dealt with suffixes!"

if __name__=="__main__":
    wrapper(Cons.DATAFILENAME)

