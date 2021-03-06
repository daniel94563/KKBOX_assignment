# -*- coding: utf-8 -*-
"""KKBOX_classify_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YJIIHP14ZSMQZmH6CoS8HRWpfwmxeYzO
"""


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from tensorflow import keras
import pandas as pd
import pickle 
import datetime, os
import tensorflow as tf
from sklearn.preprocessing import MultiLabelBinarizer

df = pd.read_csv('../Dataset/Output_dataset/review_w_class.csv', lineterminator='\n', encoding='utf8')

mlb = MultiLabelBinarizer()
tag=[]
for i in range(len(df)):
  tag.append([df['_class\r'][i]])
hashed_tag=mlb.fit_transform(tag)

  

x =df['content']
y =hashed_tag

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
tfidf = TfidfVectorizer()
#pickle.dump(tfidf.fit(X_train), open("./vectorizer_classify.pickle", "wb"))
def tfidf_features(txt, flag):
    if flag == "train":
        x = tfidf.fit_transform(txt).todense()
    else:
        x = tfidf.transform(txt).todense()
    x = x.astype('float32')
    return x 

X_train = tfidf_features(X_train, flag="train")
X_test = tfidf_features(X_test, flag="test")


model = keras.Sequential([
    keras.layers.Dense(1000, input_dim=3897),
    keras.layers.Activation('relu'),
    keras.layers.Dropout(0.25),
    keras.layers.Dense(500, activation='relu'),
    keras.layers.Dropout(0.25),
    keras.layers.Dense(1000, activation='relu'),
    keras.layers.Dropout(0.25),
    keras.layers.Dense(5),
    keras.layers.Activation('softmax'),
])



model.compile(optimizer='adam', loss=tf.keras.losses.CategoricalCrossentropy(), metrics=['accuracy'])

logdir = os.path.join("logs", datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
tensorboard_callback = tf.keras.callbacks.TensorBoard(logdir, histogram_freq=1)

model.fit(X_train, y_train, epochs=1, batch_size=16, validation_split=0.1,callbacks=[tensorboard_callback])
#model.save("./Trained_classify_model")


print(model.evaluate(X_test, y_test))

# Commented out IPython magic to ensure Python compatibility.
# %tensorboard --logdir logs
m=(model.predict(X_test[0])).tolist()
print(m)
model.summary()