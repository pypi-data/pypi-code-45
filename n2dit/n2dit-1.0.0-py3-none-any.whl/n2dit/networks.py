"""base for GAN model"""
import tensorflow as tf
from .vgg19 import Vgg19

_vgg = None


def lsgan_loss_disc(x, y):
    return (tf.reduce_mean(tf.squared_difference(x, 1)) +
            tf.reduce_mean(tf.squared_difference(y, 0))) * 0.5


def lsgan_loss_gen(x):
    return tf.reduce_mean(tf.squared_difference(x, 1))


def l1_loss(x, y):
    return tf.reduce_mean(tf.abs(x - y))


def perceptual_loss(x, y):
    global _vgg

    if not _vgg:
        _vgg = Vgg19()

    real = tf.image.resize_images(x, [224, 224])
    rec = tf.image.resize_images(y, [224, 224])

    vgg_real22, vgg_real54 = _vgg(real)
    vgg_rec22, vgg_rec54 = _vgg(rec)

    m1 = tf.reduce_mean(tf.squared_difference(vgg_real22, vgg_rec22))
    m2 = tf.reduce_mean(tf.squared_difference(vgg_real54, vgg_rec54))

    loss = (m1 + m2) * 0.00001 * 0.5

    return loss


def pad(inputs, size, mode='CONSTANT', name='pad'):
    """Pads a tensor."""
    return tf.pad(
        inputs, [[0, 0], [size, size], [size, size], [0, 0]], mode, name=name)


def conv2d(inputs, output_nc, ksize, stride, name='conv2d'):
    """Adds an N-D convolution followed by an optional batch_norm layer."""
    with tf.variable_scope(name):
        init = tf.truncated_normal_initializer(stddev=0.02)

        return tf.contrib.layers.conv2d(
            inputs,
            output_nc,
            ksize,
            stride,
            padding='VALID',
            activation_fn=None,
            weights_initializer=init)


def conv2d_trans(inputs, output_nc, name='conv2d_trans'):
    """Adds a convolution2d_transpose with an optional batch normalization
    layer."""
    with tf.variable_scope(name):
        init = tf.truncated_normal_initializer(stddev=0.02)

        return tf.contrib.layers.conv2d_transpose(
            inputs,
            output_nc,
            3,
            2,
            padding='SAME',
            activation_fn=None,
            weights_initializer=init)


