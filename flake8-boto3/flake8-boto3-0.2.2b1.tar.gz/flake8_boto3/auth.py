import ast
from typing import List

from flake8_boto3 import __version__
from flake8_boto3.dumb_scope_visitor import DumbScopeVisitor

BOTO3_NAME = "boto3"
BAD_KEYWORDS = {"aws_access_key_id", "aws_secret_access_key", "aws_session_token"}


class AuthTokenVisitor(DumbScopeVisitor):
    name = "r2c-boto3-hardcoded-access-token"

    def __init__(self):
        self.report_nodes: List[ast.Call] = []
        self.using_boto3 = False
        super(AuthTokenVisitor, self).__init__()

    def _message(self, node):
        return f"{self.name} Hardcoded access token detected. Consider using a config file or environment variables."

    def _make_report(self, node):
        return {"node": node, "message": self._message(node)}

    def _validate_aws_access_key_id(self, str_values: List[str]) -> bool:
        """
        Return true if any value
        1. starts with AKIA
        2. does not contain a space
        3. the token portion is 16 or more chars
        """
        return any([val.startswith("AKIA") and " " not in val and len(val[4:]) >= 16 for val in str_values])

    def _validate_other(self, str_values: List[str]) -> bool:
        """
        Return true if any value
        1. is not a repetition of the same character, e.g., '---' or 'XXXX'
        2. does not have a space, e.g., "<your token here>"
        3. is 16 or more chars
        """
        return any([len(set(val)) != 1 and " " not in val and len(val) >= 16 for val in str_values])

    def _validate_token(self, keyword_arg: str, str_nodes: List[ast.Str]) -> bool:
        str_values: List[str] = [self._get_symbol_value(sn) for sn in str_nodes]
        if keyword_arg == "aws_access_key_id":
            return self._validate_aws_access_key_id(str_values)
        else:
            return self._validate_other(str_values)

    def visit_Call(self, call: ast.Call):
        keywords = call.keywords
        for keyword in keywords:
            if keyword.arg in BAD_KEYWORDS:
                if isinstance(keyword.value, ast.Str) and self._validate_token(
                    keyword.arg,
                    [keyword.value]
                ):
                    self.report_nodes.append(self._make_report(call))
                    break  # only report this call once even if (likely) multiple bad keyword args
                elif isinstance(keyword.value, ast.Name):
                    # resolve to variable, if str, alert
                    possible_value_nodes = self.get_symbol_value_nodes(keyword.value.id)
                    if all(
                        [isinstance(node, ast.Str) for node in possible_value_nodes]
                    ) and self._validate_token(keyword.arg, possible_value_nodes):
                        self.report_nodes.append(self._make_report(call))
                        break

    def visit_Import(self, _import: ast.Import):
        names = _import.names
        for fqn in names:
            if fqn.name == BOTO3_NAME:
                self.using_boto3 = True

    def visit_ImportFrom(self, import_from: ast.ImportFrom):
        if import_from.module == BOTO3_NAME:
            self.using_boto3 = True
