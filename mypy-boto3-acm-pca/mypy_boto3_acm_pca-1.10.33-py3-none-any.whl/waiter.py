"Main interface for acm-pca service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_acm_pca.type_defs import (
    AuditReportCreatedWaitWaiterConfigTypeDef,
    CertificateAuthorityCsrCreatedWaitWaiterConfigTypeDef,
    CertificateIssuedWaitWaiterConfigTypeDef,
)


__all__ = (
    "AuditReportCreatedWaiter",
    "CertificateAuthorityCSRCreatedWaiter",
    "CertificateIssuedWaiter",
)


class AuditReportCreatedWaiter(Boto3Waiter):
    """
    Waiter for `audit_report_created` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        CertificateAuthorityArn: str,
        AuditReportId: str,
        WaiterConfig: AuditReportCreatedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [audit_report_created.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/acm-pca.html#ACMPCA.Waiter.audit_report_created.wait)
        """


class CertificateAuthorityCSRCreatedWaiter(Boto3Waiter):
    """
    Waiter for `certificate_authority_csr_created` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        CertificateAuthorityArn: str,
        WaiterConfig: CertificateAuthorityCsrCreatedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [certificate_authority_csr_created.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/acm-pca.html#ACMPCA.Waiter.certificate_authority_csr_created.wait)
        """


class CertificateIssuedWaiter(Boto3Waiter):
    """
    Waiter for `certificate_issued` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        CertificateAuthorityArn: str,
        CertificateArn: str,
        WaiterConfig: CertificateIssuedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        [certificate_issued.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/acm-pca.html#ACMPCA.Waiter.certificate_issued.wait)
        """
