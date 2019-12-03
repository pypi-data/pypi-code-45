"Main interface for comprehendmedical service type defs"
from __future__ import annotations

from datetime import datetime
from typing import Any, List
from mypy_boto3.type_defs import Literal, TypedDict


__all__ = (
    "ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef",
    "ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef",
    "ClientDescribeEntitiesDetectionV2JobResponseTypeDef",
    "ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef",
    "ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef",
    "ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef",
    "ClientDescribePhiDetectionJobResponseTypeDef",
    "ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef",
    "ClientDetectEntitiesResponseEntitiesAttributesTypeDef",
    "ClientDetectEntitiesResponseEntitiesTraitsTypeDef",
    "ClientDetectEntitiesResponseEntitiesTypeDef",
    "ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef",
    "ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef",
    "ClientDetectEntitiesResponseUnmappedAttributesTypeDef",
    "ClientDetectEntitiesResponseTypeDef",
    "ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef",
    "ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef",
    "ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef",
    "ClientDetectEntitiesV2ResponseEntitiesTypeDef",
    "ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef",
    "ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef",
    "ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef",
    "ClientDetectEntitiesV2ResponseTypeDef",
    "ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef",
    "ClientDetectPhiResponseEntitiesAttributesTypeDef",
    "ClientDetectPhiResponseEntitiesTraitsTypeDef",
    "ClientDetectPhiResponseEntitiesTypeDef",
    "ClientDetectPhiResponseTypeDef",
    "ClientListEntitiesDetectionV2JobsFilterTypeDef",
    "ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef",
    "ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef",
    "ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef",
    "ClientListEntitiesDetectionV2JobsResponseTypeDef",
    "ClientListPhiDetectionJobsFilterTypeDef",
    "ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef",
    "ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef",
    "ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef",
    "ClientListPhiDetectionJobsResponseTypeDef",
    "ClientStartEntitiesDetectionV2JobInputDataConfigTypeDef",
    "ClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef",
    "ClientStartEntitiesDetectionV2JobResponseTypeDef",
    "ClientStartPhiDetectionJobInputDataConfigTypeDef",
    "ClientStartPhiDetectionJobOutputDataConfigTypeDef",
    "ClientStartPhiDetectionJobResponseTypeDef",
    "ClientStopEntitiesDetectionV2JobResponseTypeDef",
    "ClientStopPhiDetectionJobResponseTypeDef",
)


_ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef(
    _ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef
):
    pass


_ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef
):
    pass


_ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "ExpirationTime": datetime,
        "InputDataConfig": ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "ManifestFilePath": str,
        "KMSKey": str,
        "ModelVersion": str,
    },
    total=False,
)


class ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef(
    _ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef
):
    """
    - **ComprehendMedicalAsyncJobProperties** *(dict) --*

      An object that contains the properties associated with a detection job.
      - **JobId** *(string) --*

        The identifier assigned to the detection job.
    """


_ClientDescribeEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "_ClientDescribeEntitiesDetectionV2JobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": ClientDescribeEntitiesDetectionV2JobResponseComprehendMedicalAsyncJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribeEntitiesDetectionV2JobResponseTypeDef(
    _ClientDescribeEntitiesDetectionV2JobResponseTypeDef
):
    """
    - *(dict) --*

      - **ComprehendMedicalAsyncJobProperties** *(dict) --*

        An object that contains the properties associated with a detection job.
        - **JobId** *(string) --*

          The identifier assigned to the detection job.
    """


_ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef = TypedDict(
    "_ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef(
    _ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef
):
    pass


_ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef = TypedDict(
    "_ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef(
    _ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef
):
    pass


_ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef = TypedDict(
    "_ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "ExpirationTime": datetime,
        "InputDataConfig": ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesInputDataConfigTypeDef,
        "OutputDataConfig": ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "ManifestFilePath": str,
        "KMSKey": str,
        "ModelVersion": str,
    },
    total=False,
)


class ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef(
    _ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef
):
    """
    - **ComprehendMedicalAsyncJobProperties** *(dict) --*

      An object that contains the properties associated with a detection job.
      - **JobId** *(string) --*

        The identifier assigned to the detection job.
    """


_ClientDescribePhiDetectionJobResponseTypeDef = TypedDict(
    "_ClientDescribePhiDetectionJobResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobProperties": ClientDescribePhiDetectionJobResponseComprehendMedicalAsyncJobPropertiesTypeDef
    },
    total=False,
)


