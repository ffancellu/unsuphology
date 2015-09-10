__author__="Tom Kocmi"

CORPUSNAME = "EN"

MODELFILENAME = "models/VectorModel-"+CORPUSNAME+".data" #model filename
FIXESFILENAME = "models/Fixes-"+CORPUSNAME+".data" #filename of saved prefixes and suffixes
DATAFILENAME = "models/"+CORPUSNAME+".txt" #filename of training data

NNSIZE = 100 #size of the word vectors
MINOCCURENCES = 2 #minimum necessary number of occurences of word in the document to allow it in vocabulary
MAXFIX = 5 #longest possible suffix or prefix, In Soricut paper equals 6

RARERULES = 3 #minimal number of pairs in support set of the rule
HITTHRESHOLD = 10
MAXSUPPORTSIZE = 100 #maximal size of support set. In Soricut paper equals 1000. Downsample if more supports


