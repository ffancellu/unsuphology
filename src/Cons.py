__author__ = "Tom Kocmi"

CORPUSNAME = "EN"
ISINDIRECTORY = False #in case that corpus is stored in separate directory instead of one file


RULESTXTFILENAME = "models/RulesTxt-%s.data" % (CORPUSNAME)
MODELFILENAME = "models/VectorModel-%s.data" % (CORPUSNAME) #model filename
FIXESFILENAME = "models/Fixes-%s.data" % (CORPUSNAME) #filename of saved prefixes and suffixes
DATAFILENAME = "models/%s.txt" % (CORPUSNAME) #filename of training data, it should have sentence per line
DATADIRNAME = "models/%s/" % (CORPUSNAME) #in case that corpus is stored in separate files in directory

#word2vec model
NNSIZE = 500  # size of the word vectors
NUMCORES = 8  # number of threads that can be used for model creation
MINOCCURENCES = 5  # minimum necessary number of occurences of word in the document to allow it in vocabulary

#generation of affixes
MAXFIX = 5  # longest possible suffix or prefix, In Soricut paper equals 6
MAXWORDS4AFFIXES = 60000 # maximal number of words used to generate affixes

#generation and evaluation of rules
RARERULES = 10  # minimal number of pairs in support set of the rule
HITTHRESHOLD = 100  # consider it that the rule applies in case that the generated vector is within HITTHRESHOLD nearest neighbors
MAXSUPPORTSIZE = 1000  # maximal size of support set. In Soricut paper equals 1000. Downsample if more supports
MEANINGPRESERVINGTHRESHOLD = 0.5  # if cosine similarity of the support set of the rule is smaller than this criterio, do not consider it


MINLENCMNSUBSTR=3 #allow only common substring on len > 3
MAXLENSEQLIST= 2