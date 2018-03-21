import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from textblob import TextBlob as tb
import json
import six.moves.cPickle as pickle
import pymorphy2



def clean(document):
    words = document.words.singularize()
    doc = []
    morph = pymorphy2.MorphAnalyzer()
    alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for i, j in enumerate(words):
        word = words[i]
        cleaned_text = ''
        for char in word:
            if (char.isalpha() and char[0] in alph) or (char == ' '):
                cleaned_text += char
        # print(word)
        if (cleaned_text != '' and len(cleaned_text) > 3):
            #cleaned_text = Porter.stem(cleaned_text)
            doc.append(morph.parse(cleaned_text)[0].normal_form)
    text = (str(doc).replace("'", "")).replace(",", "")
    return text
'''
path = '/Users/sulgod/PycharmProjects/Luna_AI/src/all.json'
pos=[]
bloblist=[]
with open(path, 'r') as f:
    data = json.loads(f.read())
    dic=[]
    for i in data:
        document = tb(str(i['text']).lower())
        words = document.words.singularize()
        doc=[]
        if(str(i['isPos'])=='true'):
            pos.append(1)
        else:
            pos.append(0)
        bloblist.append(clean(document))
    df = pd.DataFrame({'text': bloblist, 'label': pos})
    df.to_csv('cleaned_data.csv')
'''