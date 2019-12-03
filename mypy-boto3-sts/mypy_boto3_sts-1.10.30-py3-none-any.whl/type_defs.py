"Main interface for sts service type defs"
from __future__ import annotations

from datetime import datetime
from mypy_boto3.type_defs import TypedDict


__all__ = (
    "ClientAssumeRolePolicyArnsTypeDef",
    "ClientAssumeRoleResponseAssumedRoleUserTypeDef",
    "ClientAssumeRoleResponseCredentialsTypeDef",
    "ClientAssumeRoleResponseTypeDef",
    "ClientAssumeRoleTagsTypeDef",
    "ClientAssumeRoleWithSamlPolicyArnsTypeDef",
    "ClientAssumeRoleWithSamlResponseAssumedRoleUserTypeDef",
    "ClientAssumeRoleWithSamlResponseCredentialsTypeDef",
    "ClientAssumeRoleWithSamlResponseTypeDef",
    "ClientAssumeRoleWithWebIdentityPolicyArnsTypeDef",
    "ClientAssumeRoleWithWebIdentityResponseAssumedRoleUserTypeDef",
    "ClientAssumeRoleWithWebIdentityResponseCredentialsTypeDef",
    "ClientAssumeRoleWithWebIdentityResponseTypeDef",
    "ClientDecodeAuthorizationMessageResponseTypeDef",
    "ClientGetAccessKeyInfoResponseTypeDef",
    "ClientGetCallerIdentityResponseTypeDef",
    "ClientGetFederationTokenPolicyArnsTypeDef",
    "ClientGetFederationTokenResponseCredentialsTypeDef",
    "ClientGetFederationTokenResponseFederatedUserTypeDef",
    "ClientGetFederationTokenResponseTypeDef",
    "ClientGetFederationTokenTagsTypeDef",
    "ClientGetSessionTokenResponseCredentialsTypeDef",
    "ClientGetSessionTokenResponseTypeDef",
)


_ClientAssumeRolePolicyArnsTypeDef = TypedDict(
    "_ClientAssumeRolePolicyArnsTypeDef", {"arn": str}, total=False
)


class ClientAssumeRolePolicyArnsTypeDef(_ClientAssumeRolePolicyArnsTypeDef):
    pass


_ClientAssumeRoleResponseAssumedRoleUserTypeDef = TypedDict(
    "_ClientAssumeRoleResponseAssumedRoleUserTypeDef",
    {"AssumedRoleId": str, "Arn": str},
    total=False,
)


class ClientAssumeRoleResponseAssumedRoleUserTypeDef(
    _ClientAssumeRoleResponseAssumedRoleUserTypeDef
):
    pass


_ClientAssumeRoleResponseCredentialsTypeDef = TypedDict(
    "_ClientAssumeRoleResponseCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str, "Expiration": datetime},
    total=False,
)


class ClientAssumeRoleResponseCredentialsTypeDef(_ClientAssumeRoleResponseCredentialsTypeDef):
    """
    - **Credentials** *(dict) --*

      The temporary security credentials, which include an access key ID, a secret access key, and a
      security (or session) token.
      .. note::

        The size of the security token that STS API operations return is not fixed. We strongly
        recommend that you make no assumptions about the maximum size.
    """


_ClientAssumeRoleResponseTypeDef = TypedDict(
    "_ClientAssumeRoleResponseTypeDef",
    {
        "Credentials": ClientAssumeRoleResponseCredentialsTypeDef,
        "AssumedRoleUser": ClientAssumeRoleResponseAssumedRoleUserTypeDef,
        "PackedPolicySize": int,
    },
    total=False,
)


