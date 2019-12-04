"Main interface for rekognition service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_rekognition.type_defs import (
    DescribeProjectVersionsPaginatePaginationConfigTypeDef,
    DescribeProjectVersionsPaginateResponseTypeDef,
    DescribeProjectsPaginatePaginationConfigTypeDef,
    DescribeProjectsPaginateResponseTypeDef,
    ListCollectionsPaginatePaginationConfigTypeDef,
    ListCollectionsPaginateResponseTypeDef,
    ListFacesPaginatePaginationConfigTypeDef,
    ListFacesPaginateResponseTypeDef,
    ListStreamProcessorsPaginatePaginationConfigTypeDef,
    ListStreamProcessorsPaginateResponseTypeDef,
)


__all__ = (
    "DescribeProjectVersionsPaginator",
    "DescribeProjectsPaginator",
    "ListCollectionsPaginator",
    "ListFacesPaginator",
    "ListStreamProcessorsPaginator",
)


class DescribeProjectVersionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_project_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        PaginationConfig: DescribeProjectVersionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeProjectVersionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Rekognition.Client.describe_project_versions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DescribeProjectVersions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ProjectArn='string',
              VersionNames=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ProjectArn: string
        :param ProjectArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the project that contains the models you want to
          describe.

        :type VersionNames: list
        :param VersionNames:

          A list of model version names that you want to describe. You can add up to 10 model
          version names to the list. If you don't specify a value, all model descriptions are
          returned.

          - *(string) --*

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ProjectVersionDescriptions': [
                    {
                        'ProjectVersionArn': 'string',
                        'CreationTimestamp': datetime(2015, 1, 1),
                        'MinInferenceUnits': 123,
                        'Status':
                        'TRAINING_IN_PROGRESS'|'TRAINING_COMPLETED'
                        |'TRAINING_FAILED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'
                        |'STOPPED'|'DELETING',
                        'StatusMessage': 'string',
                        'BillableTrainingTimeInSeconds': 123,
                        'TrainingEndTimestamp': datetime(2015, 1, 1),
                        'OutputConfig': {
                            'S3Bucket': 'string',
                            'S3KeyPrefix': 'string'
                        },
                        'TrainingDataResult': {
                            'Input': {
                                'Assets': [
                                    {
                                        'GroundTruthManifest': {
                                            'S3Object': {
                                                'Bucket': 'string',
                                                'Name': 'string',
                                                'Version': 'string'
                                            }
                                        }
                                    },
                                ]
                            },
                            'Output': {
                                'Assets': [
                                    {
                                        'GroundTruthManifest': {
                                            'S3Object': {
                                                'Bucket': 'string',
                                                'Name': 'string',
                                                'Version': 'string'
                                            }
                                        }
                                    },
                                ]
                            }
                        },
                        'TestingDataResult': {
                            'Input': {
                                'Assets': [
                                    {
                                        'GroundTruthManifest': {
                                            'S3Object': {
                                                'Bucket': 'string',
                                                'Name': 'string',
                                                'Version': 'string'
                                            }
                                        }
                                    },
                                ],
                                'AutoCreate': True|False
                            },
                            'Output': {
                                'Assets': [
                                    {
                                        'GroundTruthManifest': {
                                            'S3Object': {
                                                'Bucket': 'string',
                                                'Name': 'string',
                                                'Version': 'string'
                                            }
                                        }
                                    },
                                ],
                                'AutoCreate': True|False
                            }
                        },
                        'EvaluationResult': {
                            'F1Score': ...,
                            'Summary': {
                                'S3Object': {
                                    'Bucket': 'string',
                                    'Name': 'string',
                                    'Version': 'string'
                                }
                            }
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ProjectVersionDescriptions** *(list) --*

              A list of model descriptions. The list is sorted by the creation date and time of the
              model versions, latest to earliest.

              - *(dict) --*

                The description of a version of a model.

                - **ProjectVersionArn** *(string) --*

                  The Amazon Resource Name (ARN) of the model version.

                - **CreationTimestamp** *(datetime) --*

                  The Unix datetime for the date and time that training started.

                - **MinInferenceUnits** *(integer) --*

                  The minimum number of inference units used by the model. For more information, see
                  StartProjectVersion .

                - **Status** *(string) --*

                  The current status of the model version.

                - **StatusMessage** *(string) --*

                  A descriptive message for an error or warning that occurred.

                - **BillableTrainingTimeInSeconds** *(integer) --*

                  The duration, in seconds, that the model version has been billed for training.
                  This value is only returned if the model version has been successfully trained.

                - **TrainingEndTimestamp** *(datetime) --*

                  The Unix date and time that training of the model ended.

                - **OutputConfig** *(dict) --*

                  The location where training results are saved.

                  - **S3Bucket** *(string) --*

                    The S3 bucket where training output is placed.

                  - **S3KeyPrefix** *(string) --*

                    The prefix applied to the training output files.

                - **TrainingDataResult** *(dict) --*

                  The manifest file that represents the training results.

                  - **Input** *(dict) --*

                    The training assets that you supplied for training.

                    - **Assets** *(list) --*

                      A Sagemaker GroundTruth manifest file that contains the training images
                      (assets).

                      - *(dict) --*

                        Assets are the images that you use to train and evaluate a model version.
                        Assets are referenced by Sagemaker GroundTruth manifest files.

                        - **GroundTruthManifest** *(dict) --*

                          The S3 bucket that contains the Ground Truth manifest file.

                          - **S3Object** *(dict) --*

                            Provides the S3 bucket name and object name.

                            The region for the S3 bucket containing the S3 object must match the
                            region you use for Amazon Rekognition operations.

                            For Amazon Rekognition to process an S3 object, the user must have
                            permission to access the S3 object. For more information, see
                            Resource-Based Policies in the Amazon Rekognition Developer Guide.

                            - **Bucket** *(string) --*

                              Name of the S3 bucket.

                            - **Name** *(string) --*

                              S3 object key name.

                            - **Version** *(string) --*

                              If the bucket is versioning enabled, you can specify the object
                              version.

                  - **Output** *(dict) --*

                    The images (assets) that were actually trained by Amazon Rekognition Custom
                    Labels.

                    - **Assets** *(list) --*

                      A Sagemaker GroundTruth manifest file that contains the training images
                      (assets).

                      - *(dict) --*

                        Assets are the images that you use to train and evaluate a model version.
                        Assets are referenced by Sagemaker GroundTruth manifest files.

                        - **GroundTruthManifest** *(dict) --*

                          The S3 bucket that contains the Ground Truth manifest file.

                          - **S3Object** *(dict) --*

                            Provides the S3 bucket name and object name.

                            The region for the S3 bucket containing the S3 object must match the
                            region you use for Amazon Rekognition operations.

                            For Amazon Rekognition to process an S3 object, the user must have
                            permission to access the S3 object. For more information, see
                            Resource-Based Policies in the Amazon Rekognition Developer Guide.

                            - **Bucket** *(string) --*

                              Name of the S3 bucket.

                            - **Name** *(string) --*

                              S3 object key name.

                            - **Version** *(string) --*

                              If the bucket is versioning enabled, you can specify the object
                              version.

                - **TestingDataResult** *(dict) --*

                  The manifest file that represents the testing results.

                  - **Input** *(dict) --*

                    The testing dataset that was supplied for training.

                    - **Assets** *(list) --*

                      The assets used for testing.

                      - *(dict) --*

                        Assets are the images that you use to train and evaluate a model version.
                        Assets are referenced by Sagemaker GroundTruth manifest files.

                        - **GroundTruthManifest** *(dict) --*

                          The S3 bucket that contains the Ground Truth manifest file.

                          - **S3Object** *(dict) --*

                            Provides the S3 bucket name and object name.

                            The region for the S3 bucket containing the S3 object must match the
                            region you use for Amazon Rekognition operations.

                            For Amazon Rekognition to process an S3 object, the user must have
                            permission to access the S3 object. For more information, see
                            Resource-Based Policies in the Amazon Rekognition Developer Guide.

                            - **Bucket** *(string) --*

                              Name of the S3 bucket.

                            - **Name** *(string) --*

                              S3 object key name.

                            - **Version** *(string) --*

                              If the bucket is versioning enabled, you can specify the object
                              version.

                    - **AutoCreate** *(boolean) --*

                      If specified, Amazon Rekognition Custom Labels creates a testing dataset with
                      an 80/20 split of the training dataset.

                  - **Output** *(dict) --*

                    The subset of the dataset that was actually tested. Some images (assets) might
                    not be tested due to file formatting and other issues.

                    - **Assets** *(list) --*

                      The assets used for testing.

                      - *(dict) --*

                        Assets are the images that you use to train and evaluate a model version.
                        Assets are referenced by Sagemaker GroundTruth manifest files.

                        - **GroundTruthManifest** *(dict) --*

                          The S3 bucket that contains the Ground Truth manifest file.

                          - **S3Object** *(dict) --*

                            Provides the S3 bucket name and object name.

                            The region for the S3 bucket containing the S3 object must match the
                            region you use for Amazon Rekognition operations.

                            For Amazon Rekognition to process an S3 object, the user must have
                            permission to access the S3 object. For more information, see
                            Resource-Based Policies in the Amazon Rekognition Developer Guide.

                            - **Bucket** *(string) --*

                              Name of the S3 bucket.

                            - **Name** *(string) --*

                              S3 object key name.

                            - **Version** *(string) --*

                              If the bucket is versioning enabled, you can specify the object
                              version.

                    - **AutoCreate** *(boolean) --*

                      If specified, Amazon Rekognition Custom Labels creates a testing dataset with
                      an 80/20 split of the training dataset.

                - **EvaluationResult** *(dict) --*

                  The training results. ``EvaluationResult`` is only returned if training is
                  successful.

                  - **F1Score** *(float) --*

                    The F1 score for the evaluation of all labels. The F1 score metric evaluates the
                    overall precision and recall performance of the model as a single value. A
                    higher value indicates better precision and recall performance. A lower score
                    indicates that precision, recall, or both are performing poorly.

                  - **Summary** *(dict) --*

                    The S3 bucket that contains the training summary.

                    - **S3Object** *(dict) --*

                      Provides the S3 bucket name and object name.

                      The region for the S3 bucket containing the S3 object must match the region
                      you use for Amazon Rekognition operations.

                      For Amazon Rekognition to process an S3 object, the user must have permission
                      to access the S3 object. For more information, see Resource-Based Policies in
                      the Amazon Rekognition Developer Guide.

                      - **Bucket** *(string) --*

                        Name of the S3 bucket.

                      - **Name** *(string) --*

                        S3 object key name.

                      - **Version** *(string) --*

                        If the bucket is versioning enabled, you can specify the object version.
        """


class DescribeProjectsPaginator(Boto3Paginator):
    """
    Paginator for `describe_projects`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: DescribeProjectsPaginatePaginationConfigTypeDef = None
    ) -> DescribeProjectsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Rekognition.Client.describe_projects`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DescribeProjects>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ProjectDescriptions': [
                    {
                        'ProjectArn': 'string',
                        'CreationTimestamp': datetime(2015, 1, 1),
                        'Status': 'CREATING'|'CREATED'|'DELETING'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ProjectDescriptions** *(list) --*

              A list of project descriptions. The list is sorted by the date and time the projects
              are created.

              - *(dict) --*

                A description of a Amazon Rekognition Custom Labels project.

                - **ProjectArn** *(string) --*

                  The Amazon Resource Name (ARN) of the project.

                - **CreationTimestamp** *(datetime) --*

                  The Unix timestamp for the date and time that the project was created.

                - **Status** *(string) --*

                  The current status of the project.
        """


class ListCollectionsPaginator(Boto3Paginator):
    """
    Paginator for `list_collections`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListCollectionsPaginatePaginationConfigTypeDef = None
    ) -> ListCollectionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Rekognition.Client.list_collections`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/ListCollections>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CollectionIds': [
                    'string',
                ],
                'FaceModelVersions': [
                    'string',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **CollectionIds** *(list) --*

              An array of collection IDs.

              - *(string) --*

            - **FaceModelVersions** *(list) --*

              Version numbers of the face detection models associated with the collections in the
              array ``CollectionIds`` . For example, the value of ``FaceModelVersions[2]`` is the
              version number for the face detection model used by the collection in
              ``CollectionId[2]`` .

              - *(string) --*
        """


class ListFacesPaginator(Boto3Paginator):
    """
    Paginator for `list_faces`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, CollectionId: str, PaginationConfig: ListFacesPaginatePaginationConfigTypeDef = None
    ) -> ListFacesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Rekognition.Client.list_faces`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/ListFaces>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CollectionId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CollectionId: string
        :param CollectionId: **[REQUIRED]**

          ID of the collection from which to list the faces.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Faces': [
                    {
                        'FaceId': 'string',
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'ImageId': 'string',
                        'ExternalImageId': 'string',
                        'Confidence': ...
                    },
                ],
                'FaceModelVersion': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Faces** *(list) --*

              An array of ``Face`` objects.

              - *(dict) --*

                Describes the face properties such as the bounding box, face ID, image ID of the
                input image, and external image ID that you assigned.

                - **FaceId** *(string) --*

                  Unique identifier that Amazon Rekognition assigns to the face.

                - **BoundingBox** *(dict) --*

                  Bounding box of the face.

                  - **Width** *(float) --*

                    Width of the bounding box as a ratio of the overall image width.

                  - **Height** *(float) --*

                    Height of the bounding box as a ratio of the overall image height.

                  - **Left** *(float) --*

                    Left coordinate of the bounding box as a ratio of overall image width.

                  - **Top** *(float) --*

                    Top coordinate of the bounding box as a ratio of overall image height.

                - **ImageId** *(string) --*

                  Unique identifier that Amazon Rekognition assigns to the input image.

                - **ExternalImageId** *(string) --*

                  Identifier that you assign to all the faces in the input image.

                - **Confidence** *(float) --*

                  Confidence level that the bounding box contains a face (and not a different object
                  such as a tree).

            - **FaceModelVersion** *(string) --*

              Version number of the face detection model associated with the input collection
              (``CollectionId`` ).
        """


class ListStreamProcessorsPaginator(Boto3Paginator):
    """
    Paginator for `list_stream_processors`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListStreamProcessorsPaginatePaginationConfigTypeDef = None
    ) -> ListStreamProcessorsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Rekognition.Client.list_stream_processors`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/ListStreamProcessors>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'StreamProcessors': [
                    {
                        'Name': 'string',
                        'Status': 'STOPPED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **StreamProcessors** *(list) --*

              List of stream processors that you have created.

              - *(dict) --*

                An object that recognizes faces in a streaming video. An Amazon Rekognition stream
                processor is created by a call to  CreateStreamProcessor . The request parameters
                for ``CreateStreamProcessor`` describe the Kinesis video stream source for the
                streaming video, face recognition parameters, and where to stream the analysis
                resullts.

                - **Name** *(string) --*

                  Name of the Amazon Rekognition stream processor.

                - **Status** *(string) --*

                  Current status of the Amazon Rekognition stream processor.
        """
