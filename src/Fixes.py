__author__ = 'Fortress'

import Cons
import pickle
import os


# def generateFixes(vocabulary):
#     if not os.path.isfile(Cons.FIXESFILENAME):
#         prefixes = []
#         suffixes = []
#
#         for i in range(0, len(vocabulary)):
#             if i % 100 == 0:
#                 print "progress: " + str(i) + "/" + str(len(vocabulary))
#             for j in range(0, len(vocabulary)):
#                 if i < j:
#                     if len(vocabulary[i]) < len(vocabulary[j]):
#                         w1 = vocabulary[i]
#                         w2 = vocabulary[j]
#                     else:
#                         w1 = vocabulary[j]
#                         w2 = vocabulary[i]
#                     # extract prefixes
#                     for fix in range(max(1, len(w1) - Cons.MAXFIX), len(w1) + 1):
#                         if w1[-fix:] == w2[-fix:]:
#                             if len(w2[:-fix]) <= Cons.MAXFIX:
#                                 prefixes.append(["pre", w1[:-fix], w2[:-fix]])
#                         else:
#                             break
#
#                     # extract suffixes
#                     for fix in range(max(1, len(w1) - Cons.MAXFIX), len(w1) + 1):
#                         if w1[:fix] == w2[:fix]:
#                             if len(w2[fix:]) <= Cons.MAXFIX:
#                                 suffixes.append(["suf", w1[fix:], w2[fix:]])
#                         else:
#                             break
#
#         with open(Cons.FIXESFILENAME, 'w') as f:
#             pickle.dump([prefixes, suffixes], f)
#     else:
#         with open(Cons.FIXESFILENAME, 'r') as f:
#             fixes = pickle.load(f)
#             prefixes = fixes[0]
#             suffixes = fixes[1]
#
#     return prefixes, suffixes


def generateFixes(vocabulary):
    if not os.path.isfile(Cons.FIXESFILENAME):
        prefixes = {}
        suffixes = {}

        for i in range(0, len(vocabulary)):
            if i % 100 == 0:
                print "progress: " + str(i) + "/" + str(len(vocabulary))
            for j in range(0, len(vocabulary)):
                if i < j:
                    if len(vocabulary[i]) < len(vocabulary[j]):
                        w1 = vocabulary[i]
                        w2 = vocabulary[j]
                    else:
                        w1 = vocabulary[j]
                        w2 = vocabulary[i]
                    # extract prefixes
                    for fix in range(len(w1) + 1,max(1, len(w1) - Cons.MAXFIX)):
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
                                    #prefixes[pre1][pre2] = 1
                                    prefixes[pre1][pre2] = [[w1, w2]]
                                else:
                                    #prefixes[pre1][pre2] += 1
                                    prefixes[pre1][pre2].append([w1, w2])
                                    print pre1+" "+pre2
                            break

                    # extract suffixes
                    for fix in range(max(1, len(w1) - Cons.MAXFIX), len(w1) + 1):
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
                                    suffixes[pre1][pre2].append([w1,w2])
                        else:
                            break


        with open(Cons.FIXESFILENAME, 'w') as f:
            pickle.dump([prefixes, suffixes], f)
    else:
        with open(Cons.FIXESFILENAME, 'r') as f:
            fixes = pickle.load(f)
            prefixes = fixes[0]
            suffixes = fixes[1]

    return prefixes, suffixes
