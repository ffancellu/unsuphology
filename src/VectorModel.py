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
    class MySentences(object):
        def __init__(self, dirname):
            self.dirname = dirname

        def __iter__(self):
            if Cons.ISINDIRECTORY:
                for fname in os.listdir(self.dirname):
                    for line in open(os.path.join(self.dirname, fname)):
                        yield line.split()
            else:
                for line in open(self.dirname):
                    yield line.split()

    sentences = MySentences(Cons.DATAFILENAME) # a memory-friendly iterator
    model = gensim.models.Word2Vec(sentences, min_count=Cons.MINOCCURENCES, size=Cons.NNSIZE, workers=Cons.NUMCORES)
    model.save(Cons.MODELFILENAME)
    return model
