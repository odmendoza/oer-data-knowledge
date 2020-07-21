import fasttext


model = fasttext.train_supervised(input="lemmatized.train",
                                  lr=0.5, epoch=25, wordNgrams=3)
model.save_model("./models/lemmatized.bin")

"""
model = fasttext.load_model('./models/tokenized_1.5.bin')
prediction = model.predict("Tecnology", k=5)

for p in prediction:
    print(p)

"""