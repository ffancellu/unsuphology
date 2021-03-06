#!/usr/bin/env python
__author__ = "Tom Kocmi"

import logging
import VectorModel
import Cons
import generateRules
import new_fixes
import time

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
start = time.time()  # for counting the time

model = VectorModel.getVectorModel()  # this will load existing model
# in case if you want to generate new model, put True in the bracket
prefixes, suffixes = new_fixes.generateFixes(model.vocab.keys())
rules = GenerateRules.generate(prefixes, suffixes, model)
print rules
# generate prefixes and suffixes from the vocabulary of the model
# if the _fixes already exist it will load them from file instead of generating new ones.
# In case that you want to forse it to generate, put True as a second parameter

# experiments with the model, the words must be in the dictionary
# print model.most_similar(positive=['winston', 'love'], negative=['war'])
# print model.doesnt_match("winston julia brother goldstein".split())
# print model.similarity("winston", "julia")

print "Time: " + str(time.time() - start)
