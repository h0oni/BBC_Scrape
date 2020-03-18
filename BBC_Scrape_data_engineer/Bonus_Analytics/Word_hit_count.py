# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:23:51 2020

@author: Sakib
"""
from nltk.probability import FreqDist

#Reading the text file with data
with open ("data.txt", "r") as myfile:
    data = myfile.readlines()

#removing punctuations
for char in '-.,?!"\n()\ ':
    data = str(data).replace(char, ' ') 

 #make all word lower case
data = data.lower()

#listing all words. (tokenizing)
word_list = data.split() 

#counting the word frequency with help of dictionary
fdist = FreqDist()
for word in word_list:
    fdist[word] += 1 

#saving the data in csv
with open('analytics.csv', 'w') as f:
    for key in fdist.keys():
        f.write("%s,%s\n"%(key,fdist[key]))


