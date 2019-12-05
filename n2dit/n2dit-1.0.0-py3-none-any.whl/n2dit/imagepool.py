import random
import tensorflow as tf


class ImagePool():
    """implements an image buffer"""

    def __init__(self, pool_size):
        """Initialize ImagePool class"""
        self.pool_size = pool_size
        if self.pool_size > 0:
            self.num_imgs = 0
            self.images = []

    def query(self, image):
        """Return an image from the pool"""
        if self.pool_size == 0:
            return image
        if self.num_imgs < self.pool_size:
            self.num_imgs += 1
            self.images.append(image)
            return image
        else:
            p = random.uniform(0, 1)
            if p > 0.5:
                random_id = random.randint(0, self.pool_size - 1)
                tmp = self.images[random_id].copy()
                self.images[random_id] = image.copy()
                return tmp
            else:
                return image
