import fasttext

model = fasttext.train_supervised(input="stopwords.train", lr=0.25, epoch=300, dim=100, ws=5, wordNgrams=1, loss='ova')

model.save_model("./models/stopwords-1.1.bin")

"""
model = fasttext.load_model('./models/stopwords.bin')
prediction = model.predict("mathematics", k=-1)

print('Type of prediction', type(prediction))
print('len() of prediction', len(prediction))

for p in prediction:
    print(p)
"""
'''
test_result = model.test("./labels.valid")
print(f"Number of sample {test_result[0]}")
print(f"Precision {test_result[1]}")
print(f"Recall {test_result[2]}")
'''

