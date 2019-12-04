"Main interface for s3control service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from mypy_boto3.type_defs import Literal

# pylint: disable=import-self
import mypy_boto3_s3control.client as client_scope
from mypy_boto3_s3control.type_defs import (
    ClientCreateAccessPointPublicAccessBlockConfigurationTypeDef,
    ClientCreateAccessPointVpcConfigurationTypeDef,
    ClientCreateJobManifestTypeDef,
    ClientCreateJobOperationTypeDef,
    ClientCreateJobReportTypeDef,
    ClientCreateJobResponseTypeDef,
    ClientDescribeJobResponseTypeDef,
    ClientGetAccessPointPolicyResponseTypeDef,
    ClientGetAccessPointPolicyStatusResponseTypeDef,
    ClientGetAccessPointResponseTypeDef,
    ClientGetPublicAccessBlockResponseTypeDef,
    ClientListAccessPointsResponseTypeDef,
    ClientListJobsResponseTypeDef,
    ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef,
    ClientUpdateJobPriorityResponseTypeDef,
    ClientUpdateJobStatusResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_access_point(
        self,
        AccountId: str,
        Name: str,
        Bucket: str,
        VpcConfiguration: ClientCreateAccessPointVpcConfigurationTypeDef = None,
        PublicAccessBlockConfiguration: ClientCreateAccessPointPublicAccessBlockConfigurationTypeDef = None,
    ) -> None:
        """
        Creates an access point and associates it with the specified bucket.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/CreateAccessPoint>`_

        **Request Syntax**
        ::

          response = client.create_access_point(
              AccountId='string',
              Name='string',
              Bucket='string',
              VpcConfiguration={
                  'VpcId': 'string'
              },
              PublicAccessBlockConfiguration={
                  'BlockPublicAcls': True|False,
                  'IgnorePublicAcls': True|False,
                  'BlockPublicPolicy': True|False,
                  'RestrictPublicBuckets': True|False
              }
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The AWS account ID for the owner of the bucket for which you want to create an access
          point.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name you want to assign to this access point.

        :type Bucket: string
        :param Bucket: **[REQUIRED]**

          The name of the bucket that you want to associate this access point with.

        :type VpcConfiguration: dict
        :param VpcConfiguration:

          If you include this field, Amazon S3 restricts access to this access point to requests
          from the specified Virtual Private Cloud (VPC).

          - **VpcId** *(string) --* **[REQUIRED]**

            If this field is specified, this access point will only allow connections from the
            specified VPC ID.

        :type PublicAccessBlockConfiguration: dict
        :param PublicAccessBlockConfiguration:

          The ``PublicAccessBlock`` configuration that you want to apply to this Amazon S3 bucket.
          You can enable the configuration options in any combination. For more information about
          when Amazon S3 considers a bucket or object public, see `The Meaning of "Public"
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status>`__
          in the Amazon Simple Storage Service Developer Guide.

          - **BlockPublicAcls** *(boolean) --*

            Specifies whether Amazon S3 should block public access control lists (ACLs) for buckets
            in this account. Setting this element to ``TRUE`` causes the following behavior:

            * PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.

            * PUT Object calls fail if the request includes a public ACL.

            * PUT Bucket calls fail if the request includes a public ACL.

            Enabling this setting doesn't affect existing policies or ACLs.

          - **IgnorePublicAcls** *(boolean) --*

            Specifies whether Amazon S3 should ignore public ACLs for buckets in this account.
            Setting this element to ``TRUE`` causes Amazon S3 to ignore all public ACLs on buckets
            in this account and any objects that they contain.

            Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't
            prevent new public ACLs from being set.

          - **BlockPublicPolicy** *(boolean) --*

            Specifies whether Amazon S3 should block public bucket policies for buckets in this
            account. Setting this element to ``TRUE`` causes Amazon S3 to reject calls to PUT Bucket
            policy if the specified bucket policy allows public access.

            Enabling this setting doesn't affect existing bucket policies.

          - **RestrictPublicBuckets** *(boolean) --*

            Specifies whether Amazon S3 should restrict public bucket policies for buckets in this
            account. Setting this element to ``TRUE`` restricts access to buckets with public
            policies to only AWS services and authorized users within this account.

            Enabling this setting doesn't affect previously stored bucket policies, except that
            public and cross-account access within any public bucket policy, including non-public
            delegation to specific accounts, is blocked.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_job(
        self,
        AccountId: str,
        Operation: ClientCreateJobOperationTypeDef,
        Report: ClientCreateJobReportTypeDef,
        ClientRequestToken: str,
        Manifest: ClientCreateJobManifestTypeDef,
        Priority: int,
        RoleArn: str,
        ConfirmationRequired: bool = None,
        Description: str = None,
    ) -> ClientCreateJobResponseTypeDef:
        """
        Creates an Amazon S3 batch operations job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/CreateJob>`_

        **Request Syntax**
        ::

          response = client.create_job(
              AccountId='string',
              ConfirmationRequired=True|False,
              Operation={
                  'LambdaInvoke': {
                      'FunctionArn': 'string'
                  },
                  'S3PutObjectCopy': {
                      'TargetResource': 'string',
                      'CannedAccessControlList':
                      'private'|'public-read'|'public-read-write'|'aws-exec-read'
                      |'authenticated-read'|'bucket-owner-read'
                      |'bucket-owner-full-control',
                      'AccessControlGrants': [
                          {
                              'Grantee': {
                                  'TypeIdentifier': 'id'|'emailAddress'|'uri',
                                  'Identifier': 'string',
                                  'DisplayName': 'string'
                              },
                              'Permission': 'FULL_CONTROL'|'READ'|'WRITE'|'READ_ACP'|'WRITE_ACP'
                          },
                      ],
                      'MetadataDirective': 'COPY'|'REPLACE',
                      'ModifiedSinceConstraint': datetime(2015, 1, 1),
                      'NewObjectMetadata': {
                          'CacheControl': 'string',
                          'ContentDisposition': 'string',
                          'ContentEncoding': 'string',
                          'ContentLanguage': 'string',
                          'UserMetadata': {
                              'string': 'string'
                          },
                          'ContentLength': 123,
                          'ContentMD5': 'string',
                          'ContentType': 'string',
                          'HttpExpiresDate': datetime(2015, 1, 1),
                          'RequesterCharged': True|False,
                          'SSEAlgorithm': 'AES256'|'KMS'
                      },
                      'NewObjectTagging': [
                          {
                              'Key': 'string',
                              'Value': 'string'
                          },
                      ],
                      'RedirectLocation': 'string',
                      'RequesterPays': True|False,
                      'StorageClass':
                      'STANDARD'|'STANDARD_IA'|'ONEZONE_IA'|'GLACIER'
                      |'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
                      'UnModifiedSinceConstraint': datetime(2015, 1, 1),
                      'SSEAwsKmsKeyId': 'string',
                      'TargetKeyPrefix': 'string',
                      'ObjectLockLegalHoldStatus': 'OFF'|'ON',
                      'ObjectLockMode': 'COMPLIANCE'|'GOVERNANCE',
                      'ObjectLockRetainUntilDate': datetime(2015, 1, 1)
                  },
                  'S3PutObjectAcl': {
                      'AccessControlPolicy': {
                          'AccessControlList': {
                              'Owner': {
                                  'ID': 'string',
                                  'DisplayName': 'string'
                              },
                              'Grants': [
                                  {
                                      'Grantee': {
                                          'TypeIdentifier': 'id'|'emailAddress'|'uri',
                                          'Identifier': 'string',
                                          'DisplayName': 'string'
                                      },
                                      'Permission':
                                      'FULL_CONTROL'|'READ'|'WRITE'
                                      |'READ_ACP'|'WRITE_ACP'
                                  },
                              ]
                          },
                          'CannedAccessControlList':
                          'private'|'public-read'|'public-read-write'
                          |'aws-exec-read'|'authenticated-read'
                          |'bucket-owner-read'|'bucket-owner-full-control'
                      }
                  },
                  'S3PutObjectTagging': {
                      'TagSet': [
                          {
                              'Key': 'string',
                              'Value': 'string'
                          },
                      ]
                  },
                  'S3InitiateRestoreObject': {
                      'ExpirationInDays': 123,
                      'GlacierJobTier': 'BULK'|'STANDARD'
                  }
              },
              Report={
                  'Bucket': 'string',
                  'Format': 'Report_CSV_20180820',
                  'Enabled': True|False,
                  'Prefix': 'string',
                  'ReportScope': 'AllTasks'|'FailedTasksOnly'
              },
              ClientRequestToken='string',
              Manifest={
                  'Spec': {
                      'Format': 'S3BatchOperations_CSV_20180820'|'S3InventoryReport_CSV_20161130',
                      'Fields': [
                          'Ignore'|'Bucket'|'Key'|'VersionId',
                      ]
                  },
                  'Location': {
                      'ObjectArn': 'string',
                      'ObjectVersionId': 'string',
                      'ETag': 'string'
                  }
              },
              Description='string',
              Priority=123,
              RoleArn='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

        :type ConfirmationRequired: boolean
        :param ConfirmationRequired:

          Indicates whether confirmation is required before Amazon S3 runs the job. Confirmation is
          only required for jobs created through the Amazon S3 console.

        :type Operation: dict
        :param Operation: **[REQUIRED]**

          The operation that you want this job to perform on each object listed in the manifest. For
          more information about the available operations, see `Available Operations
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-operations.html>`__ in the
          *Amazon Simple Storage Service Developer Guide* .

          - **LambdaInvoke** *(dict) --*

            Directs the specified job to invoke an AWS Lambda function on each object in the
            manifest.

            - **FunctionArn** *(string) --*

              The Amazon Resource Name (ARN) for the AWS Lambda function that the specified job will
              invoke for each object in the manifest.

          - **S3PutObjectCopy** *(dict) --*

            Directs the specified job to execute a PUT Copy object call on each object in the
            manifest.

            - **TargetResource** *(string) --*

            - **CannedAccessControlList** *(string) --*

            - **AccessControlGrants** *(list) --*

              - *(dict) --*

                - **Grantee** *(dict) --*

                  - **TypeIdentifier** *(string) --*

                  - **Identifier** *(string) --*

                  - **DisplayName** *(string) --*

                - **Permission** *(string) --*

            - **MetadataDirective** *(string) --*

            - **ModifiedSinceConstraint** *(datetime) --*

            - **NewObjectMetadata** *(dict) --*

              - **CacheControl** *(string) --*

              - **ContentDisposition** *(string) --*

              - **ContentEncoding** *(string) --*

              - **ContentLanguage** *(string) --*

              - **UserMetadata** *(dict) --*

                - *(string) --*

                  - *(string) --*

              - **ContentLength** *(integer) --*

              - **ContentMD5** *(string) --*

              - **ContentType** *(string) --*

              - **HttpExpiresDate** *(datetime) --*

              - **RequesterCharged** *(boolean) --*

              - **SSEAlgorithm** *(string) --*

            - **NewObjectTagging** *(list) --*

              - *(dict) --*

                - **Key** *(string) --* **[REQUIRED]**

                - **Value** *(string) --* **[REQUIRED]**

            - **RedirectLocation** *(string) --*

            - **RequesterPays** *(boolean) --*

            - **StorageClass** *(string) --*

            - **UnModifiedSinceConstraint** *(datetime) --*

            - **SSEAwsKmsKeyId** *(string) --*

            - **TargetKeyPrefix** *(string) --*

            - **ObjectLockLegalHoldStatus** *(string) --*

            - **ObjectLockMode** *(string) --*

            - **ObjectLockRetainUntilDate** *(datetime) --*

          - **S3PutObjectAcl** *(dict) --*

            Directs the specified job to execute a PUT Object acl call on each object in the
            manifest.

            - **AccessControlPolicy** *(dict) --*

              - **AccessControlList** *(dict) --*

                - **Owner** *(dict) --* **[REQUIRED]**

                  - **ID** *(string) --*

                  - **DisplayName** *(string) --*

                - **Grants** *(list) --*

                  - *(dict) --*

                    - **Grantee** *(dict) --*

                      - **TypeIdentifier** *(string) --*

                      - **Identifier** *(string) --*

                      - **DisplayName** *(string) --*

                    - **Permission** *(string) --*

              - **CannedAccessControlList** *(string) --*

          - **S3PutObjectTagging** *(dict) --*

            Directs the specified job to execute a PUT Object tagging call on each object in the
            manifest.

            - **TagSet** *(list) --*

              - *(dict) --*

                - **Key** *(string) --* **[REQUIRED]**

                - **Value** *(string) --* **[REQUIRED]**

          - **S3InitiateRestoreObject** *(dict) --*

            Directs the specified job to execute an Initiate Glacier Restore call on each object in
            the manifest.

            - **ExpirationInDays** *(integer) --*

            - **GlacierJobTier** *(string) --*

        :type Report: dict
        :param Report: **[REQUIRED]**

          Configuration parameters for the optional job-completion report.

          - **Bucket** *(string) --*

            The Amazon Resource Name (ARN) for the bucket where specified job-completion report will
            be stored.

          - **Format** *(string) --*

            The format of the specified job-completion report.

          - **Enabled** *(boolean) --* **[REQUIRED]**

            Indicates whether the specified job will generate a job-completion report.

          - **Prefix** *(string) --*

            An optional prefix to describe where in the specified bucket the job-completion report
            will be stored. Amazon S3 will store the job-completion report at
            <prefix>/job-<job-id>/report.json.

          - **ReportScope** *(string) --*

            Indicates whether the job-completion report will include details of all tasks or only
            failed tasks.

        :type ClientRequestToken: string
        :param ClientRequestToken: **[REQUIRED]**

          An idempotency token to ensure that you don't accidentally submit the same request twice.
          You can use any string up to the maximum length.

          This field is autopopulated if not provided.

        :type Manifest: dict
        :param Manifest: **[REQUIRED]**

          Configuration parameters for the manifest.

          - **Spec** *(dict) --* **[REQUIRED]**

            Describes the format of the specified job's manifest. If the manifest is in CSV format,
            also describes the columns contained within the manifest.

            - **Format** *(string) --* **[REQUIRED]**

              Indicates which of the available formats the specified manifest uses.

            - **Fields** *(list) --*

              If the specified manifest object is in the ``S3BatchOperations_CSV_20180820`` format,
              this element describes which columns contain the required data.

              - *(string) --*

          - **Location** *(dict) --* **[REQUIRED]**

            Contains the information required to locate the specified job's manifest.

            - **ObjectArn** *(string) --* **[REQUIRED]**

              The Amazon Resource Name (ARN) for a manifest object.

            - **ObjectVersionId** *(string) --*

              The optional version ID to identify a specific version of the manifest object.

            - **ETag** *(string) --* **[REQUIRED]**

              The ETag for the specified manifest object.

        :type Description: string
        :param Description:

          A description for this job. You can use any string within the permitted length.
          Descriptions don't need to be unique and can be used for multiple jobs.

        :type Priority: integer
        :param Priority: **[REQUIRED]**

          The numerical priority for this job. Higher numbers indicate higher priority.

        :type RoleArn: string
        :param RoleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) for the Identity and Access Management (IAM) Role that
          batch operations will use to execute this job's operation on each object in the manifest.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The ID for this job. Amazon S3 generates this ID automatically and returns it after a
              successful ``Create Job`` request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_access_point(self, AccountId: str, Name: str) -> None:
        """
        Deletes the specified access point.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/DeleteAccessPoint>`_

        **Request Syntax**
        ::

          response = client.delete_access_point(
              AccountId='string',
              Name='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The account ID for the account that owns the specified access point.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the access point you want to delete.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_access_point_policy(self, AccountId: str, Name: str) -> None:
        """
        Deletes the access point policy for the specified access point.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/DeleteAccessPointPolicy>`_

        **Request Syntax**
        ::

          response = client.delete_access_point_policy(
              AccountId='string',
              Name='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The account ID for the account that owns the specified access point.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the access point whose policy you want to delete.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_public_access_block(self, AccountId: str) -> None:
        """
        Removes the ``PublicAccessBlock`` configuration for an Amazon Web Services account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/DeletePublicAccessBlock>`_

        **Request Syntax**
        ::

          response = client.delete_public_access_block(
              AccountId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The account ID for the Amazon Web Services account whose ``PublicAccessBlock``
          configuration you want to remove.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_job(self, AccountId: str, JobId: str) -> ClientDescribeJobResponseTypeDef:
        """
        Retrieves the configuration parameters and status for a batch operations job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/DescribeJob>`_

        **Request Syntax**
        ::

          response = client.describe_job(
              AccountId='string',
              JobId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

        :type JobId: string
        :param JobId: **[REQUIRED]**

          The ID for the job whose information you want to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Job': {
                    'JobId': 'string',
                    'ConfirmationRequired': True|False,
                    'Description': 'string',
                    'JobArn': 'string',
                    'Status':
                    'Active'|'Cancelled'|'Cancelling'|'Complete'|'Completing'|'Failed'
                    |'Failing'|'New'|'Paused'|'Pausing'|'Preparing'|'Ready'|'Suspended',
                    'Manifest': {
                        'Spec': {
                            'Format':
                            'S3BatchOperations_CSV_20180820'
                            |'S3InventoryReport_CSV_20161130',
                            'Fields': [
                                'Ignore'|'Bucket'|'Key'|'VersionId',
                            ]
                        },
                        'Location': {
                            'ObjectArn': 'string',
                            'ObjectVersionId': 'string',
                            'ETag': 'string'
                        }
                    },
                    'Operation': {
                        'LambdaInvoke': {
                            'FunctionArn': 'string'
                        },
                        'S3PutObjectCopy': {
                            'TargetResource': 'string',
                            'CannedAccessControlList':
                            'private'|'public-read'|'public-read-write'
                            |'aws-exec-read'|'authenticated-read'
                            |'bucket-owner-read'|'bucket-owner-full-control',
                            'AccessControlGrants': [
                                {
                                    'Grantee': {
                                        'TypeIdentifier': 'id'|'emailAddress'|'uri',
                                        'Identifier': 'string',
                                        'DisplayName': 'string'
                                    },
                                    'Permission':
                                    'FULL_CONTROL'|'READ'|'WRITE'
                                    |'READ_ACP'|'WRITE_ACP'
                                },
                            ],
                            'MetadataDirective': 'COPY'|'REPLACE',
                            'ModifiedSinceConstraint': datetime(2015, 1, 1),
                            'NewObjectMetadata': {
                                'CacheControl': 'string',
                                'ContentDisposition': 'string',
                                'ContentEncoding': 'string',
                                'ContentLanguage': 'string',
                                'UserMetadata': {
                                    'string': 'string'
                                },
                                'ContentLength': 123,
                                'ContentMD5': 'string',
                                'ContentType': 'string',
                                'HttpExpiresDate': datetime(2015, 1, 1),
                                'RequesterCharged': True|False,
                                'SSEAlgorithm': 'AES256'|'KMS'
                            },
                            'NewObjectTagging': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ],
                            'RedirectLocation': 'string',
                            'RequesterPays': True|False,
                            'StorageClass':
                            'STANDARD'|'STANDARD_IA'|'ONEZONE_IA'|'GLACIER'
                            |'INTELLIGENT_TIERING'|'DEEP_ARCHIVE',
                            'UnModifiedSinceConstraint': datetime(2015, 1, 1),
                            'SSEAwsKmsKeyId': 'string',
                            'TargetKeyPrefix': 'string',
                            'ObjectLockLegalHoldStatus': 'OFF'|'ON',
                            'ObjectLockMode': 'COMPLIANCE'|'GOVERNANCE',
                            'ObjectLockRetainUntilDate': datetime(2015, 1, 1)
                        },
                        'S3PutObjectAcl': {
                            'AccessControlPolicy': {
                                'AccessControlList': {
                                    'Owner': {
                                        'ID': 'string',
                                        'DisplayName': 'string'
                                    },
                                    'Grants': [
                                        {
                                            'Grantee': {
                                                'TypeIdentifier': 'id'|'emailAddress'|'uri',
                                                'Identifier': 'string',
                                                'DisplayName': 'string'
                                            },
                                            'Permission':
                                            'FULL_CONTROL'
                                            |'READ'|'WRITE'
                                            |'READ_ACP'
                                            |'WRITE_ACP'
                                        },
                                    ]
                                },
                                'CannedAccessControlList':
                                'private'|'public-read'|'public-read-write'
                                |'aws-exec-read'|'authenticated-read'
                                |'bucket-owner-read'
                                |'bucket-owner-full-control'
                            }
                        },
                        'S3PutObjectTagging': {
                            'TagSet': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        },
                        'S3InitiateRestoreObject': {
                            'ExpirationInDays': 123,
                            'GlacierJobTier': 'BULK'|'STANDARD'
                        }
                    },
                    'Priority': 123,
                    'ProgressSummary': {
                        'TotalNumberOfTasks': 123,
                        'NumberOfTasksSucceeded': 123,
                        'NumberOfTasksFailed': 123
                    },
                    'StatusUpdateReason': 'string',
                    'FailureReasons': [
                        {
                            'FailureCode': 'string',
                            'FailureReason': 'string'
                        },
                    ],
                    'Report': {
                        'Bucket': 'string',
                        'Format': 'Report_CSV_20180820',
                        'Enabled': True|False,
                        'Prefix': 'string',
                        'ReportScope': 'AllTasks'|'FailedTasksOnly'
                    },
                    'CreationTime': datetime(2015, 1, 1),
                    'TerminationDate': datetime(2015, 1, 1),
                    'RoleArn': 'string',
                    'SuspendedDate': datetime(2015, 1, 1),
                    'SuspendedCause': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Job** *(dict) --*

              Contains the configuration parameters and status for the job specified in the
              ``Describe Job`` request.

              - **JobId** *(string) --*

                The ID for the specified job.

              - **ConfirmationRequired** *(boolean) --*

                Indicates whether confirmation is required before Amazon S3 begins running the
                specified job. Confirmation is required only for jobs created through the Amazon S3
                console.

              - **Description** *(string) --*

                The description for this job, if one was provided in this job's ``Create Job``
                request.

              - **JobArn** *(string) --*

                The Amazon Resource Name (ARN) for this job.

              - **Status** *(string) --*

                The current status of the specified job.

              - **Manifest** *(dict) --*

                The configuration information for the specified job's manifest object.

                - **Spec** *(dict) --*

                  Describes the format of the specified job's manifest. If the manifest is in CSV
                  format, also describes the columns contained within the manifest.

                  - **Format** *(string) --*

                    Indicates which of the available formats the specified manifest uses.

                  - **Fields** *(list) --*

                    If the specified manifest object is in the ``S3BatchOperations_CSV_20180820``
                    format, this element describes which columns contain the required data.

                    - *(string) --*

                - **Location** *(dict) --*

                  Contains the information required to locate the specified job's manifest.

                  - **ObjectArn** *(string) --*

                    The Amazon Resource Name (ARN) for a manifest object.

                  - **ObjectVersionId** *(string) --*

                    The optional version ID to identify a specific version of the manifest object.

                  - **ETag** *(string) --*

                    The ETag for the specified manifest object.

              - **Operation** *(dict) --*

                The operation that the specified job is configured to execute on the objects listed
                in the manifest.

                - **LambdaInvoke** *(dict) --*

                  Directs the specified job to invoke an AWS Lambda function on each object in the
                  manifest.

                  - **FunctionArn** *(string) --*

                    The Amazon Resource Name (ARN) for the AWS Lambda function that the specified
                    job will invoke for each object in the manifest.

                - **S3PutObjectCopy** *(dict) --*

                  Directs the specified job to execute a PUT Copy object call on each object in the
                  manifest.

                  - **TargetResource** *(string) --*

                  - **CannedAccessControlList** *(string) --*

                  - **AccessControlGrants** *(list) --*

                    - *(dict) --*

                      - **Grantee** *(dict) --*

                        - **TypeIdentifier** *(string) --*

                        - **Identifier** *(string) --*

                        - **DisplayName** *(string) --*

                      - **Permission** *(string) --*

                  - **MetadataDirective** *(string) --*

                  - **ModifiedSinceConstraint** *(datetime) --*

                  - **NewObjectMetadata** *(dict) --*

                    - **CacheControl** *(string) --*

                    - **ContentDisposition** *(string) --*

                    - **ContentEncoding** *(string) --*

                    - **ContentLanguage** *(string) --*

                    - **UserMetadata** *(dict) --*

                      - *(string) --*

                        - *(string) --*

                    - **ContentLength** *(integer) --*

                    - **ContentMD5** *(string) --*

                    - **ContentType** *(string) --*

                    - **HttpExpiresDate** *(datetime) --*

                    - **RequesterCharged** *(boolean) --*

                    - **SSEAlgorithm** *(string) --*

                  - **NewObjectTagging** *(list) --*

                    - *(dict) --*

                      - **Key** *(string) --*

                      - **Value** *(string) --*

                  - **RedirectLocation** *(string) --*

                  - **RequesterPays** *(boolean) --*

                  - **StorageClass** *(string) --*

                  - **UnModifiedSinceConstraint** *(datetime) --*

                  - **SSEAwsKmsKeyId** *(string) --*

                  - **TargetKeyPrefix** *(string) --*

                  - **ObjectLockLegalHoldStatus** *(string) --*

                  - **ObjectLockMode** *(string) --*

                  - **ObjectLockRetainUntilDate** *(datetime) --*

                - **S3PutObjectAcl** *(dict) --*

                  Directs the specified job to execute a PUT Object acl call on each object in the
                  manifest.

                  - **AccessControlPolicy** *(dict) --*

                    - **AccessControlList** *(dict) --*

                      - **Owner** *(dict) --*

                        - **ID** *(string) --*

                        - **DisplayName** *(string) --*

                      - **Grants** *(list) --*

                        - *(dict) --*

                          - **Grantee** *(dict) --*

                            - **TypeIdentifier** *(string) --*

                            - **Identifier** *(string) --*

                            - **DisplayName** *(string) --*

                          - **Permission** *(string) --*

                    - **CannedAccessControlList** *(string) --*

                - **S3PutObjectTagging** *(dict) --*

                  Directs the specified job to execute a PUT Object tagging call on each object in
                  the manifest.

                  - **TagSet** *(list) --*

                    - *(dict) --*

                      - **Key** *(string) --*

                      - **Value** *(string) --*

                - **S3InitiateRestoreObject** *(dict) --*

                  Directs the specified job to execute an Initiate Glacier Restore call on each
                  object in the manifest.

                  - **ExpirationInDays** *(integer) --*

                  - **GlacierJobTier** *(string) --*

              - **Priority** *(integer) --*

                The priority of the specified job.

              - **ProgressSummary** *(dict) --*

                Describes the total number of tasks that the specified job has executed, the number
                of tasks that succeeded, and the number of tasks that failed.

                - **TotalNumberOfTasks** *(integer) --*

                - **NumberOfTasksSucceeded** *(integer) --*

                - **NumberOfTasksFailed** *(integer) --*

              - **StatusUpdateReason** *(string) --*

              - **FailureReasons** *(list) --*

                If the specified job failed, this field contains information describing the failure.

                - *(dict) --*

                  If this job failed, this element indicates why the job failed.

                  - **FailureCode** *(string) --*

                    The failure code, if any, for the specified job.

                  - **FailureReason** *(string) --*

                    The failure reason, if any, for the specified job.

              - **Report** *(dict) --*

                Contains the configuration information for the job-completion report if you
                requested one in the ``Create Job`` request.

                - **Bucket** *(string) --*

                  The Amazon Resource Name (ARN) for the bucket where specified job-completion
                  report will be stored.

                - **Format** *(string) --*

                  The format of the specified job-completion report.

                - **Enabled** *(boolean) --*

                  Indicates whether the specified job will generate a job-completion report.

                - **Prefix** *(string) --*

                  An optional prefix to describe where in the specified bucket the job-completion
                  report will be stored. Amazon S3 will store the job-completion report at
                  <prefix>/job-<job-id>/report.json.

                - **ReportScope** *(string) --*

                  Indicates whether the job-completion report will include details of all tasks or
                  only failed tasks.

              - **CreationTime** *(datetime) --*

                A timestamp indicating when this job was created.

              - **TerminationDate** *(datetime) --*

                A timestamp indicating when this job terminated. A job's termination date is the
                date and time when it succeeded, failed, or was canceled.

              - **RoleArn** *(string) --*

                The Amazon Resource Name (ARN) for the Identity and Access Management (IAM) Role
                assigned to execute the tasks for this job.

              - **SuspendedDate** *(datetime) --*

                The timestamp when this job was suspended, if it has been suspended.

              - **SuspendedCause** *(string) --*

                The reason why the specified job was suspended. A job is only suspended if you
                create it through the Amazon S3 console. When you create the job, it enters the
                ``Suspended`` state to await confirmation before running. After you confirm the job,
                it automatically exits the ``Suspended`` state.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_access_point(self, AccountId: str, Name: str) -> ClientGetAccessPointResponseTypeDef:
        """
        Returns configuration information about the specified access point.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/GetAccessPoint>`_

        **Request Syntax**
        ::

          response = client.get_access_point(
              AccountId='string',
              Name='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The account ID for the account that owns the specified access point.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the access point whose configuration information you want to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Name': 'string',
                'Bucket': 'string',
                'NetworkOrigin': 'Internet'|'VPC',
                'VpcConfiguration': {
                    'VpcId': 'string'
                },
                'PublicAccessBlockConfiguration': {
                    'BlockPublicAcls': True|False,
                    'IgnorePublicAcls': True|False,
                    'BlockPublicPolicy': True|False,
                    'RestrictPublicBuckets': True|False
                },
                'CreationDate': datetime(2015, 1, 1)
            }
          **Response Structure**

          - *(dict) --*

            - **Name** *(string) --*

              The name of the specified access point.

            - **Bucket** *(string) --*

              The name of the bucket associated with the specified access point.

            - **NetworkOrigin** *(string) --*

              Indicates whether this access point allows access from the public Internet. If
              ``VpcConfiguration`` is specified for this access point, then ``NetworkOrigin`` is
              ``VPC`` , and the access point doesn't allow access from the public Internet.
              Otherwise, ``NetworkOrigin`` is ``Internet`` , and the access point allows access from
              the public Internet, subject to the access point and bucket access policies.

            - **VpcConfiguration** *(dict) --*

              Contains the Virtual Private Cloud (VPC) configuration for the specified access point.

              - **VpcId** *(string) --*

                If this field is specified, this access point will only allow connections from the
                specified VPC ID.

            - **PublicAccessBlockConfiguration** *(dict) --*

              The ``PublicAccessBlock`` configuration that you want to apply to this Amazon S3
              bucket. You can enable the configuration options in any combination. For more
              information about when Amazon S3 considers a bucket or object public, see `The Meaning
              of "Public"
              <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status>`__
              in the Amazon Simple Storage Service Developer Guide.

              - **BlockPublicAcls** *(boolean) --*

                Specifies whether Amazon S3 should block public access control lists (ACLs) for
                buckets in this account. Setting this element to ``TRUE`` causes the following
                behavior:

                * PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.

                * PUT Object calls fail if the request includes a public ACL.

                * PUT Bucket calls fail if the request includes a public ACL.

                Enabling this setting doesn't affect existing policies or ACLs.

              - **IgnorePublicAcls** *(boolean) --*

                Specifies whether Amazon S3 should ignore public ACLs for buckets in this account.
                Setting this element to ``TRUE`` causes Amazon S3 to ignore all public ACLs on
                buckets in this account and any objects that they contain.

                Enabling this setting doesn't affect the persistence of any existing ACLs and
                doesn't prevent new public ACLs from being set.

              - **BlockPublicPolicy** *(boolean) --*

                Specifies whether Amazon S3 should block public bucket policies for buckets in this
                account. Setting this element to ``TRUE`` causes Amazon S3 to reject calls to PUT
                Bucket policy if the specified bucket policy allows public access.

                Enabling this setting doesn't affect existing bucket policies.

              - **RestrictPublicBuckets** *(boolean) --*

                Specifies whether Amazon S3 should restrict public bucket policies for buckets in
                this account. Setting this element to ``TRUE`` restricts access to buckets with
                public policies to only AWS services and authorized users within this account.

                Enabling this setting doesn't affect previously stored bucket policies, except that
                public and cross-account access within any public bucket policy, including
                non-public delegation to specific accounts, is blocked.

            - **CreationDate** *(datetime) --*

              The date and time when the specified access point was created.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_access_point_policy(
        self, AccountId: str, Name: str
    ) -> ClientGetAccessPointPolicyResponseTypeDef:
        """
        Returns the access point policy associated with the specified access point.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/GetAccessPointPolicy>`_

        **Request Syntax**
        ::

          response = client.get_access_point_policy(
              AccountId='string',
              Name='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The account ID for the account that owns the specified access point.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the access point whose policy you want to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Policy': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Policy** *(string) --*

              The access point policy associated with the specified access point.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_access_point_policy_status(
        self, AccountId: str, Name: str
    ) -> ClientGetAccessPointPolicyStatusResponseTypeDef:
        """
        Indicates whether the specified access point currently has a policy that allows public
        access. For more information about public access through access points, see `Managing Data
        Access with Amazon S3 Access Points
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-points.html>`__ in the *Amazon
        Simple Storage Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/GetAccessPointPolicyStatus>`_

        **Request Syntax**
        ::

          response = client.get_access_point_policy_status(
              AccountId='string',
              Name='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The account ID for the account that owns the specified access point.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the access point whose policy status you want to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PolicyStatus': {
                    'IsPublic': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **PolicyStatus** *(dict) --*

              Indicates the current policy status of the specified access point.

              - **IsPublic** *(boolean) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_public_access_block(self, AccountId: str) -> ClientGetPublicAccessBlockResponseTypeDef:
        """
        Retrieves the ``PublicAccessBlock`` configuration for an Amazon Web Services account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/GetPublicAccessBlock>`_

        **Request Syntax**
        ::

          response = client.get_public_access_block(
              AccountId='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The account ID for the Amazon Web Services account whose ``PublicAccessBlock``
          configuration you want to retrieve.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PublicAccessBlockConfiguration': {
                    'BlockPublicAcls': True|False,
                    'IgnorePublicAcls': True|False,
                    'BlockPublicPolicy': True|False,
                    'RestrictPublicBuckets': True|False
                }
            }
          **Response Structure**

          - *(dict) --*

            - **PublicAccessBlockConfiguration** *(dict) --*

              The ``PublicAccessBlock`` configuration currently in effect for this Amazon Web
              Services account.

              - **BlockPublicAcls** *(boolean) --*

                Specifies whether Amazon S3 should block public access control lists (ACLs) for
                buckets in this account. Setting this element to ``TRUE`` causes the following
                behavior:

                * PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.

                * PUT Object calls fail if the request includes a public ACL.

                * PUT Bucket calls fail if the request includes a public ACL.

                Enabling this setting doesn't affect existing policies or ACLs.

              - **IgnorePublicAcls** *(boolean) --*

                Specifies whether Amazon S3 should ignore public ACLs for buckets in this account.
                Setting this element to ``TRUE`` causes Amazon S3 to ignore all public ACLs on
                buckets in this account and any objects that they contain.

                Enabling this setting doesn't affect the persistence of any existing ACLs and
                doesn't prevent new public ACLs from being set.

              - **BlockPublicPolicy** *(boolean) --*

                Specifies whether Amazon S3 should block public bucket policies for buckets in this
                account. Setting this element to ``TRUE`` causes Amazon S3 to reject calls to PUT
                Bucket policy if the specified bucket policy allows public access.

                Enabling this setting doesn't affect existing bucket policies.

              - **RestrictPublicBuckets** *(boolean) --*

                Specifies whether Amazon S3 should restrict public bucket policies for buckets in
                this account. Setting this element to ``TRUE`` restricts access to buckets with
                public policies to only AWS services and authorized users within this account.

                Enabling this setting doesn't affect previously stored bucket policies, except that
                public and cross-account access within any public bucket policy, including
                non-public delegation to specific accounts, is blocked.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_access_points(
        self, AccountId: str, Bucket: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ClientListAccessPointsResponseTypeDef:
        """
        Returns a list of the access points currently associated with the specified bucket. You can
        retrieve up to 1000 access points per call. If the specified bucket has more than 1000
        access points (or the number specified in ``maxResults`` , whichever is less), then the
        response will include a continuation token that you can use to list the additional access
        points.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/ListAccessPoints>`_

        **Request Syntax**
        ::

          response = client.list_access_points(
              AccountId='string',
              Bucket='string',
              NextToken='string',
              MaxResults=123
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The AWS account ID for owner of the bucket whose access points you want to list.

        :type Bucket: string
        :param Bucket:

          The name of the bucket whose associated access points you want to list.

        :type NextToken: string
        :param NextToken:

          A continuation token. If a previous call to ``ListAccessPoints`` returned a continuation
          token in the ``NextToken`` field, then providing that value here causes Amazon S3 to
          retrieve the next page of results.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of access points that you want to include in the list. If the specified
          bucket has more than this number of access points, then the response will include a
          continuation token in the ``NextToken`` field that you can use to retrieve the next page
          of access points.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AccessPointList': [
                    {
                        'Name': 'string',
                        'NetworkOrigin': 'Internet'|'VPC',
                        'VpcConfiguration': {
                            'VpcId': 'string'
                        },
                        'Bucket': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **AccessPointList** *(list) --*

              Contains identification and configuration information for one or more access points
              associated with the specified bucket.

              - *(dict) --*

                An access point used to access a bucket.

                - **Name** *(string) --*

                  The name of this access point.

                - **NetworkOrigin** *(string) --*

                  Indicates whether this access point allows access from the public Internet. If
                  ``VpcConfiguration`` is specified for this access point, then ``NetworkOrigin`` is
                  ``VPC`` , and the access point doesn't allow access from the public Internet.
                  Otherwise, ``NetworkOrigin`` is ``Internet`` , and the access point allows access
                  from the public Internet, subject to the access point and bucket access policies.

                - **VpcConfiguration** *(dict) --*

                  The Virtual Private Cloud (VPC) configuration for this access point, if one
                  exists.

                  - **VpcId** *(string) --*

                    If this field is specified, this access point will only allow connections from
                    the specified VPC ID.

                - **Bucket** *(string) --*

                  The name of the bucket associated with this access point.

            - **NextToken** *(string) --*

              If the specified bucket has more access points than can be returned in one call to
              this API, then this field contains a continuation token that you can provide in
              subsequent calls to this API to retrieve additional access points.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_jobs(
        self,
        AccountId: str,
        JobStatuses: List[
            Literal[
                "Active",
                "Cancelled",
                "Cancelling",
                "Complete",
                "Completing",
                "Failed",
                "Failing",
                "New",
                "Paused",
                "Pausing",
                "Preparing",
                "Ready",
                "Suspended",
            ]
        ] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ClientListJobsResponseTypeDef:
        """
        Lists current jobs and jobs that have ended within the last 30 days for the AWS account
        making the request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/ListJobs>`_

        **Request Syntax**
        ::

          response = client.list_jobs(
              AccountId='string',
              JobStatuses=[
                  'Active'|'Cancelled'|'Cancelling'|'Complete'|'Completing'|'Failed'|'Failing'|'New'
                  |'Paused'|'Pausing'|'Preparing'|'Ready'|'Suspended',
              ],
              NextToken='string',
              MaxResults=123
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

        :type JobStatuses: list
        :param JobStatuses:

          The ``List Jobs`` request returns jobs that match the statuses listed in this element.

          - *(string) --*

        :type NextToken: string
        :param NextToken:

          A pagination token to request the next page of results. Use the token that Amazon S3
          returned in the ``NextToken`` element of the ``ListJobsResult`` from the previous ``List
          Jobs`` request.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of jobs that Amazon S3 will include in the ``List Jobs`` response. If
          there are more jobs than this number, the response will include a pagination token in the
          ``NextToken`` field to enable you to retrieve the next page of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'Jobs': [
                    {
                        'JobId': 'string',
                        'Description': 'string',
                        'Operation':
                        'LambdaInvoke'|'S3PutObjectCopy'|'S3PutObjectAcl'
                        |'S3PutObjectTagging'|'S3InitiateRestoreObject',
                        'Priority': 123,
                        'Status':
                        'Active'|'Cancelled'|'Cancelling'|'Complete'|'Completing'
                        |'Failed'|'Failing'|'New'|'Paused'|'Pausing'|'Preparing'
                        |'Ready'|'Suspended',
                        'CreationTime': datetime(2015, 1, 1),
                        'TerminationDate': datetime(2015, 1, 1),
                        'ProgressSummary': {
                            'TotalNumberOfTasks': 123,
                            'NumberOfTasksSucceeded': 123,
                            'NumberOfTasksFailed': 123
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --*

              If the ``List Jobs`` request produced more than the maximum number of results, you can
              pass this value into a subsequent ``List Jobs`` request in order to retrieve the next
              page of results.

            - **Jobs** *(list) --*

              The list of current jobs and jobs that have ended within the last 30 days.

              - *(dict) --*

                Contains the configuration and status information for a single job retrieved as part
                of a job list.

                - **JobId** *(string) --*

                  The ID for the specified job.

                - **Description** *(string) --*

                  The user-specified description that was included in the specified job's ``Create
                  Job`` request.

                - **Operation** *(string) --*

                  The operation that the specified job is configured to run on each object listed in
                  the manifest.

                - **Priority** *(integer) --*

                  The current priority for the specified job.

                - **Status** *(string) --*

                  The specified job's current status.

                - **CreationTime** *(datetime) --*

                  A timestamp indicating when the specified job was created.

                - **TerminationDate** *(datetime) --*

                  A timestamp indicating when the specified job terminated. A job's termination date
                  is the date and time when it succeeded, failed, or was canceled.

                - **ProgressSummary** *(dict) --*

                  Describes the total number of tasks that the specified job has executed, the
                  number of tasks that succeeded, and the number of tasks that failed.

                  - **TotalNumberOfTasks** *(integer) --*

                  - **NumberOfTasksSucceeded** *(integer) --*

                  - **NumberOfTasksFailed** *(integer) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_access_point_policy(self, AccountId: str, Name: str, Policy: str) -> None:
        """
        Associates an access policy with the specified access point. Each access point can have only
        one policy, so a request made to this API replaces any existing policy associated with the
        specified access point.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/PutAccessPointPolicy>`_

        **Request Syntax**
        ::

          response = client.put_access_point_policy(
              AccountId='string',
              Name='string',
              Policy='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The AWS account ID for owner of the bucket associated with the specified access point.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the access point that you want to associate with the specified policy.

        :type Policy: string
        :param Policy: **[REQUIRED]**

          The policy that you want to apply to the specified access point. For more information
          about access point policies, see `Managing Data Access with Amazon S3 Access Points
          <https://docs.aws.amazon.com/AmazonS3/latest/dev/access-points.html>`__ in the *Amazon
          Simple Storage Service Developer Guide* .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_public_access_block(
        self,
        PublicAccessBlockConfiguration: ClientPutPublicAccessBlockPublicAccessBlockConfigurationTypeDef,
        AccountId: str,
    ) -> None:
        """
        Creates or modifies the ``PublicAccessBlock`` configuration for an Amazon Web Services
        account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/PutPublicAccessBlock>`_

        **Request Syntax**
        ::

          response = client.put_public_access_block(
              PublicAccessBlockConfiguration={
                  'BlockPublicAcls': True|False,
                  'IgnorePublicAcls': True|False,
                  'BlockPublicPolicy': True|False,
                  'RestrictPublicBuckets': True|False
              },
              AccountId='string'
          )
        :type PublicAccessBlockConfiguration: dict
        :param PublicAccessBlockConfiguration: **[REQUIRED]**

          The ``PublicAccessBlock`` configuration that you want to apply to the specified Amazon Web
          Services account.

          - **BlockPublicAcls** *(boolean) --*

            Specifies whether Amazon S3 should block public access control lists (ACLs) for buckets
            in this account. Setting this element to ``TRUE`` causes the following behavior:

            * PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.

            * PUT Object calls fail if the request includes a public ACL.

            * PUT Bucket calls fail if the request includes a public ACL.

            Enabling this setting doesn't affect existing policies or ACLs.

          - **IgnorePublicAcls** *(boolean) --*

            Specifies whether Amazon S3 should ignore public ACLs for buckets in this account.
            Setting this element to ``TRUE`` causes Amazon S3 to ignore all public ACLs on buckets
            in this account and any objects that they contain.

            Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't
            prevent new public ACLs from being set.

          - **BlockPublicPolicy** *(boolean) --*

            Specifies whether Amazon S3 should block public bucket policies for buckets in this
            account. Setting this element to ``TRUE`` causes Amazon S3 to reject calls to PUT Bucket
            policy if the specified bucket policy allows public access.

            Enabling this setting doesn't affect existing bucket policies.

          - **RestrictPublicBuckets** *(boolean) --*

            Specifies whether Amazon S3 should restrict public bucket policies for buckets in this
            account. Setting this element to ``TRUE`` restricts access to buckets with public
            policies to only AWS services and authorized users within this account.

            Enabling this setting doesn't affect previously stored bucket policies, except that
            public and cross-account access within any public bucket policy, including non-public
            delegation to specific accounts, is blocked.

        :type AccountId: string
        :param AccountId: **[REQUIRED]**

          The account ID for the Amazon Web Services account whose ``PublicAccessBlock``
          configuration you want to set.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_job_priority(
        self, AccountId: str, JobId: str, Priority: int
    ) -> ClientUpdateJobPriorityResponseTypeDef:
        """
        Updates an existing job's priority.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/UpdateJobPriority>`_

        **Request Syntax**
        ::

          response = client.update_job_priority(
              AccountId='string',
              JobId='string',
              Priority=123
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

        :type JobId: string
        :param JobId: **[REQUIRED]**

          The ID for the job whose priority you want to update.

        :type Priority: integer
        :param Priority: **[REQUIRED]**

          The priority you want to assign to this job.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string',
                'Priority': 123
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The ID for the job whose priority Amazon S3 updated.

            - **Priority** *(integer) --*

              The new priority assigned to the specified job.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_job_status(
        self,
        AccountId: str,
        JobId: str,
        RequestedJobStatus: Literal["Cancelled", "Ready"],
        StatusUpdateReason: str = None,
    ) -> ClientUpdateJobStatusResponseTypeDef:
        """
        Updates the status for the specified job. Use this operation to confirm that you want to run
        a job or to cancel an existing job.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/UpdateJobStatus>`_

        **Request Syntax**
        ::

          response = client.update_job_status(
              AccountId='string',
              JobId='string',
              RequestedJobStatus='Cancelled'|'Ready',
              StatusUpdateReason='string'
          )
        :type AccountId: string
        :param AccountId: **[REQUIRED]**

        :type JobId: string
        :param JobId: **[REQUIRED]**

          The ID of the job whose status you want to update.

        :type RequestedJobStatus: string
        :param RequestedJobStatus: **[REQUIRED]**

          The status that you want to move the specified job to.

        :type StatusUpdateReason: string
        :param StatusUpdateReason:

          A description of the reason why you want to change the specified job's status. This field
          can be any string up to the maximum length.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'JobId': 'string',
                'Status':
                'Active'|'Cancelled'|'Cancelling'|'Complete'|'Completing'|'Failed'|'Failing'
                |'New'|'Paused'|'Pausing'|'Preparing'|'Ready'|'Suspended',
                'StatusUpdateReason': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **JobId** *(string) --*

              The ID for the job whose status was updated.

            - **Status** *(string) --*

              The current status for the specified job.

            - **StatusUpdateReason** *(string) --*

              The reason that the specified job's status was updated.
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    IdempotencyException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidRequestException: Boto3ClientError
    JobStatusException: Boto3ClientError
    NoSuchPublicAccessBlockConfiguration: Boto3ClientError
    NotFoundException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
