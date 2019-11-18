# Copyright 2019 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""CholeskyLKJ distribution class."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Dependency imports
import numpy as np
import tensorflow.compat.v2 as tf

from tensorflow_probability.python.distributions import distribution
from tensorflow_probability.python.distributions import lkj
from tensorflow_probability.python.internal import assert_util
from tensorflow_probability.python.internal import dtype_util
from tensorflow_probability.python.internal import prefer_static
from tensorflow_probability.python.internal import reparameterization
from tensorflow_probability.python.internal import tensor_util
from tensorflow_probability.python.internal import tensorshape_util


__all__ = [
    'CholeskyLKJ',
]


class CholeskyLKJ(distribution.Distribution):
  """The CholeskyLKJ distribution on cholesky factors of correlation matrices.

  This is a one-parameter family of distributions on cholesky factors of
  correlation matrices.

  In other words, if If `X ~ CholeskyLKJ(c)`, then `X @ X^T ~ LKJ(c)`.

  For more details on the LKJ distribution, see `tfp.distributions.LKJ`.

  #### Examples

  ```python
  # Initialize a single 3x3 LKJ with concentration parameter 1.5
  dist = tfp.distributions.CholeskyLKJ(dimension=3, concentration=1.5)

  # Evaluate this at a batch of two observations, each in R^{3x3}.
  x = ...  # Shape is [2, 3, 3].
  dist.prob(x)  # Shape is [2].

  # Draw 6 Cholesky LKJ-distributed 3x3 lower triangular matrices
  ans = dist.sample(sample_shape=[2, 3], seed=42)
  # shape of ans is [2, 3, 3, 3]
  ```
  The sampler follows the 'onion' method from

  [1] Daniel Lewandowski, Dorota Kurowicka, and Harry Joe,
  'Generating random correlation matrices based on vines and extended
  onion method,' Journal of Multivariate Analysis 100 (2009), pp
  1989-2001.
  """

  def __init__(self,
               dimension,
               concentration,
               validate_args=False,
               allow_nan_stats=True,
               name='CholeskyLKJ'):
    """Construct CholeskyLKJ distributions.

    Args:
      dimension: Python `int`. The dimension of the correlation matrices
        to sample.
      concentration: `float` or `double` `Tensor`. The positive concentration
        parameter of the CholeskyLKJ distributions.
      validate_args: Python `bool`, default `False`. When `True`, distribution
        parameters are checked for validity despite possibly degrading runtime
        performance. When `False`, invalid inputs may silently render incorrect
        outputs.
      allow_nan_stats: Python `bool`, default `True`. When `True`, statistics
        (e.g., mean, mode, variance) use the value `NaN` to indicate the
        result is undefined. When `False`, an exception is raised if one or
        more of the statistic's batch members are undefined.
      name: Python `str` name prefixed to Ops created by this class.

    Raises:
      ValueError: If `dimension` is negative.
    """
    if dimension < 0:
      raise ValueError(
          'There are no negative-dimension correlation matrices.')
    parameters = dict(locals())
    with tf.name_scope(name):
      dtype = dtype_util.common_dtype([concentration], tf.float32)
      self._concentration = tensor_util.convert_nonref_to_tensor(
          concentration, name='concentration', dtype=dtype)
      self._dimension = dimension
      super(CholeskyLKJ, self).__init__(
          dtype=self._concentration.dtype,
          validate_args=validate_args,
          allow_nan_stats=allow_nan_stats,
          reparameterization_type=reparameterization.NOT_REPARAMETERIZED,
          parameters=parameters,
          name=name)

  @classmethod
  def _params_event_ndims(cls):
    return dict(concentration=0)

  @property
  def dimension(self):
    """Dimension of returned cholesky factors of correlation matrices."""
    return self._dimension

  @property
  def concentration(self):
    """Concentration parameter."""
    return self._concentration

  def _batch_shape_tensor(self):
    return prefer_static.shape(self.concentration)

  def _batch_shape(self):
    return self.concentration.shape

  def _event_shape_tensor(self):
    return tf.constant([self.dimension, self.dimension], dtype=tf.int32)

  def _event_shape(self):
    return tf.TensorShape([self.dimension, self.dimension])

  def _sample_n(self, num_samples, seed=None, name=None):
    """Returns a Tensor of samples from a CholeskyLKJ distribution.

    Args:
      num_samples: Python `int`. The number of samples to draw.
      seed: Python integer seed for RNG
      name: Python `str` name prefixed to Ops created by this function.

    Returns:
      samples: A Tensor of cholesky factors of correlation matrices with shape
        `[n] + B + [D, D]`, where `B` is the shape of the `concentration`
        parameter, and `D` is the `dimension`.

    Raises:
      ValueError: If `dimension` is negative.
    """
    return lkj.sample_lkj(
        num_samples=num_samples,
        dimension=self.dimension,
        concentration=self.concentration,
        cholesky_space=True,
        seed=seed,
        name=name)

  def _has_valid_dimensions(self, x):
    if tensorshape_util.is_fully_defined(x.shape[-2:]):
      if (tensorshape_util.dims(x.shape)[-2] ==
          tensorshape_util.dims(x.shape)[-1] ==
          self.dimension):
        return []
      else:
        raise ValueError(
            'Input dimension mismatch: expected [..., {}, {}], got {}'.format(
                self.dimension, self.dimension, tensorshape_util.dims(x.shape)))
    elif self.validate_args:
      msg = 'Input dimension mismatch: expected [..., {}, {}], got {}'.format(
          self.dimension, self.dimension, tf.shape(x))
      return [
          assert_util.assert_equal(
              tf.shape(x)[-2], self.dimension, message=msg),
          assert_util.assert_equal(
              tf.shape(x)[-1], self.dimension, message=msg)]
    return []

  def _is_valid_correlation_cholesky(self, x):
    if not self.validate_args:
      return []
    return [
        assert_util.assert_near(
            x,
            tf.linalg.band_part(x, -1, 0),
            message='Cholesky factors must be lower triangular.')
    ]

  def _log_prob(self, x):
    with tf.control_dependencies(
        self._has_valid_dimensions(x) + self._is_valid_correlation_cholesky(x)):
      concentration = tf.convert_to_tensor(self.concentration)
      normalizer = self._log_normalization(concentration=concentration)
      # This log_prob comes from using a change of variables via the Cholesky
      # decomposition on the LKJ's log_prob.
      # The first term represents the change of variables of the LKJ's
      # unnormalized log_prob, the second is the normalization term coming
      # from the LKJ distribution, and the final is a normalization term
      # coming from the change of variables.
      return (self._log_unnorm_prob(x, concentration) -
              normalizer + self.dimension * np.log(2.))

  def _log_unnorm_prob(self, x, concentration, name=None):
    """Returns the unnormalized log density of a CholeskyLKJ distribution.

    Args:
      x: `float` or `double` `Tensor` of Cholesky factors of correlation
        matrices. The shape of `x` must be `B + [D, D]`, where `B` broadcasts
        with the shape of `concentration`.
      concentration: `float` or `double` `Tensor`. The positive concentration
        parameter of the CholeskyLKJ distributions.
      name: Python `str` name prefixed to Ops created by this function.

    Returns:
      log_p: A Tensor of the unnormalized log density of each matrix element of
        `x`, with respect to an CholeskyLKJ distribution with parameter the
        corresponding element of `concentration`.
    """
    with tf.name_scope(name or 'log_unnorm_prob_cholesky_lkj'):
      x = tf.convert_to_tensor(x, name='x')
      logdiag = tf.math.log(tf.linalg.diag_part(x))
      # We pick up a weighted sum of the log(diag) due to the jacobian
      # of the cholesky decomposition. See `tfp.bijectors.CholeskyOuterProduct`
      # for details.
      dimension_range = np.linspace(
          self.dimension,
          1., self.dimension, dtype=dtype_util.as_numpy_dtype(
              concentration.dtype))
      return tf.reduce_sum(
          (2. * concentration[..., tf.newaxis] - 2. + dimension_range) *
          logdiag, axis=-1)

  def _log_normalization(self, concentration=None, name='log_normalization'):
    """Returns the log normalization of a CholeskyLKJ distribution.

    Args:
      concentration: `float` or `double` `Tensor`. The positive concentration
        parameter of the CholeskyLKJ distributions.
      name: Python `str` name prefixed to Ops created by this function.

    Returns:
      log_z: A Tensor of the same shape and dtype as `concentration`, containing
        the corresponding log normalizers.
    """
    # The formula is from D. Lewandowski et al [1], p. 1999, from the
    # proof that eqs 16 and 17 are equivalent.
    with tf.name_scope(name or 'log_normalization_lkj'):
      if concentration is None:
        concentration = tf.convert_to_tensor(self.concentration)
      logpi = np.log(np.pi)
      ans = tf.zeros_like(concentration)
      for k in range(1, self.dimension):
        ans = ans + logpi * (k / 2.)
        ans = ans + tf.math.lgamma(concentration +
                                   (self.dimension - 1 - k) / 2.)
        ans = ans - tf.math.lgamma(concentration + (self.dimension - 1) / 2.)
      return ans

  def _parameter_control_dependencies(self, is_init):
    if not self.validate_args:
      return []
    assertions = []
    if is_init != tensor_util.is_ref(self.concentration):
      # concentration >= 1
      # TODO(b/111451422, b/115950951) Generalize to concentration > 0.
      assertions.append(assert_util.assert_non_negative(
          self.concentration - 1,
          message='Argument `concentration` must be >= 1.'))
    return assertions
