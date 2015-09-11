#-*- coding:utf-8 -*-

import codecs
import re
import Cons

def find_ordered_common_subseqs(w1,w2):
    len_w1 = len(w1)
    len_w2 = len(w2)
    common_seqs = []

    # deals with full reduplciation
    if w1 in w2:
        common_seqs.append(w1)
    elif w2 in w1:
        common_seqs.append(w2)
    else:
        if len_w1 > 1 or len_w2 > 1:
            to_consider = None
            i = 0
            while i < len_w1:
                # find the longest common substring
                substr = ""
                end = 0
                end_index_w2 = 0
                for j in xrange(len_w1-i+1):
                    where_w2 = w2.find(w1[i:i+j])
                    if j > len(substr) and where_w2!=-1:
                        substr = w1[i:i+j]
                        end = i+j
                        end_index_w2 = where_w2 + len(substr)-1
                if substr!="":
                    if to_consider==None:
                        to_consider = (substr,end_index_w2)
                    else:
                        if end_index_w2 > to_consider[1]:
                            common_seqs.append(to_consider[0])
                        to_consider = (substr,end_index_w2)
                i = end if end!=0 else i+1
            # dump any to_consider left
            if to_consider!=None:
                common_seqs.append(to_consider[0])

    return common_seqs

def get_affixes(w1,w2,common_seqs):
    if common_seqs!=[]:
        if len(common_seqs)<Cons.MAXLENSEQLIST:
            if len(common_seqs[0])>Cons.MINLENCMNSUBSTR:
                print len(common_seqs),len(common_seqs[0])
                regex = '|'.join(common_seqs)
                w1_sub = re.sub(regex,"_",w1)
                w2_sub = re.sub(regex,"_",w2)
                print "r::%s:%s for %s,%s" % (w1_sub,w2_sub,w1,w2)

def gets_vocabulary(filepath):
    f = codecs.open(filepath,'rb','utf8')
    vocabulary = []
    i = 0
    for line in f:
        if len(vocabulary)>1000:
            break
        else:
            words = line.strip().split()
            vocabulary.extend(words)
        i+=1
    return set(vocabulary)

def wrapper(filepath):
    # print "Fetch vocabulary..."
    voc = list(gets_vocabulary(filepath))
    # print "Vocabulary fecthed!"
    # print "vocabulary length: ",len(voc)
    # print "Dealing with suffixes..."
    # number_tup =0
    # for tup in yield_combinations(voc):
    # w1,w2 = "kutub","kitab"
    # cs = find_ordered_common_subseq(w1,w2)
    # get_affixes(w1,w2,cs)
    voc_len = len(voc)
    for i in xrange(voc_len):
        for j in xrange(voc_len):
            if i<j:
                w1,w2 = voc[i],voc[j]
                cs = find_ordered_common_subseqs(voc[i],voc[j])
                get_affixes(w1,w2,cs)
    #     generate_fixes(tup[0],tup[1])
    #     number_tup+=1
    # print "Dealt with suffixes!"

if __name__=="__main__":
    wrapper("/Users/ffancellu/Desktop/orwell.en")