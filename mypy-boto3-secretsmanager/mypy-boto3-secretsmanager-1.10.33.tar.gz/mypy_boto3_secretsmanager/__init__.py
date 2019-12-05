"Main interface for secretsmanager service"

from mypy_boto3_secretsmanager.client import Client
from mypy_boto3_secretsmanager.paginator import ListSecretsPaginator


__all__ = ("Client", "ListSecretsPaginator")
