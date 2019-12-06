depends = ('ITKPyBase', 'ITKSmoothing', 'ITKImageSources', 'ITKImageGrid', 'ITKIOImageBase', 'ITKCommon', )
templates = (
  ('ParameterObject', 'elastix::ParameterObject', 'elastixParameterObject', False),
  ('ElastixRegistrationMethod', 'itk::ElastixRegistrationMethod', 'itkElastixRegistrationMethodIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('ElastixRegistrationMethod', 'itk::ElastixRegistrationMethod', 'itkElastixRegistrationMethodIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('TransformixFilter', 'itk::TransformixFilter', 'itkTransformixFilterIF2', True, 'itk::Image< float,2 >'),
  ('TransformixFilter', 'itk::TransformixFilter', 'itkTransformixFilterIF3', True, 'itk::Image< float,3 >'),
)
snake_case_functions = ('transformix_filter', 'elastix_registration_method', )
