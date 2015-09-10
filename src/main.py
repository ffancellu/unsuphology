__author__ = "Tom Kocmi"

import logging
import VectorModel
import Cons, Fixes, GenerateRules
import time

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
start = time.time()  # for counting the time

model = VectorModel.getVectorModel()  # this will load existing model
# in case if you want to generate new model, put True in the bracket



# generate prefixes and suffixes from the vocabulary of the model
# if the _fixes already exist it will load them from file instead of generating new ones.
# In case that you want to forse it to generate, put True as a second parameter

# prefixes, suffixes = Fixes.generateFixes(model.vocab.keys())




# experiments with the model, the words must be in the dictionary
print model.most_similar(positive=['winston', 'love'], negative=['war'])
print model.doesnt_match("winston julia brother goldstein".split())
print model.similarity("winston", "julia")

print "Time: " + str(time.time() - start)