class ClientDescribePhiDetectionJobResponseTypeDef(_ClientDescribePhiDetectionJobResponseTypeDef):
    """
    - *(dict) --*

      - **ComprehendMedicalAsyncJobProperties** *(dict) --*

        An object that contains the properties associated with a detection job.
        - **JobId** *(string) --*

          The identifier assigned to the detection job.
    """


_ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)


class ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef(
    _ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef
):
    pass


_ClientDetectEntitiesResponseEntitiesAttributesTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseEntitiesAttributesTypeDef",
    {
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Score": Any,
        "RelationshipScore": Any,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[ClientDetectEntitiesResponseEntitiesAttributesTraitsTypeDef],
    },
    total=False,
)


class ClientDetectEntitiesResponseEntitiesAttributesTypeDef(
    _ClientDetectEntitiesResponseEntitiesAttributesTypeDef
):
    pass


_ClientDetectEntitiesResponseEntitiesTraitsTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseEntitiesTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)


class ClientDetectEntitiesResponseEntitiesTraitsTypeDef(
    _ClientDetectEntitiesResponseEntitiesTraitsTypeDef
):
    pass


_ClientDetectEntitiesResponseEntitiesTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseEntitiesTypeDef",
    {
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Score": Any,
        "Text": str,
        "Category": Literal[
            "MEDICATION",
            "MEDICAL_CONDITION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "ANATOMY",
        ],
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Traits": List[ClientDetectEntitiesResponseEntitiesTraitsTypeDef],
        "Attributes": List[ClientDetectEntitiesResponseEntitiesAttributesTypeDef],
    },
    total=False,
)


class ClientDetectEntitiesResponseEntitiesTypeDef(_ClientDetectEntitiesResponseEntitiesTypeDef):
    """
    - *(dict) --*

      Provides information about an extracted medical entity.
      - **Id** *(integer) --*

        The numeric identifier for the entity. This is a monotonically increasing id unique within
        this response rather than a global unique identifier.
    """


_ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)


class ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef(
    _ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef
):
    pass


_ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef",
    {
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Score": Any,
        "RelationshipScore": Any,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[ClientDetectEntitiesResponseUnmappedAttributesAttributeTraitsTypeDef],
    },
    total=False,
)


class ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef(
    _ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef
):
    pass


_ClientDetectEntitiesResponseUnmappedAttributesTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseUnmappedAttributesTypeDef",
    {
        "Type": Literal[
            "MEDICATION",
            "MEDICAL_CONDITION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "ANATOMY",
        ],
        "Attribute": ClientDetectEntitiesResponseUnmappedAttributesAttributeTypeDef,
    },
    total=False,
)


class ClientDetectEntitiesResponseUnmappedAttributesTypeDef(
    _ClientDetectEntitiesResponseUnmappedAttributesTypeDef
):
    pass


_ClientDetectEntitiesResponseTypeDef = TypedDict(
    "_ClientDetectEntitiesResponseTypeDef",
    {
        "Entities": List[ClientDetectEntitiesResponseEntitiesTypeDef],
        "UnmappedAttributes": List[ClientDetectEntitiesResponseUnmappedAttributesTypeDef],
        "PaginationToken": str,
        "ModelVersion": str,
    },
    total=False,
)


class ClientDetectEntitiesResponseTypeDef(_ClientDetectEntitiesResponseTypeDef):
    """
    - *(dict) --*

      - **Entities** *(list) --*

        The collection of medical entities extracted from the input text and their associated
        information. For each entity, the response provides the entity text, the entity category,
        where the entity text begins and ends, and the level of confidence that Amazon Comprehend
        Medical has in the detection and analysis. Attributes and traits of the entity are also
        returned.
        - *(dict) --*

          Provides information about an extracted medical entity.
          - **Id** *(integer) --*

            The numeric identifier for the entity. This is a monotonically increasing id unique
            within this response rather than a global unique identifier.
    """


_ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)


class ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef(
    _ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef
):
    pass


_ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef",
    {
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Score": Any,
        "RelationshipScore": Any,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[ClientDetectEntitiesV2ResponseEntitiesAttributesTraitsTypeDef],
    },
    total=False,
)


class ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef(
    _ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef
):
    pass


_ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)


class ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef(
    _ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef
):
    pass


