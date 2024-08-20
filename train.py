from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# Load the data into the dataset variable
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')

# Segregate dataset into input and output
x = dataset[:,0:8]
y = dataset[:,8]

# Designing neural neural network
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train
model.fit(x, y, epochs=50, batch_size=10)

# Evaluate the model
_, accuracy = model.evaluate(x, y)
print('Accuracy: %.2f' % (accuracy*100))

# Save the model
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

# Save the weights with the correct file path
model.save_weights("model.weights.h5")
print("Saved model to disk")