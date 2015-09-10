#-*- coding:utf-8 -*-

import codecs
import re
import Cons

def find_iter(sub,w):
    return [m.start() for m in re.finditer(sub,w)]

def long_substr(w1,w2):

    # :find the longest common contigouous substrings between two substrings
    # I:str,str
    # O:dict{str:list},dict{str:list}

    substr_w1 = {}
    substr_w2 = {}
    if w1 in w2:
        substr_w1[w1] = [0] 
        substr_w2[w1] = [w2.find(w1)]
    elif w2 in w1:
        substr_w1[w2] = [w1.find(w2)]
        substr_w2[w2] = [0]
    else:
        if len(w1) > 1 or len(w2) > 1:
            i = 0
            while i < len(w1):
                # find the longest common substring
                substr = ""
                end = 0
                for j in range(len(w1)-i+1):
                    if j > len(substr) and w1[i:i+j] in w2:
                        substr = w1[i:i+j]
                        end = i+j
                # print "substr: ",substr,"end: ",end
                if substr!="":
                    substr_w1.setdefault(substr,[]).append(w1.find(substr))
                    substr_w2.setdefault(substr,[]).extend(find_iter(substr,w2))
                i = end if end!=0 else i+1

    return substr_w1,substr_w2

def generate_fixes(w1,w2):
    substr_w1,substr_w2 = long_substr(w1,w2)
    # print substr_w1,substr_w2
    # print substr_w1,substr_w2
    for sub in substr_w1.keys():
        # {'m':[0,4],'s':[3,6]}
        sub1_indeces, sub2_indeces = substr_w1[sub],substr_w2[sub]
        # sub = 'm'; w1_indeces = [i1,i2]; w2_indeces = [i1,i2]
        for s1_start_ind in sub1_indeces:
            for s2_start_ind in sub2_indeces:
                s1_end_ind,s2_end_ind = s1_start_ind+len(sub),s2_start_ind+len(sub)
                # is there a prefix?
                prefix_w1 = w1[:s1_start_ind] if s1_start_ind!=0 else '$'
                prefix_w2 = w2[:s2_start_ind] if s2_start_ind!=0 else '$'
                if len(prefix_w1) < Cons.MAXFIX and len(prefix_w2) < Cons.MAXFIX:
                    if w1[s1_start_ind:]==w2[s2_start_ind:]:
                        print "prefix:%s:%s for %s,%s" % (prefix_w1,prefix_w2,w1,w2)
                # is there a suffix?
                suffix_w1 = w1[s1_end_ind:] if s1_end_ind!=len(w1)-1 else '$'
                suffix_w2 = w2[s2_end_ind:] if s2_end_ind!=len(w2)-1 else '$'
                if len(suffix_w1) < Cons.MAXFIX and len(suffix_w2) < Cons.MAXFIX:
                    if w1[:s1_end_ind]==w2[:s2_end_ind]:
                        print "suffix:%s:%s for %s,%s" % (suffix_w1,suffix_w2,w1,w2)

def gets_vocabulary(filepath):
    f = codecs.open(filepath,'rb','utf8')
    vocabulary = []
    i = 0
    for line in f:
        print "Considering line %d", i
        if len(vocabulary)>1000:
            break
        else:
            words = line.strip().split()
            vocabulary.extend(words)
        i+=1
    return set(vocabulary)

def yield_combinations(voc_set):
    voc_set = list(voc_set)
    for i in range(len(voc_set)):
        for j in range(len(voc_set)):
            if i!=j and i<j:
                yield (voc_set[i],voc_set[j])

def wrapper(filepath):
    print "Fetch vocabulary..."
    voc = gets_vocabulary(filepath)
    print "Vocabulary fecthed!"
    print "vocabulary length: ",len(voc)
    print "Dealing with suffixes..."
    number_tup =0
    for tup in yield_combinations(voc):
        generate_fixes(tup[0],tup[1])
        number_tup+=1
    print "Dealt with suffixes!"

if __name__=="__main__":
    wrapper("/Users/ffancellu/Desktop/orwell.en")