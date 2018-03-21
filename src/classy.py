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

def newdoc(text):
    doc = (clean(tb(text).lower()))
    dataset = pd.read_csv('cleaned_data.csv', index_col=0).dropna()
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
    print(pred1)
    feature_names = vector.get_feature_names()

    doc = 0
    feature_index = newdoc_transformed[doc, :].nonzero()[1]
    tfidf_scores = zip(feature_index, [newdoc_transformed[doc, x] for x in feature_index])
    sorted_words = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)

    if pred == 1:
        print("It's positive article")
        return("Почему {} не оставит вас равнодушным".format(feature_names[sorted_words[0][0]]))
    else:
        print("It's negative article")
        return ("Почему из-за {} так плохо".format(feature_names[sorted_words[0][0]]))


testtest = newdoc("""Общественный транспорт очень популярен в Германии, учитывая его эффективность и относительную дешевизну по сравнению с другими крупными странами Европы — один билет в Берлине стоит 2,90 евро (более 212 рублей). В 2017 году число пассажирских перевозок достигло 10,3 миллиарда, и потребуется серьезное планирование, прежде чем можно будет перейти на бесплатный проезд.  При этом критики идеи бесплатного проезда указывают на высокие расходы, а также на ее невыполнимость в скором будущем. """)
print(testtest)

