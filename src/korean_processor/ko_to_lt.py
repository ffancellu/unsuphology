#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
import codecs
import os

def openfile(ko_dir):
    for f in os.listdir(ko_dir):
        ko_filepath = '%s/%s' % (ko_dir,f)
        i = codecs.open(ko_filepath,'rb','cp949').read()
        soup = BeautifulSoup(i)
        for s in soup.find_all("tdmsfiletext"):
            print s.text

if __name__=="__main__":
    DIR = "/Users/ffancellu/Documents/Research/Korean_corpora/raw/mass-media/magazine"
    openfile(DIR)
