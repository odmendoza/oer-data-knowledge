from prediction import Prediction

my_prediction = Prediction

p = my_prediction.predict(text='Open educative resources')

print(p)
print('Type [ ', type(p), ' ]')