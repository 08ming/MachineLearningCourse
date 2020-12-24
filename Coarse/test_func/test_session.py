import tensorflow as tf

input1 = tf.Variable(1,)
input2 = tf.Variable([[1, 2, 3]])

sum_ = tf.add(input1, input2)

with tf.variable_creator_scope("ds"):
    print(input1.shape)
    print(input2.shape)
    print(sum_)