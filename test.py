from numpy import loadtxt
from keras.models import model_from_json

# Load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
x = dataset[:, 0:8]
y = dataset[:, 8]

# Load the model architecture from JSON
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

# Create the model from the JSON file
model = model_from_json(loaded_model_json)

# Load the model weights
model.load_weights("model.weights.h5")  # Ensure the weights file name matches your saved weights file
print("Loaded model from disk")

# Make predictions
predictions = model.predict(x)  # Get the predicted probabilities
predicted_classes = (predictions > 0.5).astype(int)  # Convert probabilities to class labels

# Display predictions for a few samples
for i in range(5, 10):
    print('%s => %d (Original Class: %d)' % (x[i].tolist(), predicted_classes[i][0], y[i]))
    