_ClientDetectEntitiesV2ResponseEntitiesTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseEntitiesTypeDef",
    {
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Score": Any,
        "Text": str,
        "Category": Literal[
            "MEDICATION",
            "MEDICAL_CONDITION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "ANATOMY",
        ],
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Traits": List[ClientDetectEntitiesV2ResponseEntitiesTraitsTypeDef],
        "Attributes": List[ClientDetectEntitiesV2ResponseEntitiesAttributesTypeDef],
    },
    total=False,
)


class ClientDetectEntitiesV2ResponseEntitiesTypeDef(_ClientDetectEntitiesV2ResponseEntitiesTypeDef):
    """
    - *(dict) --*

      Provides information about an extracted medical entity.
      - **Id** *(integer) --*

        The numeric identifier for the entity. This is a monotonically increasing id unique within
        this response rather than a global unique identifier.
    """


_ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)


class ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef(
    _ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef
):
    pass


_ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef",
    {
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Score": Any,
        "RelationshipScore": Any,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTraitsTypeDef],
    },
    total=False,
)


class ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef(
    _ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef
):
    pass


_ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef",
    {
        "Type": Literal[
            "MEDICATION",
            "MEDICAL_CONDITION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "ANATOMY",
        ],
        "Attribute": ClientDetectEntitiesV2ResponseUnmappedAttributesAttributeTypeDef,
    },
    total=False,
)


class ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef(
    _ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef
):
    pass


_ClientDetectEntitiesV2ResponseTypeDef = TypedDict(
    "_ClientDetectEntitiesV2ResponseTypeDef",
    {
        "Entities": List[ClientDetectEntitiesV2ResponseEntitiesTypeDef],
        "UnmappedAttributes": List[ClientDetectEntitiesV2ResponseUnmappedAttributesTypeDef],
        "PaginationToken": str,
        "ModelVersion": str,
    },
    total=False,
)


class ClientDetectEntitiesV2ResponseTypeDef(_ClientDetectEntitiesV2ResponseTypeDef):
    """
    - *(dict) --*

      - **Entities** *(list) --*

        The collection of medical entities extracted from the input text and their associated
        information. For each entity, the response provides the entity text, the entity category,
        where the entity text begins and ends, and the level of confidence in the detection and
        analysis. Attributes and traits of the entity are also returned.
        - *(dict) --*

          Provides information about an extracted medical entity.
          - **Id** *(integer) --*

            The numeric identifier for the entity. This is a monotonically increasing id unique
            within this response rather than a global unique identifier.
    """


_ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef = TypedDict(
    "_ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)


class ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef(
    _ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef
):
    pass


_ClientDetectPhiResponseEntitiesAttributesTypeDef = TypedDict(
    "_ClientDetectPhiResponseEntitiesAttributesTypeDef",
    {
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Score": Any,
        "RelationshipScore": Any,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[ClientDetectPhiResponseEntitiesAttributesTraitsTypeDef],
    },
    total=False,
)


class ClientDetectPhiResponseEntitiesAttributesTypeDef(
    _ClientDetectPhiResponseEntitiesAttributesTypeDef
):
    pass


_ClientDetectPhiResponseEntitiesTraitsTypeDef = TypedDict(
    "_ClientDetectPhiResponseEntitiesTraitsTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": Any},
    total=False,
)


class ClientDetectPhiResponseEntitiesTraitsTypeDef(_ClientDetectPhiResponseEntitiesTraitsTypeDef):
    pass


_ClientDetectPhiResponseEntitiesTypeDef = TypedDict(
    "_ClientDetectPhiResponseEntitiesTypeDef",
    {
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Score": Any,
        "Text": str,
        "Category": Literal[
            "MEDICATION",
            "MEDICAL_CONDITION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "ANATOMY",
        ],
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Traits": List[ClientDetectPhiResponseEntitiesTraitsTypeDef],
        "Attributes": List[ClientDetectPhiResponseEntitiesAttributesTypeDef],
    },
    total=False,
)


class ClientDetectPhiResponseEntitiesTypeDef(_ClientDetectPhiResponseEntitiesTypeDef):
    """
    - *(dict) --*

      Provides information about an extracted medical entity.
      - **Id** *(integer) --*

        The numeric identifier for the entity. This is a monotonically increasing id unique within
        this response rather than a global unique identifier.
    """


_ClientDetectPhiResponseTypeDef = TypedDict(
    "_ClientDetectPhiResponseTypeDef",
    {
        "Entities": List[ClientDetectPhiResponseEntitiesTypeDef],
        "PaginationToken": str,
        "ModelVersion": str,
    },
    total=False,
)


