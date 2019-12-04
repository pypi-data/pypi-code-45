from datamaestro_image.data import ImageClassification, LabelledImages, Generic
from datamaestro.data.tensor import IDX

from datamaestro.download.single import FileDownloader
from datamaestro.definitions import Data, Argument, Type, DataTasks, DataTags, Dataset


@FileDownloader("train_images.idx", "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz")
@FileDownloader("train_labels.idx", "http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz")
@FileDownloader("test_images.idx", "http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz")
@FileDownloader("test_labels.idx", "http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz")
@Dataset(
  ImageClassification,
  url="http://yann.lecun.com/exdb/mnist/",
)
def MNIST(train_images, train_labels, test_images, test_labels):
  """The MNIST database
  
  The MNIST database of handwritten digits, available from this page, has a
  training set of 60,000 examples, and a test set of 10,000 examples. It is a
  subset of a larger set available from NIST. The digits have been
  size-normalized and centered in a fixed-size image. 
  """
  return {
    "train": LabelledImages(
      images=IDX(path=train_images),
      labels=IDX(path=train_labels)
    ),
    "test": LabelledImages(
      images=IDX(path=test_images),
      labels=IDX(path=test_labels)
    ),
  }
