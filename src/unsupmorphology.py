__author__ = "Tom Kocmi"

# if __name__ == "__main__":

import logging
import VectorModel
import Cons, Fixes
import time
import random

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

model = VectorModel.getVectorModel()
vocabulary={}
vocabulary = model.vocab.keys()

start = time.time()

prefixes, suffixes = Fixes.generateFixes(vocabulary, True)


print "Time: "+str(time.time()-start)

print len(prefixes)
print len(suffixes)





#print model.most_similar(positive=['winston', 'love'], negative=['war'])
#print model.doesnt_match("winston julia brother goldstein".split())
#print model.similarity("winston", "julia")
