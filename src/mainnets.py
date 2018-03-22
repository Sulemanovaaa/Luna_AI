from sklearn.cross_validation import train_test_split
from keras.preprocessing import sequence
import pandas as pd
import numpy as np
from textblob import TextBlob as tb
import nets
#from clean import *


dataset = pd.read_csv('cleaned.csv', index_col=0).dropna()


n = 20000
max_length = 300

X = []
y = []
dictionary = []

dataset['label'].replace(-1, 0, inplace=True)
dataset = dataset.sample(frac=1)
tpls = list(dataset.itertuples())[:n]

for tpl in tpls:
    row = []
    for word in tpl[2]:
        if word not in dictionary:
            dictionary.append(word)
        row.append(dictionary.index(word) + 1)
    X.append(row)
    y.append(tpl[1])

X = sequence.pad_sequences(np.array(X), maxlen=max_length)
y = np.array(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

model = nets.get_dropout_net(len(dictionary), max_length)
#model.fit(X_train, y_train, batch_size=64, nb_epoch=1)
model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=64, nb_epoch=1)

scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))

'''
from keras.preprocessing.text import Tokenizer
tk = Tokenizer()
testtext = "Общественный транспорт очень популярен в Германии, учитывая его эффективность и относительную дешевизну по сравнению с другими крупными странами Европы — один билет в Берлине стоит 2,90 евро (более 212 рублей). В 2017 году число пассажирских перевозок достигло 10,3 миллиарда, и потребуется серьезное планирование, прежде чем можно будет перейти на бесплатный проезд.  При этом критики идеи бесплатного проезда указывают на высокие расходы, а также на ее невыполнимость в скором будущем. "
testtext=clean(tb(testtext).lower())
tk.fit_on_texts(testtext)
index_list = tk.texts_to_sequences(testtext)
xnew = sequence.pad_sequences(index_list, maxlen=max_length)
result = model.predict_proba(xnew)
print(np.average(result))
'''