class ClientDetectPhiResponseTypeDef(_ClientDetectPhiResponseTypeDef):
    """
    - *(dict) --*

      - **Entities** *(list) --*

        The collection of PHI entities extracted from the input text and their associated
        information. For each entity, the response provides the entity text, the entity category,
        where the entity text begins and ends, and the level of confidence that Amazon Comprehend
        Medical has in its detection.
        - *(dict) --*

          Provides information about an extracted medical entity.
          - **Id** *(integer) --*

            The numeric identifier for the entity. This is a monotonically increasing id unique
            within this response rather than a global unique identifier.
    """


_ClientListEntitiesDetectionV2JobsFilterTypeDef = TypedDict(
    "_ClientListEntitiesDetectionV2JobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListEntitiesDetectionV2JobsFilterTypeDef(
    _ClientListEntitiesDetectionV2JobsFilterTypeDef
):
    """
    Filters the jobs that are returned. You can filter jobs based on their names, status, or the
    date and time that they were submitted. You can only set one filter at a time.
    - **JobName** *(string) --*

      Filters on the name of the job.
    """


_ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef(
    _ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef
):
    pass


_ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef(
    _ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef
):
    pass


_ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef = TypedDict(
    "_ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "ExpirationTime": datetime,
        "InputDataConfig": ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "ManifestFilePath": str,
        "KMSKey": str,
        "ModelVersion": str,
    },
    total=False,
)


class ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef(
    _ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about a detection job.
      - **JobId** *(string) --*

        The identifier assigned to the detection job.
    """


_ClientListEntitiesDetectionV2JobsResponseTypeDef = TypedDict(
    "_ClientListEntitiesDetectionV2JobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            ClientListEntitiesDetectionV2JobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListEntitiesDetectionV2JobsResponseTypeDef(
    _ClientListEntitiesDetectionV2JobsResponseTypeDef
):
    """
    - *(dict) --*

      - **ComprehendMedicalAsyncJobPropertiesList** *(list) --*

        A list containing the properties of each job returned.
        - *(dict) --*

          Provides information about a detection job.
          - **JobId** *(string) --*

            The identifier assigned to the detection job.
    """


_ClientListPhiDetectionJobsFilterTypeDef = TypedDict(
    "_ClientListPhiDetectionJobsFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)


class ClientListPhiDetectionJobsFilterTypeDef(_ClientListPhiDetectionJobsFilterTypeDef):
    """
    Filters the jobs that are returned. You can filter jobs based on their names, status, or the
    date and time that they were submitted. You can only set one filter at a time.
    - **JobName** *(string) --*

      Filters on the name of the job.
    """


_ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef = TypedDict(
    "_ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef(
    _ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef
):
    pass


_ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef = TypedDict(
    "_ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef",
    {"S3Bucket": str, "S3Key": str},
    total=False,
)


class ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef(
    _ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef
):
    pass


_ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef = TypedDict(
    "_ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "ExpirationTime": datetime,
        "InputDataConfig": ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListInputDataConfigTypeDef,
        "OutputDataConfig": ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListOutputDataConfigTypeDef,
        "LanguageCode": str,
        "DataAccessRoleArn": str,
        "ManifestFilePath": str,
        "KMSKey": str,
        "ModelVersion": str,
    },
    total=False,
)


class ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef(
    _ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef
):
    """
    - *(dict) --*

      Provides information about a detection job.
      - **JobId** *(string) --*

        The identifier assigned to the detection job.
    """


_ClientListPhiDetectionJobsResponseTypeDef = TypedDict(
    "_ClientListPhiDetectionJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[
            ClientListPhiDetectionJobsResponseComprehendMedicalAsyncJobPropertiesListTypeDef
        ],
        "NextToken": str,
    },
    total=False,
)


class ClientListPhiDetectionJobsResponseTypeDef(_ClientListPhiDetectionJobsResponseTypeDef):
    """
    - *(dict) --*

      - **ComprehendMedicalAsyncJobPropertiesList** *(list) --*

        A list containing the properties of each job returned.
        - *(dict) --*

          Provides information about a detection job.
          - **JobId** *(string) --*

            The identifier assigned to the detection job.
    """


_RequiredClientStartEntitiesDetectionV2JobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartEntitiesDetectionV2JobInputDataConfigTypeDef", {"S3Bucket": str}
)
_OptionalClientStartEntitiesDetectionV2JobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartEntitiesDetectionV2JobInputDataConfigTypeDef", {"S3Key": str}, total=False
)


class ClientStartEntitiesDetectionV2JobInputDataConfigTypeDef(
    _RequiredClientStartEntitiesDetectionV2JobInputDataConfigTypeDef,
    _OptionalClientStartEntitiesDetectionV2JobInputDataConfigTypeDef,
):
    """
    Specifies the format and location of the input data for the job.
    - **S3Bucket** *(string) --***[REQUIRED]**

      The URI of the S3 bucket that contains the input data. The bucket must be in the same region
      as the API endpoint that you are calling.
      Each file in the document collection must be less than 40 KB. You can store a maximum of 30 GB
      in the bucket.
    """


_RequiredClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef", {"S3Bucket": str}
)
_OptionalClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef", {"S3Key": str}, total=False
)


class ClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef(
    _RequiredClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef,
    _OptionalClientStartEntitiesDetectionV2JobOutputDataConfigTypeDef,
):
    """
    Specifies where to send the output files.
    - **S3Bucket** *(string) --***[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output.
    """


_ClientStartEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "_ClientStartEntitiesDetectionV2JobResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartEntitiesDetectionV2JobResponseTypeDef(
    _ClientStartEntitiesDetectionV2JobResponseTypeDef
):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier generated for the job. To get the status of a job, use this identifier with
        the ``DescribeEntitiesDetectionV2Job`` operation.
    """


_RequiredClientStartPhiDetectionJobInputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartPhiDetectionJobInputDataConfigTypeDef", {"S3Bucket": str}
)
_OptionalClientStartPhiDetectionJobInputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartPhiDetectionJobInputDataConfigTypeDef", {"S3Key": str}, total=False
)


