import fasttext as ft

model = ft.train_supervised(input="data.train",
                            lr=0.45,
                            epoch=200,
                            wordNgrams=2,
                            ws=5,
                            dim=100)
# model = ft.train_supervised(input="data.train",
#                            autotuneValidationFile='data.valid')
model.save_model("./models/text-classification-model-2.bin")
