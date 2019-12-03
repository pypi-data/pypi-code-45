"Main interface for importexport service type defs"
from __future__ import annotations

from datetime import datetime
from typing import List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientCancelJobResponseTypeDef",
    "ClientCreateJobResponseArtifactListTypeDef",
    "ClientCreateJobResponseTypeDef",
    "ClientGetShippingLabelResponseTypeDef",
    "ClientGetStatusResponseArtifactListTypeDef",
    "ClientGetStatusResponseTypeDef",
    "ClientListJobsResponseJobsTypeDef",
    "ClientListJobsResponseTypeDef",
    "ClientUpdateJobResponseArtifactListTypeDef",
    "ClientUpdateJobResponseTypeDef",
    "ListJobsPaginatePaginationConfigTypeDef",
    "ListJobsPaginateResponseJobsTypeDef",
    "ListJobsPaginateResponseTypeDef",
)


_ClientCancelJobResponseTypeDef = TypedDict(
    "_ClientCancelJobResponseTypeDef", {"Success": bool}, total=False
)


class ClientCancelJobResponseTypeDef(_ClientCancelJobResponseTypeDef):
    """
    - *(dict) --*Output structure for the CancelJob operation.

      - **Success** *(boolean) --*Specifies whether (true) or not (false) AWS Import/Export updated
      your job.
    """


_ClientCreateJobResponseArtifactListTypeDef = TypedDict(
    "_ClientCreateJobResponseArtifactListTypeDef", {"Description": str, "URL": str}, total=False
)


class ClientCreateJobResponseArtifactListTypeDef(_ClientCreateJobResponseArtifactListTypeDef):
    """
    - *(dict) --*A discrete item that contains the description and URL of an artifact (such as a
    PDF).

      - **Description** *(string) --*The associated description for this object.
      - **URL** *(string) --*The URL for a given Artifact.
    """


_ClientCreateJobResponseTypeDef = TypedDict(
    "_ClientCreateJobResponseTypeDef",
    {
        "JobId": str,
        "JobType": Literal["Import", "Export"],
        "Signature": str,
        "SignatureFileContents": str,
        "WarningMessage": str,
        "ArtifactList": List[ClientCreateJobResponseArtifactListTypeDef],
    },
    total=False,
)


class ClientCreateJobResponseTypeDef(_ClientCreateJobResponseTypeDef):
    """
    - *(dict) --*Output structure for the CreateJob operation.

      - **JobId** *(string) --*A unique identifier which refers to a particular job.
      - **JobType** *(string) --*Specifies whether the job to initiate is an import or export job.
      - **Signature** *(string) --*An encrypted code used to authenticate the request and response,
      for example, "DV+TpDfx1/TdSE9ktyK9k/bDTVI=". Only use this value is you want to create the
      signature file yourself. Generally you should use the SignatureFileContents value.
      - **SignatureFileContents** *(string) --*The actual text of the SIGNATURE file to be written
      to disk.
      - **WarningMessage** *(string) --*An optional message notifying you of non-fatal issues with
      the job, such as use of an incompatible Amazon S3 bucket name.
      - **ArtifactList** *(list) --*A collection of artifacts.

        - *(dict) --*A discrete item that contains the description and URL of an artifact (such as a
        PDF).

          - **Description** *(string) --*The associated description for this object.
          - **URL** *(string) --*The URL for a given Artifact.
    """


_ClientGetShippingLabelResponseTypeDef = TypedDict(
    "_ClientGetShippingLabelResponseTypeDef", {"ShippingLabelURL": str, "Warning": str}, total=False
)


class ClientGetShippingLabelResponseTypeDef(_ClientGetShippingLabelResponseTypeDef):
    """
    - *(dict) --*

      - **ShippingLabelURL** *(string) --*
      - **Warning** *(string) --*
    """


_ClientGetStatusResponseArtifactListTypeDef = TypedDict(
    "_ClientGetStatusResponseArtifactListTypeDef", {"Description": str, "URL": str}, total=False
)


class ClientGetStatusResponseArtifactListTypeDef(_ClientGetStatusResponseArtifactListTypeDef):
    """
    - *(dict) --*A discrete item that contains the description and URL of an artifact (such as a
    PDF).

      - **Description** *(string) --*The associated description for this object.
      - **URL** *(string) --*The URL for a given Artifact.
    """


