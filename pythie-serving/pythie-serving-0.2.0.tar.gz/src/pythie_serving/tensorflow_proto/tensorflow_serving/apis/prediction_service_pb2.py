# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_serving/apis/prediction_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow_serving.apis import classification_pb2 as tensorflow__serving_dot_apis_dot_classification__pb2
from pythie_serving.tensorflow_proto.tensorflow_serving.apis import get_model_metadata_pb2 as tensorflow__serving_dot_apis_dot_get__model__metadata__pb2
from pythie_serving.tensorflow_proto.tensorflow_serving.apis import inference_pb2 as tensorflow__serving_dot_apis_dot_inference__pb2
from pythie_serving.tensorflow_proto.tensorflow_serving.apis import predict_pb2 as tensorflow__serving_dot_apis_dot_predict__pb2
from pythie_serving.tensorflow_proto.tensorflow_serving.apis import regression_pb2 as tensorflow__serving_dot_apis_dot_regression__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow_serving/apis/prediction_service.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_options=_b('\370\001\001'),
  serialized_pb=_b('\n0tensorflow_serving/apis/prediction_service.proto\x12\x12tensorflow.serving\x1a,tensorflow_serving/apis/classification.proto\x1a\x30tensorflow_serving/apis/get_model_metadata.proto\x1a\'tensorflow_serving/apis/inference.proto\x1a%tensorflow_serving/apis/predict.proto\x1a(tensorflow_serving/apis/regression.proto2\xfc\x03\n\x11PredictionService\x12\x61\n\x08\x43lassify\x12).tensorflow.serving.ClassificationRequest\x1a*.tensorflow.serving.ClassificationResponse\x12X\n\x07Regress\x12%.tensorflow.serving.RegressionRequest\x1a&.tensorflow.serving.RegressionResponse\x12R\n\x07Predict\x12\".tensorflow.serving.PredictRequest\x1a#.tensorflow.serving.PredictResponse\x12g\n\x0eMultiInference\x12).tensorflow.serving.MultiInferenceRequest\x1a*.tensorflow.serving.MultiInferenceResponse\x12m\n\x10GetModelMetadata\x12+.tensorflow.serving.GetModelMetadataRequest\x1a,.tensorflow.serving.GetModelMetadataResponseB\x03\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow__serving_dot_apis_dot_classification__pb2.DESCRIPTOR,tensorflow__serving_dot_apis_dot_get__model__metadata__pb2.DESCRIPTOR,tensorflow__serving_dot_apis_dot_inference__pb2.DESCRIPTOR,tensorflow__serving_dot_apis_dot_predict__pb2.DESCRIPTOR,tensorflow__serving_dot_apis_dot_regression__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_PREDICTIONSERVICE = _descriptor.ServiceDescriptor(
  name='PredictionService',
  full_name='tensorflow.serving.PredictionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=291,
  serialized_end=799,
  methods=[
  _descriptor.MethodDescriptor(
    name='Classify',
    full_name='tensorflow.serving.PredictionService.Classify',
    index=0,
    containing_service=None,
    input_type=tensorflow__serving_dot_apis_dot_classification__pb2._CLASSIFICATIONREQUEST,
    output_type=tensorflow__serving_dot_apis_dot_classification__pb2._CLASSIFICATIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Regress',
    full_name='tensorflow.serving.PredictionService.Regress',
    index=1,
    containing_service=None,
    input_type=tensorflow__serving_dot_apis_dot_regression__pb2._REGRESSIONREQUEST,
    output_type=tensorflow__serving_dot_apis_dot_regression__pb2._REGRESSIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Predict',
    full_name='tensorflow.serving.PredictionService.Predict',
    index=2,
    containing_service=None,
    input_type=tensorflow__serving_dot_apis_dot_predict__pb2._PREDICTREQUEST,
    output_type=tensorflow__serving_dot_apis_dot_predict__pb2._PREDICTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MultiInference',
    full_name='tensorflow.serving.PredictionService.MultiInference',
    index=3,
    containing_service=None,
    input_type=tensorflow__serving_dot_apis_dot_inference__pb2._MULTIINFERENCEREQUEST,
    output_type=tensorflow__serving_dot_apis_dot_inference__pb2._MULTIINFERENCERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetModelMetadata',
    full_name='tensorflow.serving.PredictionService.GetModelMetadata',
    index=4,
    containing_service=None,
    input_type=tensorflow__serving_dot_apis_dot_get__model__metadata__pb2._GETMODELMETADATAREQUEST,
    output_type=tensorflow__serving_dot_apis_dot_get__model__metadata__pb2._GETMODELMETADATARESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PREDICTIONSERVICE)

DESCRIPTOR.services_by_name['PredictionService'] = _PREDICTIONSERVICE

# @@protoc_insertion_point(module_scope)
