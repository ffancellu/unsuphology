#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "Tom Kocmi"

import logging
import VectorModel
import Cons, Fixes, GenerateRules
import time
import Queue


# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)

model = VectorModel.getVectorModel()
vocabulary = model.vocab.keys()


# prefixes, suffixes = Fixes.generateFixes(vocabulary)
# rules = GenerateRules.generate(prefixes, suffixes, model)
# print rules


# print model.doesnt_match("winston julia brother goldstein".split())
# print model.most_similar(positive=['most'])
