#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import math
import random
from functools import reduce
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

bloblist = []

for i, blob in enumerate(bloblist):
    #print("Top word in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    num = random.randint(1, 3)
   # if num == 1:
   #     print("Почему {} не оставит вас равнодушным".format(sorted_words[0][0]))
   # if num == 2:
   #     print("Как с помощью {} победить всех".format(sorted_words[0][0]))
   # if num == 3:
   #     print("Как {} вам поможет".format(sorted_words[0][0]))
    #for word, score in sorted_words[:5]:
        #print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))
