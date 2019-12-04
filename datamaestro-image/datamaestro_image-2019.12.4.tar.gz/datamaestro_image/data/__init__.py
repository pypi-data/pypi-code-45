from datamaestro.data import Generic
from datamaestro.data.ml import Supervised
from datamaestro.definitions import Data, Argument, Type, DataTasks, DataTags, Dataset

@Data()
class Image(Generic): pass

@DataTasks("image classification")
@DataTags("images")
@Data()
class ImageClassification(Supervised):
  """Image classification dataset"""
  pass


@Argument("images", Image)
@Argument("labels", Generic)
@DataTasks("image classification")
@DataTags("images")
@Data()
class LabelledImages:
  """Image classification dataset"""
  pass

