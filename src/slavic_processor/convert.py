#-*- coding:utf-8 -*-

import re
import os
import string

table = string.maketrans("","")
SLAVIC_DATA="/net/cluster/TMP/kljueva/kontext/word2vec/unsuphology/src/models"

def clean():
        for filename in os.listdir(SLAVIC_DATA):
                outfilename = filename+"_cleaned.txt"
                if filename.startswith("umc"):
                        f = open(outfilename,'w') 
                        umc_file = SLAVIC_DATA+"/"+filename
                        for line in open(umc_file):
                                line = re.sub('“', '',line)
                                line = re.sub('„', '',line)
                                f.write(test_trans(line))


def test_trans(s):
    return s.translate(table, string.punctuation)
    

if __name__=="__main__":
        clean()
