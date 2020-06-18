#!/usr/bin/python
from flask import Flask, jsonify, abort, make_response, request
import subprocess

from keras.models import Model, Input
from keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional
import keras as k
from keras_contrib.layers import CRF
import numpy as np
import pickle
from keras.preprocessing.sequence import pad_sequences


app = Flask(__name__)

word2index = np.load('word2index.npy', allow_pickle=True)
tag2index = np.load('tag2index.npy', allow_pickle=True)

MAX_LENGTH = 149

input = Input(shape=(MAX_LENGTH,))
word_embedding_size = 300

# Embedding Layer
model = Embedding(input_dim=len(word2index), output_dim=word_embedding_size, input_length=MAX_LENGTH)(input)

# BI-LSTM Layer
model = Bidirectional(LSTM(units=word_embedding_size, 
                           return_sequences=True, 
                           dropout=0.5, 
                           recurrent_dropout=0.5, 
                           kernel_initializer=k.initializers.he_normal()))(model)
model = LSTM(units=word_embedding_size * 2, 
             return_sequences=True, 
             dropout=0.5, 
             recurrent_dropout=0.5, 
             kernel_initializer=k.initializers.he_normal())(model)

# TimeDistributed Layer
model = TimeDistributed(Dense(len(tag2index), activation="relu"))(model)  

# CRF Layer
crf = CRF(len(tag2index))

out = crf(model)  # output
model = Model(input, out)


#Optimiser 
adam = k.optimizers.Adam(lr=0.0005, beta_1=0.9, beta_2=0.999)

# Compile model
model.compile(optimizer=adam, loss=crf.loss_function, metrics=[crf.accuracy, 'accuracy'])
	
model.load_weights('mb-full.h5')

#ESTA FUNCION RECIBE EN sequences LA LISTA DE ORACIONES DONDE CADA ELEMENTO DE LA ORACION ES UN ONE HOT VECTOR
def logits_to_tokens(sequences, index):
    token_sequences = []
    for categorical_sequence in sequences:
        token_sequence = []
        for categorical in categorical_sequence:
            token_sequence.append(index[np.argmax(categorical)])
 
        token_sequences.append(token_sequence)
 
    return token_sequences

@app.route('/', methods=['POST'])
def serve():
	
	test_samples = request.json['text']
	
	test_samples = text.split("\n")
	for i in range(len(text)):
		test_samples[i] = test_samples[i].split()
		
	test_samples_X = []
	
	for s in test_samples:
		s_int = []
		for w in s:
			try:
				s_int.append(word2index[w.lower()])
			except KeyError:
				s_int.append(word2index['-OOV-'])
		test_samples_X.append(s_int)

	test_samples_X = pad_sequences(test_samples_X, maxlen=MAX_LENGTH, padding='post')
	predictions = model.predict(test_samples_X)
	log_tokens = logits_to_tokens(predictions, {i: t for t, i in tag2index.items()})
	return jsonify({"msg":log_tokens})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
