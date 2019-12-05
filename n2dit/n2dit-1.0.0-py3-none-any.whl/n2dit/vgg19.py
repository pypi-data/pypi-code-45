import tensorflow as tf
import numpy as np
import os

VGG_MEAN = [103.939, 116.779, 123.68]


class Vgg19:
    def __init__(self, name='vgg19', vgg19_npy_path=None):
        if vgg19_npy_path is None:
            vgg19_npy_path = './n2dit/vgg19.npy'
        self.name = name
        self.build(vgg19_npy_path)

    def build(self, vgg19_npy_path):
        dat = np.load(vgg19_npy_path, encoding='latin1').item()
        self.weight, self.bias = {}, {}

        with tf.variable_scope(self.name):
            for key in sorted(dat.keys()):
                with tf.variable_scope(key):
                    self.bias[key] = tf.constant(dat[key][1], name="bias")
                    self.weight[key] = tf.constant(dat[key][0], name="weight")

    def __call__(self, rgb):
        """
        load variable from npy to build the VGG
        :param rgb: rgb image [batch, height, width, 3] values scaled [0, 1]
        """

        rgb_scaled = (rgb + 1) * 127.5

        # Convert RGB to BGR
        red, green, blue = tf.split(
            axis=3, num_or_size_splits=3, value=rgb_scaled)
        assert red.get_shape().as_list()[1:] == [224, 224, 1]
        assert green.get_shape().as_list()[1:] == [224, 224, 1]
        assert blue.get_shape().as_list()[1:] == [224, 224, 1]
        bgr = tf.concat(
            axis=3,
            values=[
                blue - VGG_MEAN[0],
                green - VGG_MEAN[1],
                red - VGG_MEAN[2],
            ])
        assert bgr.get_shape().as_list()[1:] == [224, 224, 3]

        with tf.variable_scope(self.name, reuse=True):
            out = self.conv_layer(bgr, "conv1_1")
            out = self.conv_layer(out, "conv1_2")
            out = self.max_pool(out, 'pool1')

            out = self.conv_layer(out, "conv2_1")
            out = self.conv_layer(out, "conv2_2")
            out = self.max_pool(out, 'pool2')
            pool2 = out

            out = self.conv_layer(out, "conv3_1")
            out = self.conv_layer(out, "conv3_2")
            out = self.conv_layer(out, "conv3_3")
            out = self.conv_layer(out, "conv3_4")
            out = self.max_pool(out, 'pool3')

            out = self.conv_layer(out, "conv4_1")
            out = self.conv_layer(out, "conv4_2")
            out = self.conv_layer(out, "conv4_3")
            out = self.conv_layer(out, "conv4_4")
            out = self.max_pool(out, 'pool4')

            out = self.conv_layer(out, "conv5_1")
            out = self.conv_layer(out, "conv5_2")
            out = self.conv_layer(out, "conv5_3")
            out = self.conv_layer(out, "conv5_4")
            out = self.max_pool(out, 'pool5')
            pool5 = out

            return pool2, pool5
#             out = self.fc_layer(out, "fc6")
#             assert out.get_shape().as_list()[1:] == [4096]
#             out = tf.nn.relu(out, 'fc6/relu')

#             out = self.fc_layer(out, "fc7")
#             out = tf.nn.relu(out, 'fc7/relu')

#             out = self.fc_layer(out, "fc8")
#             out = tf.nn.softmax(out, name="prob")

#             return out

    def max_pool(self, bottom, name):
        return tf.nn.max_pool(
            bottom,
            ksize=[1, 2, 2, 1],
            strides=[1, 2, 2, 1],
            padding='SAME',
            name=name)

    def conv_layer(self, bottom, name):
        with tf.variable_scope(name):
            weight = self.weight[name]
            conv = tf.nn.conv2d(bottom, weight, [1, 1, 1, 1], padding='SAME')
            bias = tf.nn.bias_add(conv, self.bias[name])
            relu = tf.nn.relu(bias, 'relu')
            return relu


#     def fc_layer(self, bottom, name):
#         with tf.variable_scope(name):
#             shape = bottom.get_shape().as_list()
#             dim = 1
#             for d in shape[1:]:
#                 dim *= d
#             x = tf.reshape(bottom, [-1, dim])

#             weights = self.weight[name]
#             biases = self.bias[name]

#             # Fully connected layer. Note that the '+' operation automatically
#             # broadcasts the biases.
#             fc = tf.nn.bias_add(tf.matmul(x, weights), biases)

#             return fc
