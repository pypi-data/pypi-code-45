"Main interface for codeguru-reviewer service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_codeguru_reviewer.type_defs import (
    ListRepositoryAssociationsPaginatePaginationConfigTypeDef,
    ListRepositoryAssociationsPaginateResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ListRepositoryAssociationsPaginator",)


class ListRepositoryAssociationsPaginator(Boto3Paginator):
    """
    Paginator for `list_repository_associations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ProviderTypes: List[Literal["CodeCommit", "GitHub"]] = None,
        States: List[Literal["Associated", "Associating", "Failed", "Disassociating"]] = None,
        Names: List[str] = None,
        Owners: List[str] = None,
        PaginationConfig: ListRepositoryAssociationsPaginatePaginationConfigTypeDef = None,
    ) -> ListRepositoryAssociationsPaginateResponseTypeDef:
        """
        [ListRepositoryAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.33/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Paginator.ListRepositoryAssociations.paginate)
        """
