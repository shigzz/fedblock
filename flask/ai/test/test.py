import tensorflow as tf
import pickle

placeX = tf.placeholder(tf.float32, shape=[None,784])
placeY = tf.placeholder(tf.float32, shape=[None,10])

in_dim = int(placeX.get_shape()[1])
out_dim = int(placeY.get_shape()[1])
hd = 128

#print(in_dim,out_dim)

initialw = tf.truncated_normal([in_dim,hd],stddev=0.1)
initialb = tf.constant(0.1,shape=[hd])
initialw2 = tf.truncated_normal([hd,out_dim],stddev=0.1)
initialb2 = tf.constant(0.1,shape=[out_dim])

W1 = tf.Variable(initialw)
b1 = tf.Variable(initialb)

#print(W1,b1)

W2 = tf.Variable(initialw2)
b2 = tf.Variable(initialb2)


h1 = tf.nn.relu(tf.matmul(placeX,W1)+b1)

selfy = tf.matmul(h1,W2)+b2

var_list = [W1,b1,W2,b2]

#print(var_list)

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=placeY,logits=selfy))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(selfy,1),tf.argmax(placeY,1))


accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))


init = tf.global_variables_initializer()
weights = []
with tf.Session() as sess:
    sess.run(init)
    for v in range(len(var_list)):
        weights.append(var_list[v].eval())

print(weights)

with open('model.pkl','wb') as f:
    pickle.dump(weights,f)

