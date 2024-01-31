import tensorflow as tf
import numpy as np

################################################################
# Tensorflow 
################################################################

# This checks that your local environment can handle Tensorflow properly by running a simple Tensorflow model.

# Generate training data
X_train = np.linspace(0, 2 * np.pi, 100)
y_train = np.sin(X_train)

DENSE_SIZE = 10
# Build the model
model = tf.keras.Sequential()
model.add(tf.keras.Input(shape=(1)))
model.add(tf.keras.layers.Dense(10, activation="tanh"))
model.add(tf.keras.layers.Dense(3, activation="tanh"))
model.add(tf.keras.layers.Dense(1))

# Compile the model
model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.05), loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=2000)

# Test the model
X_test = np.linspace(0, 2 * np.pi, 50)
y_test = model.predict(X_test)

# Save the model into a file
model.save("model")

# Plot the results
import matplotlib.pyplot as plt
plt.plot(X_test, y_test)
plt.savefig("test_fig.png")

