import tensorflow as tf


# a = tf.Variable([[4.0, 5.0, 6.0, -0.1, 0],[1.0, 2.0, 3.0, -0.1, 4.0]])
# b = tf.Variable([[1.0, 2.0, 3.0, -0.1]])
# output = tf.reshape(a, [2, 5])
# print(output)
# print(b)

input_shape = (4, 3, 8)
x = tf.random.normal(input_shape)
y = tf.keras.layers.GlobalAveragePooling1D()(x)
print(y)