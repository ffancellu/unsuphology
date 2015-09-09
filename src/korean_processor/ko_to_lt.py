#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from ConfigParser import ConfigParser
import conversion as Conv
import codecs
import os

config = ConfigParser()
config.read("../config.cfg")

def create_corpus(ko_dir):

    o = codecs.open(config.get("korean","output"),'wb','utf8')

    for f in os.listdir(ko_dir):
        ko_filepath = '%s/%s' % (ko_dir,f)
        i = codecs.open(ko_filepath,'rb','cp949').read()
        soup = BeautifulSoup(i)
        for s in soup.find_all("tdmsfiletext"):
            o.write(s.text)

    o.close()

def transform():

    ko = codecs.open(config.get("korean","output"),'rb','utf8')
    for line in ko:
        words = line.split()
        words_conv = []
        for i in range(len(words)):
            words_conv.append(Conv.wrapper(words[i]))
        latin_str = ' '.join(filter(lambda x: x!='',words_conv))
        print latin_str
            

if __name__=="__main__":
    # create_corpus(config.get("korean","input"))
    transform()
