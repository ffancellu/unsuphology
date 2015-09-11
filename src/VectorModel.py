__author__ = "Tom Kocmi"

import os.path
import re
import gensim
import Cons


def getVectorModel(generateNew=False):
    if os.path.isfile(Cons.MODELFILENAME) and not generateNew:
        return gensim.models.Word2Vec.load(Cons.MODELFILENAME)
    else:
        return generateModel()


def generateModel():
    with open(Cons.DATAFILENAME, "r") as myfile:
        documents = myfile.read().lower().split('\n')

    texts = [word.split() for word in documents]
    model = gensim.models.Word2Vec(texts, min_count=Cons.MINOCCURENCES, size=Cons.NNSIZE, workers=Cons.NUMCORES)
    model.save(Cons.MODELFILENAME)
    return model
