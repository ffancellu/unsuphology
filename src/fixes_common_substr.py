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
    w1_sub = None
    w2_sub = None
    if common_seqs!=[]:
        if len(common_seqs)<Cons.MAXLENSEQLIST:
            if len(common_seqs[0])>Cons.MINLENCMNSUBSTR:
                regex = '|'.join(common_seqs)
                w1_sub = re.sub(regex,"_",w1)
                w2_sub = re.sub(regex,"_",w2)
                
    return w1_sub,w2_sub

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

def fetch(voc,store=True,store_how="pickle"):
    trie = {}
    for i in xrange(voc_len):
        for j in xrange(voc_len):
            if i<j:
                if number_tup % 100==0:
                    print "Generating rule for tuple %d..." % number_tup
                w1,w2 = voc[i],voc[j]
                cs = find_ordered_common_subseqs(voc[i],voc[j])
                w1_sub,w2_sub = get_affixes(w1,w2,cs)
                if w1_sub!=None and w2_sub!=None:
                    nested_voc = trie.setdefault(w1_sub,{})
                    nested_voc.setdefault(w2_sub,[]).append((w1,w2))
                    
        number_tup+=1

    if store_how=="pickle":  
        print "Pickling results..."
        with open(Cons.FIXESFILENAME, 'wb') as f:
            pickle.dump(trie, f)
    if store_how=="write_txt":
        print "Writing to file..."
        with open(Cons.RULESTXTFILENAME, 'wb','utf8') as f:
            for key in trie.iterkeys():
                for key_n in trie[key].iterkeys():
                    items = trie[key][key_n]
                    f.write("rule::%s:%s %d\n" % (key,key_n,len(items)))
                    for item in items:
                        f.write("\t%s %s\n" % (item[0],item[1]))

    if store_how=="std_err":
        print "Printing to stdErr..."
        for key in trie.iterkeys():
            for key_n in trie[key].iterkeys():
                items = trie[key][key_n]
                print "rule::%s:%s %d\n" % (key,key_n,len(items))
                for item in items:
                        print "\t%s %s\n" % (item[0],item[1])

def wrapper(filepath):
    print "Fetch vocabulary..."
    voc = list(gets_vocabulary(filepath))
    voc_len = len(voc)
    print "Vocabulary fecthed!"
    print "vocabulary length: ",len(voc)
    print "Dealing with suffixes..."
    number_tup =0
    fetch(voc)
    print "Dealt with suffixes!"

if __name__=="__main__":
    wrapper("/Users/ffancellu/Desktop/orwell.en")