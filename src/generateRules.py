__author__ = "Tom Kocmi"

import Cons, Queue, gensim, numpy

kthneighbor = {}

def generate(prefixes, suffixes, model):
    rules = []
    for pre1, r in prefixes.iteritems():
        for pre2, support in r.iteritems():
            break
            rules.append(["prefix", pre1, pre2, computeHitRate(support, model)])
            #print ["prefix", pre1, pre2, computeHitRate(support, model)]
    for pre1, r in suffixes.iteritems():
        for pre2, support in r.iteritems():
            rules.append(["suffix", pre1, pre2, computeHitRate(support, model)])
            print ["suffix", pre1, pre2, computeHitRate(support, model)]

    return rules


def computeHitRate(support, model):
    hitrate=0
    sum = 0
    for pair1 in support:
        for pair2 in support:
            if pair1 != pair2:
                diff = numpy.subtract(model[pair2[1]], model[pair2[0]])
                cos = numpy.dot(gensim.matutils.unitvec(model[pair1[1]]), gensim.matutils.unitvec(numpy.add(model[pair1[0]],diff)))

                if pair1[1] not in kthneighbor:
                    kthneighbor[pair1[1]] = getKthClosestNeighbor(pair1[1], model, Cons.HITTHRESHOLD)
                if cos>kthneighbor[pair1[1]]:
                    hitrate+=1
                sum+=1

    return hitrate/sum



def getKthClosestNeighbor(word, model, K):
    pq = Queue.PriorityQueue(K)
    for w2 in model.vocab.keys():
        if word == w2:
            continue;
        if pq.qsize() < K:
            pq.put(-model.similarity(word, w2))
        else:
            sim = -model.similarity(word, w2)
            if pq.queue[0] > sim:
                pq.get()
                pq.put(sim)
    return -pq.queue[0]
