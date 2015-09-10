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

prefixes, suffixes = Fixes.generateFixes(vocabulary)


rules = GenerateRules.generate(prefixes, suffixes, model)
print rules


print "Time: " + str(time.time() - start)