_ClientGetStatusResponseTypeDef = TypedDict(
    "_ClientGetStatusResponseTypeDef",
    {
        "JobId": str,
        "JobType": Literal["Import", "Export"],
        "LocationCode": str,
        "LocationMessage": str,
        "ProgressCode": str,
        "ProgressMessage": str,
        "Carrier": str,
        "TrackingNumber": str,
        "LogBucket": str,
        "LogKey": str,
        "ErrorCount": int,
        "Signature": str,
        "SignatureFileContents": str,
        "CurrentManifest": str,
        "CreationDate": datetime,
        "ArtifactList": List[ClientGetStatusResponseArtifactListTypeDef],
    },
    total=False,
)


class ClientGetStatusResponseTypeDef(_ClientGetStatusResponseTypeDef):
    """
    - *(dict) --*Output structure for the GetStatus operation.

      - **JobId** *(string) --*A unique identifier which refers to a particular job.
      - **JobType** *(string) --*Specifies whether the job to initiate is an import or export job.
      - **LocationCode** *(string) --*A token representing the location of the storage device, such
      as "AtAWS".
      - **LocationMessage** *(string) --*A more human readable form of the physical location of the
      storage device.
      - **ProgressCode** *(string) --*A token representing the state of the job, such as "Started".
      - **ProgressMessage** *(string) --*A more human readable form of the job status.
      - **Carrier** *(string) --*Name of the shipping company. This value is included when the
      LocationCode is "Returned".
      - **TrackingNumber** *(string) --*The shipping tracking number assigned by AWS Import/Export
      to the storage device when it's returned to you. We return this value when the LocationCode is
      "Returned".
      - **LogBucket** *(string) --*Amazon S3 bucket for user logs.
      - **LogKey** *(string) --*The key where the user logs were stored.
      - **ErrorCount** *(integer) --*Number of errors. We return this value when the ProgressCode is
      Success or SuccessWithErrors.
      - **Signature** *(string) --*An encrypted code used to authenticate the request and response,
      for example, "DV+TpDfx1/TdSE9ktyK9k/bDTVI=". Only use this value is you want to create the
      signature file yourself. Generally you should use the SignatureFileContents value.
      - **SignatureFileContents** *(string) --*An encrypted code used to authenticate the request
      and response, for example, "DV+TpDfx1/TdSE9ktyK9k/bDTVI=
          ". Only use this value is you want to
      create the signature file yourself. Generally you should use the SignatureFileContents value.
      - **CurrentManifest** *(string) --*The last manifest submitted, which will be used to process
      the job.
      - **CreationDate** *(datetime) --*Timestamp of the CreateJob request in ISO8601 date format.
      For example "2010-03-28T20:27:35Z".
      - **ArtifactList** *(list) --*A collection of artifacts.

        - *(dict) --*A discrete item that contains the description and URL of an artifact (such as a
        PDF).

          - **Description** *(string) --*The associated description for this object.
          - **URL** *(string) --*The URL for a given Artifact.
    """


_ClientListJobsResponseJobsTypeDef = TypedDict(
    "_ClientListJobsResponseJobsTypeDef",
    {
        "JobId": str,
        "CreationDate": datetime,
        "IsCanceled": bool,
        "JobType": Literal["Import", "Export"],
    },
    total=False,
)


class ClientListJobsResponseJobsTypeDef(_ClientListJobsResponseJobsTypeDef):
    """
    - *(dict) --*Representation of a job returned by the ListJobs operation.

      - **JobId** *(string) --*A unique identifier which refers to a particular job.
      - **CreationDate** *(datetime) --*Timestamp of the CreateJob request in ISO8601 date format.
      For example "2010-03-28T20:27:35Z".
      - **IsCanceled** *(boolean) --*Indicates whether the job was canceled.
      - **JobType** *(string) --*Specifies whether the job to initiate is an import or export job.
    """


_ClientListJobsResponseTypeDef = TypedDict(
    "_ClientListJobsResponseTypeDef",
    {"Jobs": List[ClientListJobsResponseJobsTypeDef], "IsTruncated": bool},
    total=False,
)


class ClientListJobsResponseTypeDef(_ClientListJobsResponseTypeDef):
    """
    - *(dict) --*Output structure for the ListJobs operation.

      - **Jobs** *(list) --*A list container for Jobs returned by the ListJobs operation.

        - *(dict) --*Representation of a job returned by the ListJobs operation.

          - **JobId** *(string) --*A unique identifier which refers to a particular job.
          - **CreationDate** *(datetime) --*Timestamp of the CreateJob request in ISO8601 date
          format. For example "2010-03-28T20:27:35Z".
          - **IsCanceled** *(boolean) --*Indicates whether the job was canceled.
          - **JobType** *(string) --*Specifies whether the job to initiate is an import or export
          job.
    """


