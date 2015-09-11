__author__ = "Tom Kocmi"

CORPUSNAME = "EN"

RULESTXTFILENAME = "models/RulesTxt-%s.data" % (CORPUSNAME)
MODELFILENAME = "models/VectorModel-%s.data" % (CORPUSNAME) #model filename
FIXESFILENAME = "models/Fixes-%s.data" % (CORPUSNAME) #filename of saved prefixes and suffixes
DATAFILENAME = "models/%s.txt" #filename of training data

NNSIZE = 100 #size of the word vectors
MINOCCURENCES = 2 #minimum necessary number of occurences of word in the document to allow it in vocabulary
MAXFIX = 5 #longest possible suffix or prefix, In Soricut paper equals 6
MINLENCMNSUBSTR=3 #allow only common substring on len > 3
MAXLENSEQLIST= 2

RARERULES = 10  # minimal number of pairs in support set of the rule
HITTHRESHOLD = 100  # consider it that the rule applies in case that the generated vector is within HITTHRESHOLD nearest neighbors
MAXSUPPORTSIZE = 1000  # maximal size of support set. In Soricut paper equals 1000. Downsample if more supports



MEANINGPRESERVINGTHRESHOLD = 0.5 #if cosine similarity of the support set of the rule is smaller than this criterio, do not consider it
MEANINGPRESERVINGTHRESHOLD = 0.5  # if cosine similarity of the support set of the rule is smaller than this criterio, do not consider it

NUMCORES = 8  # number of threads that can be used for model creation
