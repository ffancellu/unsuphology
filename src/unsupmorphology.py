__author__ = "Tom Kocmi"

# if __name__ == "__main__":

import logging
import VectorModel
import Cons, Fixes
import time

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

model = VectorModel.getVectorModel()
vocabulary = model.vocab.keys()


start = time.time()

prefixes, suffixes = Fixes.generateFixes(vocabulary)

print len(prefixes)
print len(suffixes)
print "Time: "+str(time.time()-start)


# prefixes = []
# suffixes = []
# for word in vocabulary:
#    for x in range (1, Cons.MAXFIX):
#        if len(word[x:]) > 0:
#            prefixes.append(word[:x])
#        if len(word[:-x]) > 0:
#            suffixes.append(word[x:])




print model.most_similar(positive=['winston', 'love'], negative=['war'])
print model.doesnt_match("winston julia brother goldstein".split())
print model.similarity("winston", "julia")