class ClientAssumeRoleResponseTypeDef(_ClientAssumeRoleResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  AssumeRole request, including temporary AWS credentials
      that can be used to make AWS requests.
      - **Credentials** *(dict) --*

        The temporary security credentials, which include an access key ID, a secret access key, and
        a security (or session) token.
        .. note::

          The size of the security token that STS API operations return is not fixed. We strongly
          recommend that you make no assumptions about the maximum size.
    """


_ClientAssumeRoleTagsTypeDef = TypedDict(
    "_ClientAssumeRoleTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientAssumeRoleTagsTypeDef(_ClientAssumeRoleTagsTypeDef):
    pass


_ClientAssumeRoleWithSamlPolicyArnsTypeDef = TypedDict(
    "_ClientAssumeRoleWithSamlPolicyArnsTypeDef", {"arn": str}, total=False
)


class ClientAssumeRoleWithSamlPolicyArnsTypeDef(_ClientAssumeRoleWithSamlPolicyArnsTypeDef):
    pass


_ClientAssumeRoleWithSamlResponseAssumedRoleUserTypeDef = TypedDict(
    "_ClientAssumeRoleWithSamlResponseAssumedRoleUserTypeDef",
    {"AssumedRoleId": str, "Arn": str},
    total=False,
)


class ClientAssumeRoleWithSamlResponseAssumedRoleUserTypeDef(
    _ClientAssumeRoleWithSamlResponseAssumedRoleUserTypeDef
):
    pass


_ClientAssumeRoleWithSamlResponseCredentialsTypeDef = TypedDict(
    "_ClientAssumeRoleWithSamlResponseCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str, "Expiration": datetime},
    total=False,
)


class ClientAssumeRoleWithSamlResponseCredentialsTypeDef(
    _ClientAssumeRoleWithSamlResponseCredentialsTypeDef
):
    """
    - **Credentials** *(dict) --*

      The temporary security credentials, which include an access key ID, a secret access key, and a
      security (or session) token.
      .. note::

        The size of the security token that STS API operations return is not fixed. We strongly
        recommend that you make no assumptions about the maximum size.
    """


_ClientAssumeRoleWithSamlResponseTypeDef = TypedDict(
    "_ClientAssumeRoleWithSamlResponseTypeDef",
    {
        "Credentials": ClientAssumeRoleWithSamlResponseCredentialsTypeDef,
        "AssumedRoleUser": ClientAssumeRoleWithSamlResponseAssumedRoleUserTypeDef,
        "PackedPolicySize": int,
        "Subject": str,
        "SubjectType": str,
        "Issuer": str,
        "Audience": str,
        "NameQualifier": str,
    },
    total=False,
)


class ClientAssumeRoleWithSamlResponseTypeDef(_ClientAssumeRoleWithSamlResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  AssumeRoleWithSAML request, including temporary AWS
      credentials that can be used to make AWS requests.
      - **Credentials** *(dict) --*

        The temporary security credentials, which include an access key ID, a secret access key, and
        a security (or session) token.
        .. note::

          The size of the security token that STS API operations return is not fixed. We strongly
          recommend that you make no assumptions about the maximum size.
    """


_ClientAssumeRoleWithWebIdentityPolicyArnsTypeDef = TypedDict(
    "_ClientAssumeRoleWithWebIdentityPolicyArnsTypeDef", {"arn": str}, total=False
)


class ClientAssumeRoleWithWebIdentityPolicyArnsTypeDef(
    _ClientAssumeRoleWithWebIdentityPolicyArnsTypeDef
):
    pass


_ClientAssumeRoleWithWebIdentityResponseAssumedRoleUserTypeDef = TypedDict(
    "_ClientAssumeRoleWithWebIdentityResponseAssumedRoleUserTypeDef",
    {"AssumedRoleId": str, "Arn": str},
    total=False,
)


class ClientAssumeRoleWithWebIdentityResponseAssumedRoleUserTypeDef(
    _ClientAssumeRoleWithWebIdentityResponseAssumedRoleUserTypeDef
):
    pass


_ClientAssumeRoleWithWebIdentityResponseCredentialsTypeDef = TypedDict(
    "_ClientAssumeRoleWithWebIdentityResponseCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str, "Expiration": datetime},
    total=False,
)


class ClientAssumeRoleWithWebIdentityResponseCredentialsTypeDef(
    _ClientAssumeRoleWithWebIdentityResponseCredentialsTypeDef
):
    """
    - **Credentials** *(dict) --*

      The temporary security credentials, which include an access key ID, a secret access key, and a
      security token.
      .. note::

        The size of the security token that STS API operations return is not fixed. We strongly
        recommend that you make no assumptions about the maximum size.
    """


_ClientAssumeRoleWithWebIdentityResponseTypeDef = TypedDict(
    "_ClientAssumeRoleWithWebIdentityResponseTypeDef",
    {
        "Credentials": ClientAssumeRoleWithWebIdentityResponseCredentialsTypeDef,
        "SubjectFromWebIdentityToken": str,
        "AssumedRoleUser": ClientAssumeRoleWithWebIdentityResponseAssumedRoleUserTypeDef,
        "PackedPolicySize": int,
        "Provider": str,
        "Audience": str,
    },
    total=False,
)


class ClientAssumeRoleWithWebIdentityResponseTypeDef(
    _ClientAssumeRoleWithWebIdentityResponseTypeDef
):
    """
    - *(dict) --*

      Contains the response to a successful  AssumeRoleWithWebIdentity request, including temporary
      AWS credentials that can be used to make AWS requests.
      - **Credentials** *(dict) --*

        The temporary security credentials, which include an access key ID, a secret access key, and
        a security token.
        .. note::

          The size of the security token that STS API operations return is not fixed. We strongly
          recommend that you make no assumptions about the maximum size.
    """


_ClientDecodeAuthorizationMessageResponseTypeDef = TypedDict(
    "_ClientDecodeAuthorizationMessageResponseTypeDef", {"DecodedMessage": str}, total=False
)


class ClientDecodeAuthorizationMessageResponseTypeDef(
    _ClientDecodeAuthorizationMessageResponseTypeDef
):
    """
    - *(dict) --*

      A document that contains additional information about the authorization status of a request
      from an encoded message that is returned in response to an AWS request.
      - **DecodedMessage** *(string) --*

        An XML document that contains the decoded message.
    """


_ClientGetAccessKeyInfoResponseTypeDef = TypedDict(
    "_ClientGetAccessKeyInfoResponseTypeDef", {"Account": str}, total=False
)


class ClientGetAccessKeyInfoResponseTypeDef(_ClientGetAccessKeyInfoResponseTypeDef):
    """
    - *(dict) --*

      - **Account** *(string) --*

        The number used to identify the AWS account.
    """


_ClientGetCallerIdentityResponseTypeDef = TypedDict(
    "_ClientGetCallerIdentityResponseTypeDef",
    {"UserId": str, "Account": str, "Arn": str},
    total=False,
)


class ClientGetCallerIdentityResponseTypeDef(_ClientGetCallerIdentityResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetCallerIdentity request, including information about
      the entity making the request.
      - **UserId** *(string) --*

        The unique identifier of the calling entity. The exact value depends on the type of entity
        that is making the call. The values returned are those listed in the **aws:userid** column
        in the `Principal table
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html#principaltable>`__
        found on the **Policy Variables** reference page in the *IAM User Guide* .
    """


_ClientGetFederationTokenPolicyArnsTypeDef = TypedDict(
    "_ClientGetFederationTokenPolicyArnsTypeDef", {"arn": str}, total=False
)


class ClientGetFederationTokenPolicyArnsTypeDef(_ClientGetFederationTokenPolicyArnsTypeDef):
    pass


_ClientGetFederationTokenResponseCredentialsTypeDef = TypedDict(
    "_ClientGetFederationTokenResponseCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str, "Expiration": datetime},
    total=False,
)


class ClientGetFederationTokenResponseCredentialsTypeDef(
    _ClientGetFederationTokenResponseCredentialsTypeDef
):
    """
    - **Credentials** *(dict) --*

      The temporary security credentials, which include an access key ID, a secret access key, and a
      security (or session) token.
      .. note::

        The size of the security token that STS API operations return is not fixed. We strongly
        recommend that you make no assumptions about the maximum size.
    """


_ClientGetFederationTokenResponseFederatedUserTypeDef = TypedDict(
    "_ClientGetFederationTokenResponseFederatedUserTypeDef",
    {"FederatedUserId": str, "Arn": str},
    total=False,
)


class ClientGetFederationTokenResponseFederatedUserTypeDef(
    _ClientGetFederationTokenResponseFederatedUserTypeDef
):
    pass


_ClientGetFederationTokenResponseTypeDef = TypedDict(
    "_ClientGetFederationTokenResponseTypeDef",
    {
        "Credentials": ClientGetFederationTokenResponseCredentialsTypeDef,
        "FederatedUser": ClientGetFederationTokenResponseFederatedUserTypeDef,
        "PackedPolicySize": int,
    },
    total=False,
)


class ClientGetFederationTokenResponseTypeDef(_ClientGetFederationTokenResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetFederationToken request, including temporary AWS
      credentials that can be used to make AWS requests.
      - **Credentials** *(dict) --*

        The temporary security credentials, which include an access key ID, a secret access key, and
        a security (or session) token.
        .. note::

          The size of the security token that STS API operations return is not fixed. We strongly
          recommend that you make no assumptions about the maximum size.
    """


_ClientGetFederationTokenTagsTypeDef = TypedDict(
    "_ClientGetFederationTokenTagsTypeDef", {"Key": str, "Value": str}, total=False
)


class ClientGetFederationTokenTagsTypeDef(_ClientGetFederationTokenTagsTypeDef):
    pass


_ClientGetSessionTokenResponseCredentialsTypeDef = TypedDict(
    "_ClientGetSessionTokenResponseCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str, "Expiration": datetime},
    total=False,
)


class ClientGetSessionTokenResponseCredentialsTypeDef(
    _ClientGetSessionTokenResponseCredentialsTypeDef
):
    """
    - **Credentials** *(dict) --*

      The temporary security credentials, which include an access key ID, a secret access key, and a
      security (or session) token.
      .. note::

        The size of the security token that STS API operations return is not fixed. We strongly
        recommend that you make no assumptions about the maximum size.
    """


_ClientGetSessionTokenResponseTypeDef = TypedDict(
    "_ClientGetSessionTokenResponseTypeDef",
    {"Credentials": ClientGetSessionTokenResponseCredentialsTypeDef},
    total=False,
)


class ClientGetSessionTokenResponseTypeDef(_ClientGetSessionTokenResponseTypeDef):
    """
    - *(dict) --*

      Contains the response to a successful  GetSessionToken request, including temporary AWS
      credentials that can be used to make AWS requests.
      - **Credentials** *(dict) --*

        The temporary security credentials, which include an access key ID, a secret access key, and
        a security (or session) token.
        .. note::

          The size of the security token that STS API operations return is not fixed. We strongly
          recommend that you make no assumptions about the maximum size.
    """
