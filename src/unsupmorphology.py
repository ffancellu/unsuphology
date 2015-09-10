__author__ = "Tom Kocmi"

import logging
import VectorModel
import Cons, Fixes, GenerateRules
import time
import Queue

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

model = VectorModel.getVectorModel()
vocabulary = {}
vocabulary = model.vocab.keys()

start = time.time()

# prefixes, suffixes = Fixes.generateFixes(vocabulary,True)


<<<<<<< HEAD
rules = GenerateRules.generate(prefixes, suffixes, model)
print rules


print "Time: " + str(time.time() - start)


=======
# print "Time: "+str(time.time()-start)

# print len(prefixes)
# print len(suffixes)


# print model.most_similar(positive=['winston', 'love'], negative=['war'])
# print model.doesnt_match("winston julia brother goldstein".split())
print model.similarity("migukgwa","irakeuyi")
print model.similarity("migukgwa","hanguk")
print model.similarity("migukgwa","hwarbarhan")
print model.similarity("migukgwa","jasinyi")
>>>>>>> 36a68cb1b982489e6fcb1a46f507072a4e661e2a
