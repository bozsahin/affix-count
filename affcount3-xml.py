# simple affix count, which you can also use for allomorphy --cem bozsahin, Mar 2019
# this one is for text in xml files

# argument index 0: this script, index 1: input file, 2-n: affixes

# Some interfacing
# we take a text file name and a plain sequence of Aff()s as search terms, assuming
#   all affixes in the sequence are to be searched in text
# if you pass in same affix in different forms, e.g. -ler and -lar for the Turkish plural
#  you'll get allomorphic counts

import sys # for interface
import re  # for affix search
import string # for cleaning up pun ctuation
import xml.etree.ElementTree as ET   # for xml processing

class Aff():   # affixes are identified as suffixes like '-ness' or prefixes like 're-'
    # or infixes like '-fuckin-'.  NOTE:  you need the dash or dashes in the name
    def __init__ (self,morph):
        self.name = morph
        self.type = "suffix" if morph[0] == '-' else "prefix" if morph[-1] == '-' else "error"
        self.type = "infix" if morph[0] == '-' and morph[-1] == '-' else self.type
        self.form = morph[1:] if self.type == "suffix" else morph[:-1] if self.type == "prefix" else morph[1:-1] if self.type == "infix" else []
        self.count = 0
        

#set up the affix list
affixlist=[]
for params in sys.argv[2:]:    
    aff=Aff(params)
    affixlist.append(aff)

codec = str.maketrans('','',string.punctuation)  # to get rid of punctuation later

# get the xml file's structured representation
tree = ET.parse(sys.argv[1])
root = tree.getroot()

#read text, clean them and split to words, and count
wc=0
cleanline = ''.join(root.itertext())
cleanline = re.sub('[^\w\s]',' ',cleanline.strip())  # turn them to space
cleanline = cleanline.translate(codec) # standard removal -- python 3 version
if cleanline:
   for word in cleanline.split():
       wc +=1
       for aff in affixlist:
           if aff.type == "suffix" and re.search('.+'+aff.form+'$',word):
              aff.count += 1
           if aff.type == "prefix" and re.search('^'+aff.form+'.+',word):
              aff.count += 1
           if aff.type == "infix" and re.search('.+'+aff.form+'.+',word):
              aff.count += 1

# report
print("Number of affixes in file (%d tokens in text): %s" % (wc,sys.argv[1]))
for aff in affixlist:
    print("%s : %d" % (aff.name,aff.count))

