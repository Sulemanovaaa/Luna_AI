#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from nltk.probability import FreqDist
from nltk.classify import SklearnClassifier
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import json
from textblob import TextBlob as tb
from stemword import Porter
from test_tfidf import *
import pickle




def replace_all(text):
    dic = {',': '', '.': '', ':': '', ';': '', '@': '', '!': '', '$': '', '\'': '', '"': '', '#': '', '%': '',
           '^': '', '&': '', '*': '', '(': '', ')': '', '-': '', '_': '', '+': '', '=': '', '\\': '', '/': '', '?': '',
           '±': '', '<': '', '>': '', '§': '', ' и ': ' ', ' в ': ' ', ' с ': ' ', ' о ': '', ']': '', '[': '', '`': '',
           '~': '', '«': '', '»': '', '0': '', '1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '',
           '9': '', ' а ': ' ', ' к ': ' ', ' к ': ' ', ' те ': ' ', '  ': ' ', 'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '','g': '', 'h': '',
           'i': '', 'j': '', 'k': '', 'l': '', 'm': '', 'n': '', 'o': '', 'p': '', 'q': '', 'r': '', 's': '', 't': '',
           'u': '', 'v': '', 'w': '', 'x': '', 'y': '', 'z': '', ' пр ': ' ', 'мпк ': '', '  когда': '',
           'нтв': '', 'ü': ''}
    for i, j in dic.items():
        text = text.replace(i, j)
    text = text.replace('  ', ' ')
    text = text.replace('   ', ' ')
    return text

bloblist = []
text_list = []

path = '/Users/sulgod/PycharmProjects/Luna_AI/src/ex.json'

with open(path, 'r') as f:
    data = json.loads(f.read())
    dic=[]
    for i in data['articles']['article']:
        document = tb(replace_all(str(i['text']).lower()))
        words = document.words.singularize()
        dic.append(words)
        dics = replace_all(str(dic).lower())
        doc=[]
        for i, j in enumerate(words):
            word = Porter.stem(words[i])
            doc.append(word)
        text = (str(doc).replace("'", "")).replace(",", "")
        text_list.append(tb(text))
        bloblist.append(text)

def newdoc(text):
    doc = (replace_all(text.lower()))
    return doc

cat = np.array([1, 1, 0, 0, 0])
#np.array(cat).reshape(1, -1)
vector = TfidfVectorizer()
transformer = vector.fit_transform(bloblist)
#print('Shape of Sparse Matrix: ', transformer.shape)
#print('Amount of Non-Zero occurrences: ', transformer.nnz)
# Percentage of non-zero values
density = (100.0 * transformer.nnz / (transformer.shape[0] * transformer.shape[1]))
#print('Density: {}'.format((density)))
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(transformer, cat, test_size=0.2, random_state=101)
nb = MultinomialNB()
nb.fit(X_train, y_train)
idf = vector.idf_
top =dict(zip(vector.get_feature_names(), idf))
testtest = newdoc("""Вам знакомо чувство, когда проекты начинают поглощать все ваше время? Слишком много функций для реализации, слишком много найденных ошибок, чрезмерные затраты на исправления. В некоторые дни вы просто недостаточно быстро работаете, слабо продумываете код, тратите часы, чтобы исправить одну единственную ошибку. И чтобы усугубить ситуацию, вы тратите оставшееся время на бессмысленные встречи, а не на работу. Конечно, в такие дни вы начинаете трудиться сверхурочно, чтобы удержать в руках расползающуюся ткань реальности. Довольно скоро такой график становится нормой, и все привыкают, что вам можно писать письма (и требовать ответы) в любое время. Наступает момент выгорания. И тогда вы начинаете задумываться о практиках тайм-менеджмента. Сотни людей вокруг, кажется, только и делают, что учат других. Давайте будем честны друг с другом: все курсы управления временем пишут психологи, менеджеры, кто угодно, только не разработчики. Но ведь многие основополагающие вещи контроля времени и управления проектами придумали именно программисты (Фредерик Брукс: «Если проект не укладывается в сроки, то добавление рабочей силы задержит его еще больше»). Теория, дофамин, бег времени Время — понятие субъективное. У каждого есть свое собственное время, выраженное в способности определять продолжительность моментов, точку наступления событий в будущем, а также время наступления события относительно временных отметок. В 1962 году спелеолог Мишель Сифр провел эксперимент, в ходе которого он находился два месяца в одиночестве в пещере. Эксперимент закончился 14 сентября, в то время как Сифр думал, что еще только 20 августа. Периоды бодрствования и сна «пещерного исследователя» в сумме составили 24,5 часа. Однако субъективные оценки временных промежутков, как продолжительных (сутки), так и кратковременных (120 с), изменились — время словно замедлилось. В более поздних экспериментах испытуемые переходили с 24-часовых суток на 48-часовые (36 часов бодрствования и 12 часов сна). В другом исследовании, которое длилось полгода в пещере, испытуемый смог без всякого сна и дискомфорта для себя провести около 50 часов. Просто для него это время «текло» гораздо быстрее. Так от чего же зависит течение времени внутри нас? Как показывают современные исследования, все связано с уровнем дофамина. Чем меньше дофамина в базальных ганглиях центральной части мозга, тем быстрее для нас течет субъективная минута. Поэтому интересные события, связанные с подъемом уровня дофамина, могут пролетать незаметно, а скучные, вызывающие дофаминовый спад, тянутся долго. Важен не только уровень самого дофамина, но и чувствительность рецепторов к нему. На рецепторы влияют различные зависимости (алкоголь, наркотики, азартные игры и т.д.) и даже постоянные мысли о каком-то хорошем событии, которое еще не наступило, могут оказать негативное воздействие на усвоение дофамина.""")
newdoc_transformed = vector.transform([testtest])
pred = nb.predict(newdoc_transformed)[0]
bloblist.append(testtest)
for i, blob in enumerate(text_list):
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
if pred == 0:
    print ("It's positive article")
    print("Почему {} не оставит вас равнодушным".format(sorted_words[0][0]))
else:
    print ("It's negative article")
    print("Почему из-за {} так плохо".format(sorted_words[0][0]))
