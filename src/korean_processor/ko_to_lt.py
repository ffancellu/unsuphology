#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import conversion as Conv
import codecs
import os

KOREAN_DATA_FOLDER="/Users/ffancellu/Documents/Research/Korean_corpora/raw/generality/speech95"
KOREAN_OUTPUT_PATH="/Users/ffancellu/git/unsuphology/src/models/korean_corpus_all.txt"

def create_corpus():
    o = codecs.open(KOREAN_OUTPUT_PATH,'wb','utf8')

    for f in os.listdir(KOREAN_DATA_FOLDER):
        ko_filepath = '%s/%s' % (KOREAN_DATA_FOLDER,f)
        try:
            i = codecs.open(ko_filepath,'rb','cp949').read()
            soup = BeautifulSoup(i)
            for s in soup.find_all("tdmsfiletext"):
                o.write(s.text)
        except(UnicodeDecodeError):
            pass
    o.close()

def transform():

    ko = codecs.open(KOREAN_OUTPUT_PATH,'rb','utf8')
    for line in ko:
        words = line.split()
        words_conv = []
        for i in range(len(words)):
            words_conv.append(Conv.wrapper(words[i]))
        latin_str = ' '.join(filter(lambda x: x!='',words_conv))
        print latin_str
            

if __name__=="__main__":
    # create_corpus()
    transform()
