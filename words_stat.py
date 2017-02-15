# -*- coding: utf-8 -*-

import re

fp = open("sample.txt","r")
article = fp.read()
new_article = re.sub("[^a-zA-Z\s]","",article)
words = new_article.split()
word_counts = dict()
for word in words:
    if word.upper() in word_counts:
        word_counts[word.upper()] += 1
    else:
        word_counts[word.upper()] = 1

key_list = list(word_counts.keys())
key_list.sort()
for key in key_list:
    if word_counts[key] >= 1:
        print("{}:{}".format(key,word_counts[key]))


