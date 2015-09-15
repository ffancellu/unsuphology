__author__ = "Tom Kocmi"

import Cons, Queue, gensim, numpy, logging

kthneighbor = {}


def generate(prefixes, suffixes, model, vocabulary):
    rules = []
    print "evaluating prefixes"
    i = 0
    for pre1, r in prefixes.iteritems():
        for pre2, support in r.iteritems():
            if len(support) < 100:
                continue
            # if pre1!="" or pre2!="un": continue
            rules.append(["prefix", pre1, pre2, computeHitRate(support, model, vocabulary)])
            logging.info(rules[-1])
        i += 1
    print "prefixes evaluated"
    i = 0
    for pre1, r in suffixes.iteritems():
        for pre2, support in r.iteritems():
            if len(support) < 100:
                continue
            rules.append(["suffix", pre1, pre2, computeHitRate(support, model, vocabulary)])
            logging.info(rules[-1])
        i += 1

    return rules


def computeHitRate(support, model, vocabulary):
    hitrate = 0
    sum = 0
    for pair1 in support:
        for pair2 in support:
            if pair1 != pair2:
                diff = numpy.subtract(model[pair2[1]], model[pair2[0]])
                cos = numpy.dot(gensim.matutils.unitvec(model[pair1[1]]),
                                gensim.matutils.unitvec(numpy.add(model[pair1[0]], diff)))

                if pair1[1] not in kthneighbor:
                    kthneighbor[pair1[1]] = getKthClosestNeighbor(pair1[1], model, Cons.HITTHRESHOLD, vocabulary)
                if cos > kthneighbor[pair1[1]]:
                    hitrate += 1
                # print str(pair1) + " " + str(pair2) + str(cos) + " " + str(kthneighbor[pair1[1]])
                sum += 1

    return hitrate / sum


def getKthClosestNeighbor(word, model, K, vocabulary):
    pq = Queue.PriorityQueue(K)
    for w2 in vocabulary:  # model.vocab.keys()
        if word == w2:
            continue;
        sim = -numpy.dot(gensim.matutils.unitvec(model[word]), gensim.matutils.unitvec(model[w2]))
        if pq.qsize() < K:
            pq.put(sim)
        else:
            if pq.queue[0] > sim:
                pq.get()
                pq.put(sim)
    return -pq.queue[0]
