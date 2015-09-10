__author__ = "Tom Kocmi"

import Cons, Queue

kthneighbor = {}

def generate(prefixes, suffixes, model):
    rules = []
    for pre1, r in prefixes.iteritems():
        for pre2, support in r.iteritems():
            rules.append(["prefix", pre1, pre2, computeHitRate(support, model)])
    for pre1, r in suffixes.iteritems():
        for pre2, support in r.iteritems():
            rules.append(["suffix", pre1, pre2, computeHitRate(support, model)])

    return rules


def computeHitRate(support, model):
    for pair1 in support:
        for pair2 in support:
            if pair1!=pair2:
                print pair1+pair2
                print model[pair1[0]]
                #print dot(matutils.unitvec(self[w1]), matutils.unitvec(self[w2]))
                #cos = model.similarity(pair[1])



    for word in model.vocab.keys():
        kthneighbor[word] = getKthClosestNeighbor(word, model, Cons.HITTHRESHOLD)


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