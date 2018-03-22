#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from test_tfidf import *
from clean import *
from textblob import TextBlob as tb
import six.moves.cPickle as pickle
import random

def newdoc(text):
    doc = (clean(tb(text).lower()))
    dataset = pd.read_csv('cleaned.csv', index_col=0).dropna()
    vector = TfidfVectorizer()

    transformer = vector.fit_transform(dataset['text'])
    pos = dataset['label']

    #nb = MultinomialNB()
    #nb=nb.fit(transformer, pos)

    newdoc_transformed = vector.transform([doc])
    # save the classifier
    #with open('nb_classifier.pkl', 'wb') as fid:
    #    pickle.dump(nb, fid)

    # load MultinomialNB
    with open('nb_classifier.pkl', 'rb') as fid:
        nb_loaded = pickle.load(fid)

    #svm = SGDClassifier(loss='hinge', penalty='l2', alpha = 1e-3, n_iter = 5, random_state = 42)
    #svm = svm.fit(transformer, pos)
    #with open('svm_classifier.pkl', 'wb') as fid:
    #    pickle.dump(nb, fid)

    # load svm
    with open('svm_classifier.pkl', 'rb') as fid:
        svm_loaded = pickle.load(fid)
    pred = nb_loaded.predict(newdoc_transformed)[0]
    pred1 = svm_loaded.predict(newdoc_transformed)[0]
    feature_names = vector.get_feature_names()

    doc = 0
    feature_index = newdoc_transformed[doc, :].nonzero()[1]
    tfidf_scores = zip(feature_index, [newdoc_transformed[doc, x] for x in feature_index])
    sorted_words = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)

    if (pred == 1 or pred1 == 1):
        print("It's positive article")
        num = random.randint(1, 3)
        if num == 1:
            return ("Почему {} не оставит вас равнодушным".format(feature_names[sorted_words[0][0]]))
        if num == 2:
            return ("Как с помощью {} победить всех".format(feature_names[sorted_words[0][0]]))
        if num == 3:
            return ("Как {} вам поможет".format(feature_names[sorted_words[0][0]]))
    else:
        print("It's negative article")
        num = random.randint(1, 3)
        if num == 1:
            return ("Почему из-за {} так плохо".format(feature_names[sorted_words[0][0]]))
        if num == 2:
            return ("Почему мы совершаем одинаковые ошибки с {}".format(feature_names[sorted_words[0][0]]))
        if num == 3:
            return ("Как победить {} в три этапа".format(feature_names[sorted_words[0][0]]))