_ClientUpdateJobResponseArtifactListTypeDef = TypedDict(
    "_ClientUpdateJobResponseArtifactListTypeDef", {"Description": str, "URL": str}, total=False
)


class ClientUpdateJobResponseArtifactListTypeDef(_ClientUpdateJobResponseArtifactListTypeDef):
    """
    - *(dict) --*A discrete item that contains the description and URL of an artifact (such as a
    PDF).

      - **Description** *(string) --*The associated description for this object.
      - **URL** *(string) --*The URL for a given Artifact.
    """


_ClientUpdateJobResponseTypeDef = TypedDict(
    "_ClientUpdateJobResponseTypeDef",
    {
        "Success": bool,
        "WarningMessage": str,
        "ArtifactList": List[ClientUpdateJobResponseArtifactListTypeDef],
    },
    total=False,
)


class ClientUpdateJobResponseTypeDef(_ClientUpdateJobResponseTypeDef):
    """
    - *(dict) --*Output structure for the UpateJob operation.

      - **Success** *(boolean) --*Specifies whether (true) or not (false) AWS Import/Export updated
      your job.
      - **WarningMessage** *(string) --*An optional message notifying you of non-fatal issues with
      the job, such as use of an incompatible Amazon S3 bucket name.
      - **ArtifactList** *(list) --*A collection of artifacts.

        - *(dict) --*A discrete item that contains the description and URL of an artifact (such as a
        PDF).

          - **Description** *(string) --*The associated description for this object.
          - **URL** *(string) --*The URL for a given Artifact.
    """


_ListJobsPaginatePaginationConfigTypeDef = TypedDict(
    "_ListJobsPaginatePaginationConfigTypeDef",
    {"MaxItems": int, "PageSize": int, "StartingToken": str},
    total=False,
)


class ListJobsPaginatePaginationConfigTypeDef(_ListJobsPaginatePaginationConfigTypeDef):
    """
    A dictionary that provides parameters to control pagination.
    - **MaxItems** *(integer) --*

      The total number of items to return. If the total number of items available is more than the
      value specified in max-items then a ``NextToken`` will be provided in the output that you can
      use to resume pagination.
    """


_ListJobsPaginateResponseJobsTypeDef = TypedDict(
    "_ListJobsPaginateResponseJobsTypeDef",
    {
        "JobId": str,
        "CreationDate": datetime,
        "IsCanceled": bool,
        "JobType": Literal["Import", "Export"],
    },
    total=False,
)


class ListJobsPaginateResponseJobsTypeDef(_ListJobsPaginateResponseJobsTypeDef):
    """
    - *(dict) --*Representation of a job returned by the ListJobs operation.

      - **JobId** *(string) --*A unique identifier which refers to a particular job.
      - **CreationDate** *(datetime) --*Timestamp of the CreateJob request in ISO8601 date format.
      For example "2010-03-28T20:27:35Z".
      - **IsCanceled** *(boolean) --*Indicates whether the job was canceled.
      - **JobType** *(string) --*Specifies whether the job to initiate is an import or export job.
    """


_ListJobsPaginateResponseTypeDef = TypedDict(
    "_ListJobsPaginateResponseTypeDef",
    {"Jobs": List[ListJobsPaginateResponseJobsTypeDef], "IsTruncated": bool, "NextToken": str},
    total=False,
)


class ListJobsPaginateResponseTypeDef(_ListJobsPaginateResponseTypeDef):
    """
    - *(dict) --*Output structure for the ListJobs operation.

      - **Jobs** *(list) --*A list container for Jobs returned by the ListJobs operation.

        - *(dict) --*Representation of a job returned by the ListJobs operation.

          - **JobId** *(string) --*A unique identifier which refers to a particular job.
          - **CreationDate** *(datetime) --*Timestamp of the CreateJob request in ISO8601 date
          format. For example "2010-03-28T20:27:35Z".
          - **IsCanceled** *(boolean) --*Indicates whether the job was canceled.
          - **JobType** *(string) --*Specifies whether the job to initiate is an import or export
          job.
    """
