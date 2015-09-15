#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "Tom Kocmi"

import logging
import VectorModel
import Cons, Fixes, GenerateRules
import time
import pickle
import Queue

start = time.time()  # for counting the time
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

model = VectorModel.getVectorModel()

# vocabulary = Fixes.downsampleVocabulary(model, Cons.MAXWORDS4AFFIXES)
# with open("models/vocabulary2.data", 'w') as f:
#     pickle.dump(vocabulary, f)
# with open("models/vocabulary.data", 'r') as f:
#      vocabulary = pickle.load(f)


prefixes, suffixes = Fixes.generateFixes(vocabulary)



# rules = GenerateRules.generate(prefixes, suffixes, model, vocabulary)
# with open("models/rules6.data", 'w') as f:
#     pickle.dump(rules, f)


#print model.doesnt_match("winston julia brother goldstein".split())
#print model.most_similar(positive=['most'])
# with open("models/rules.data", 'r') as f:
#     rules = pickle.load(f)
# print rules


logging.info("Time: " + str(time.time() - start)+" s")

