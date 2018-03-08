#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import math
import random
from functools import reduce

from stemword import Porter

from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

def newdoc(text):
    newdoc = tb(replace_all(text.lower()))
    bloblist.append(newdoc)

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

path = '/Users/sulgod/PycharmProjects/Luna_AI/src/ex.json'

#with open(path, 'r') as f:
 #   data = json.loads(f.read())
  #  for i in data['articles']['article']:
   #     document = tb(i['text'])
    #    bloblist.append(document.lower())


with open(path, 'r') as f:
    data = json.loads(f.read())
    doc=[]
    for i in data['articles']['article']:
        document = tb(replace_all(str(i['text']).lower()))
        words = document.words.singularize()
        for i, j in enumerate(words):
            word = Porter.stem(words[i])
            doc.append(word)
            print(word)
        text = tb(str(doc).replace("'", ""))
        bloblist.append(text)

newdoc("""Вам знакомо чувство, когда проекты начинают поглощать все ваше время? Слишком много функций для реализации, слишком много найденных ошибок, чрезмерные затраты на исправления. В некоторые дни вы просто недостаточно быстро работаете, слабо продумываете код, тратите часы, чтобы исправить одну единственную ошибку. И чтобы усугубить ситуацию, вы тратите оставшееся время на бессмысленные встречи, а не на работу. Конечно, в такие дни вы начинаете трудиться сверхурочно, чтобы удержать в руках расползающуюся ткань реальности. Довольно скоро такой график становится нормой, и все привыкают, что вам можно писать письма (и требовать ответы) в любое время. Наступает момент выгорания. И тогда вы начинаете задумываться о практиках тайм-менеджмента. Сотни людей вокруг, кажется, только и делают, что учат других. Давайте будем честны друг с другом: все курсы управления временем пишут психологи, менеджеры, кто угодно, только не разработчики. Но ведь многие основополагающие вещи контроля времени и управления проектами придумали именно программисты (Фредерик Брукс: «Если проект не укладывается в сроки, то добавление рабочей силы задержит его еще больше»). Теория, дофамин, бег времени Время — понятие субъективное. У каждого есть свое собственное время, выраженное в способности определять продолжительность моментов, точку наступления событий в будущем, а также время наступления события относительно временных отметок. В 1962 году спелеолог Мишель Сифр провел эксперимент, в ходе которого он находился два месяца в одиночестве в пещере. Эксперимент закончился 14 сентября, в то время как Сифр думал, что еще только 20 августа. Периоды бодрствования и сна «пещерного исследователя» в сумме составили 24,5 часа. Однако субъективные оценки временных промежутков, как продолжительных (сутки), так и кратковременных (120 с), изменились — время словно замедлилось. В более поздних экспериментах испытуемые переходили с 24-часовых суток на 48-часовые (36 часов бодрствования и 12 часов сна). В другом исследовании, которое длилось полгода в пещере, испытуемый смог без всякого сна и дискомфорта для себя провести около 50 часов. Просто для него это время «текло» гораздо быстрее. Так от чего же зависит течение времени внутри нас? Как показывают современные исследования, все связано с уровнем дофамина. Чем меньше дофамина в базальных ганглиях центральной части мозга, тем быстрее для нас течет субъективная минута. Поэтому интересные события, связанные с подъемом уровня дофамина, могут пролетать незаметно, а скучные, вызывающие дофаминовый спад, тянутся долго. Важен не только уровень самого дофамина, но и чувствительность рецепторов к нему. На рецепторы влияют различные зависимости (алкоголь, наркотики, азартные игры и т.д.) и даже постоянные мысли о каком-то хорошем событии, которое еще не наступило, могут оказать негативное воздействие на усвоение дофамина.""")

for i, blob in enumerate(bloblist):
    print("Top word in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    num = random.randint(1, 3)
   # if num == 1:
   #     print("Почему {} не оставит вас равнодушным".format(sorted_words[0][0]))
   # if num == 2:
   #     print("Как с помощью {} победить всех".format(sorted_words[0][0]))
   # if num == 3:
   #     print("Как {} вам поможет".format(sorted_words[0][0]))
    for word, score in sorted_words[:5]:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))
