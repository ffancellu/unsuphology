__author__ = "Tom Kocmi"

import os.path
import re
import gensim
import Cons


def getVectorModel(generateNew=False):
    if os.path.isfile(Cons.MODELFILENAME) and not generateNew:
        #in case that you are using Google pre trained corpus, you need to load it differently
        #also because the corpus is so big, you will need 64bit Python and enough memory
        if Cons.CORPUSNAME=="Google":
            return gensim.models.Word2Vec.load_word2vec_format(Cons.MODELFILENAME, binary=True)
        else:
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
