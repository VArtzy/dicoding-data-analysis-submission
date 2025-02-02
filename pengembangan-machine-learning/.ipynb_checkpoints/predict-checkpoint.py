import tensorflow as tf
import numpy as np
from tensorflow import keras

x = np.array([-4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0])
y = np.array([5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(optimizer="sgd", loss="mean_squared_error")
model.fit(x, y, epochs=500)
print(model.predict(np.array([4, 5])).round())