def conv2d_resize(inputs, output_nc, name='conv2d_resize'):
    """Adds a convolution2d_resize with an optional batch normalization
    layer."""
    with tf.variable_scope(name):
        out = tf.image.resize(
            inputs,
            tf.shape(inputs)[1:3] * 2,
            align_corners=True,
            name='resize',
            method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
        out = pad(out, 1, 'REFLECT', 'pad')
        return conv2d(out, output_nc, 3, 1, 'conv2d')


def Resnetblock(inputs, output_nc, name='R_block'):
    """Residual Block"""
    with tf.variable_scope(name):
        out = pad(inputs, 1, 'REFLECT', 'pad1')
        out = conv2d(out, output_nc, 3, 1, name=name + '_c1')
        out = tf.contrib.layers.instance_norm(out)
        out = tf.nn.relu(out)

        out = pad(out, 1, 'REFLECT', 'pad2')
        out = conv2d(out, output_nc, 3, 1, name=name + '_c2')
        out = tf.contrib.layers.instance_norm(out)
        # do not use activation layer after the second conv layer

        return inputs + out


def get_upsampler(sam_type):
    if sam_type == 'trans_conv':
        return conv2d_trans
    elif sam_type == 'resize_conv':
        return conv2d_resize
    else:
        raise NotImplementedError('upsampler %s not implemented' % sam_type)


def get_loss_fn(loss_type):
    if loss_type == 'l1':
        return l1_loss
    elif loss_type == 'pcpt':
        return perceptual_loss
    else:
        raise NotImplementedError('loss_fn %s not implemented' % loss_type)


class Generator():
    """CycleGAN generator"""

    def __init__(self, name, nblocks=9, upsample='trans_conv'):
        self.name = name
        self.nblocks = nblocks
        self.upsample = get_upsampler(upsample)

    def __call__(self, inputs):
        return self.forward(inputs)

    def forward(self, inputs):
        """Construct a Resnet-based generator"""
        with tf.variable_scope(self.name, reuse=tf.AUTO_REUSE):
            # Encoder
            out = pad(inputs, 3, 'REFLECT', 'pad1')
            out = conv2d(out, 64, 7, 1, 'c7s1-64')
            out = tf.contrib.layers.instance_norm(out)
            out = tf.nn.relu(out, 'relu1')

            out = pad(out, 1, 'CONSTANT', 'pad2')
            out = conv2d(out, 128, 3, 2, 'd128')
            out = tf.contrib.layers.instance_norm(out)
            out = tf.nn.relu(out, 'relu2')

            out = pad(out, 1, 'CONSTANT', 'pad3')
            out = conv2d(out, 256, 3, 2, 'd256')
            out = tf.contrib.layers.instance_norm(out)
            out = tf.nn.relu(out, 'relu3')

            # Transformer
            for i in range(1, self.nblocks + 1):
                out = Resnetblock(out, 256, 'R256_%d' % i)

            # Decoder
            out = self.upsample(out, 128, 'u128')
            out = tf.contrib.layers.instance_norm(out)
            out = tf.nn.relu(out, 'relu4')

            out = self.upsample(out, 64, 'u64')
            out = tf.contrib.layers.instance_norm(out)
            out = tf.nn.relu(out, 'relu5')

            out = pad(out, 3, 'REFLECT', 'pad4')
            out = conv2d(out, 3, 7, 1, 'u3')
            out = tf.math.tanh(out)

            self.variables = tf.compat.v1.get_collection(
                tf.compat.v1.GraphKeys.TRAINABLE_VARIABLES)

            return out


class Discriminator():
    """CycleGAN discriminator"""

    def __init__(self, name, nlayers=4):
        self.name = name
        self.nlayers = nlayers

    def __call__(self, inputs):
        return self.forward(inputs)

    def forward(self, inputs):
        """Construct a PatchGAN discriminator"""
        with tf.variable_scope(self.name, reuse=tf.AUTO_REUSE):
            out = pad(inputs, 1, 'CONSTANT', 'pad1')
            out = conv2d(out, 64, 4, 2, 'C64-s2')
            out = tf.nn.leaky_relu(out)

            out = pad(out, 1, 'CONSTANT', 'pad2')
            out = conv2d(out, 128, 4, 2, 'C128-s2')
            out = tf.contrib.layers.instance_norm(out)
            out = tf.nn.leaky_relu(out)

            out = pad(out, 1, 'CONSTANT', 'pad3')
            out = conv2d(out, 256, 4, 2, 'C256-s2')
            out = tf.contrib.layers.instance_norm(out)
            out = tf.nn.leaky_relu(out)

            for i in range(1, self.nlayers - 2):
                out = pad(out, 1, 'CONSTANT', 'pad%d' % (i + 3))
                out = conv2d(out, 512, 4, 2, 'C512-s2_%d' % i)
                out = tf.contrib.layers.instance_norm(out)
                out = tf.nn.leaky_relu(out)

            out = pad(out, 1, 'CONSTANT', 'pad%d' % (self.nlayers + 1))
            out = conv2d(out, 512, 4, 1, 'C512-s1')
            out = tf.contrib.layers.instance_norm(out)
            out = tf.nn.leaky_relu(out)

            out = pad(out, 1, 'CONSTANT', 'pad%d' % (self.nlayers + 2))
            out = conv2d(out, 1, 4, 1, 'C1-s1')

            self.variables = tf.compat.v1.get_collection(
                tf.compat.v1.GraphKeys.TRAINABLE_VARIABLES, scope=self.name)

            return out
