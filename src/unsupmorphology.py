#!/usr/bin/env python
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


prefixes, suffixes = Fixes.generateFixes(vocabulary)

rules = GenerateRules.generate(prefixes, suffixes, model)
print rules