class ClientStartPhiDetectionJobInputDataConfigTypeDef(
    _RequiredClientStartPhiDetectionJobInputDataConfigTypeDef,
    _OptionalClientStartPhiDetectionJobInputDataConfigTypeDef,
):
    """
    Specifies the format and location of the input data for the job.
    - **S3Bucket** *(string) --***[REQUIRED]**

      The URI of the S3 bucket that contains the input data. The bucket must be in the same region
      as the API endpoint that you are calling.
      Each file in the document collection must be less than 40 KB. You can store a maximum of 30 GB
      in the bucket.
    """


_RequiredClientStartPhiDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_RequiredClientStartPhiDetectionJobOutputDataConfigTypeDef", {"S3Bucket": str}
)
_OptionalClientStartPhiDetectionJobOutputDataConfigTypeDef = TypedDict(
    "_OptionalClientStartPhiDetectionJobOutputDataConfigTypeDef", {"S3Key": str}, total=False
)


class ClientStartPhiDetectionJobOutputDataConfigTypeDef(
    _RequiredClientStartPhiDetectionJobOutputDataConfigTypeDef,
    _OptionalClientStartPhiDetectionJobOutputDataConfigTypeDef,
):
    """
    Specifies where to send the output files.
    - **S3Bucket** *(string) --***[REQUIRED]**

      When you use the ``OutputDataConfig`` object with asynchronous operations, you specify the
      Amazon S3 location where you want to write the output data. The URI must be in the same region
      as the API endpoint that you are calling. The location is used as the prefix for the actual
      location of the output.
    """


_ClientStartPhiDetectionJobResponseTypeDef = TypedDict(
    "_ClientStartPhiDetectionJobResponseTypeDef", {"JobId": str}, total=False
)


class ClientStartPhiDetectionJobResponseTypeDef(_ClientStartPhiDetectionJobResponseTypeDef):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier generated for the job. To get the status of a job, use this identifier with
        the ``DescribePHIDetectionJob`` operation.
    """


_ClientStopEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "_ClientStopEntitiesDetectionV2JobResponseTypeDef", {"JobId": str}, total=False
)


class ClientStopEntitiesDetectionV2JobResponseTypeDef(
    _ClientStopEntitiesDetectionV2JobResponseTypeDef
):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier of the medical entities detection job that was stopped.
    """


_ClientStopPhiDetectionJobResponseTypeDef = TypedDict(
    "_ClientStopPhiDetectionJobResponseTypeDef", {"JobId": str}, total=False
)


class ClientStopPhiDetectionJobResponseTypeDef(_ClientStopPhiDetectionJobResponseTypeDef):
    """
    - *(dict) --*

      - **JobId** *(string) --*

        The identifier of the PHI detection job that was stopped.
    """
