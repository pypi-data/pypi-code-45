import tensorflow as tf
import os

IMG_EXTENSIONS = ['.jpg', '.jpeg', '.png']


def is_image_file(fname):
    return os.path.splitext(fname)[-1].lower() in IMG_EXTENSIONS


def get_img_paths(dname):
    assert os.path.isdir(dname), '%s is not a directory' % dname
    paths = [
        os.path.join(dname, fname) for fname in os.listdir(dname)
        if is_image_file(fname)
    ]
    paths.sort()

    return paths


class DatasetLoader:
    def __init__(self, opt):
        self.shuffle = True if hasattr(
            opt, 'shuffle') and opt.shuffle == 'yes' else False
        self.img_size = opt.load_size
        self.crop_size = opt.crop_size if hasattr(opt, 'crop_size') else -1
        self.resize = True if self.img_size != -1 else False
        self.crop = True if self.crop_size != -1 else False
        self.batch_size = 1
        self.len = 0
        self.mode = opt.command
        if self.mode == 'train':
            self.train_set(opt)
        else:
            self.test_set(opt)

    def train_set(self, opt):
        self.dir_A = os.path.join(opt.dirA)
        self.A_paths = get_img_paths(self.dir_A)
        self.AtoB = self.load(self.A_paths).get_next()

        self.dir_B = os.path.join(opt.dirB)
        self.B_paths = get_img_paths(self.dir_B)
        self.BtoA = self.load(self.B_paths).get_next()

    def test_set(self, opt):
        self.dir_A = os.path.join(opt.dirA)
        self.A_paths = get_img_paths(self.dir_A)
        self.AtoB = self.load(self.A_paths).get_next()

    def load(self, paths):
        self.len = max(self.len, len(paths))
        dataset = tf.data.Dataset.from_tensor_slices(paths)
        dataset = dataset.map(self.decode_image)
        if self.shuffle:
            dataset = dataset.shuffle(len(paths))
        dataset = dataset.repeat()
        dataset = dataset.batch(self.batch_size)
        iterator = dataset.make_one_shot_iterator()

        return iterator

    def __len__(self):
        return self.len

    def decode_image(self, img_path):
        img_str = tf.io.read_file(img_path)

        img = tf.cond(
            tf.image.is_jpeg(img_str),
            lambda: tf.image.decode_jpeg(img_str, channels=3),
            lambda: tf.image.decode_png(img_str, channels=3))

        if self.resize:
            img = tf.image.resize(
                img, [self.img_size, self.img_size], align_corners=True)
        else:
            img = tf.image.convert_image_dtype(img, tf.float32)
        if self.crop:
            img = tf.image.random_crop(img,
                                       [self.crop_size, self.crop_size, 3])

        return (img / 127.5) - 1.0

    def get_next(self):
        if self.mode == 'train':
            return self.AtoB, self.BtoA
        else:
            return self.AtoB
