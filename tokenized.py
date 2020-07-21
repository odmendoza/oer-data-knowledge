import fasttext

"""
model = fasttext.train_supervised(input="tokenized.train", lr=0.25,
                                  epoch=300,
                                  dim=100,
                                  ws = 5,
                                  wordNgrams=3)
model.save_model("./models/tokenized_1.5.bin")

"""
model = fasttext.load_model('./models/tokenized_1.5.bin')
prediction = model.predict("Open Educative Resources", k=5)

for p in prediction:
    print(p)

