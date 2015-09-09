__author__="Tom Kocmi"


MODELFILENAME = "models/VectorModel.data" #model filename
FIXESFILENAME = "models/Fixes.data" #filename of saved prefixes and suffixes
DATAFILENAME = "models/orwell.txt" #filename of training data

NNSIZE = 100 #size of the word vectors
MINOCCURENCES = 1 #minimum necessary number of occurences of word in the document to allow it in vocabulary
MAXFIX = 5 #longest possible suffix or prefix, originaly 6

RARERULES = 3 #minimal number of pairs in support set of the rule

