import tensorflow as tf
import numpy as np

class Edge_Toolkit:

    def __init__(self, logger):
        self.logger = logger
        self.samples = None
        pass

    def convert_model_lite(self, calibration_data, pb_model_path=None, keras_model_path=None):
        self.samples = calibration_data
        # try:
        if (pb_model_path is not None):
            converter = tf.lite.TFLiteConverter.from_saved_model(pb_model_path)
            tflite_model = converter.convert()
            open('../storage/' + pb_model_path.split('/')[-1].split('.')[0] + ".tflite", "wb").write(tflite_model)
            self.logger.info("Converted pb model " + str(pb_model_path.split('/')[-1]) + " to tf lite")

        if (keras_model_path is not None):
            # converter = tf.lite.TFLiteConverter.from_keras_model_file(keras_model_path)
            converter = tf.compat.v1.lite.TFLiteConverter.from_keras_model_file(keras_model_path)

            if (tf.__version__ == '1.14.0'):
                converter.target_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
            elif (tf.__version__ == '2.0.0-beta1'):
                converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
            else:
                converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
            # TODO This should be a choice at some point... quantize or not... may not be necessary if not using TPU
            converter.representative_dataset = self.representative_dataset_gen
            converter.inference_input_type = tf.uint8
            converter.inference_output_type = tf.uint8
            converter.optimizations = [tf.lite.Optimize.DEFAULT]

            try:
                tflite_model = converter.convert()
            except Exception as e:
                self.logger.error("Error converting model to tf lite: " + str(e))
                return

            open('../storage/' + keras_model_path.split('/')[-1].split('.')[0] + ".tflite", "wb").write(
                tflite_model)
            self.logger.info("Converted keras model " + str(keras_model_path.split('/')[-1]) + " to tf lite")

    def representative_dataset_gen(self):
        for i in range(len(self.samples)):
            data = np.array(self.samples[i: i + 1], dtype=np.float32)
            yield [data]
