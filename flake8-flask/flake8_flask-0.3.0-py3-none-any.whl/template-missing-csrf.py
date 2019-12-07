import ast
import logging
import sys
from typing import List, Set

from flake8_flask.constants import MODULE_NAME
from flake8_flask.flask_base_visitor import FlaskBaseVisitor

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(stream=sys.stderr)
handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
logger.addHandler(handler)


FXN_NAME: str = "render_template"


class TemplateMissingCsrf(UnescapedTemplateFileExtensionsVisitor):
    def __init__(self, include_edge_cases=False):
        self.include_edge_cases = include_edge_cases
        super(TemplateMissingCsrf, self).__init__()

    name = "r2c-flask-wtf-template-missing-csrf"

    def visit_Call(self, call_node: ast.Call):
        # Is this flask.render_template?
        if not self.is_node_method_alias_of(call_node, FXN_NAME, MODULE_NAME):
            logger.debug(f"This call is not {FXN_NAME}")
            return

        # Check if the possible values aren't an autoescape extension
        arg0 = call_node.args[0]
        possible_values = self._resolve_to_possible_values(arg0)
        logger.debug(possible_values)
        if all([self._has_escaped_extension(value) for value in possible_values]):
            logger.debug(
                "Template has an escaped extension; template will be autoescaped"
            )
            return

        # If not autoescaped, check for escaped vars
        if all([self._is_kwarg_escaped(kw) for kw in call_node.keywords]):
            logger.debug("All context variables are escaped.")
            return

        # Edge cases
        if self.include_edge_cases:
            if self._edge_case_detect_return_content_type_with_text(call_node):
                logger.debug(
                    "Template is rendered with `text/plain` mimetype. Assuming this is safe."
                )
                return

        logger.debug(f"Found this node: {ast.dump(call_node)}")
        extensions = set(
            [self._get_template_extension(value) for value in possible_values]
        )
        extensions_to_go_in_message = extensions - escaped_extensions
        self.report_nodes.append(
            {
                "node": call_node,
                "message": f"{self.name} Flask does not autoescape templates with the {str(extensions_to_go_in_message)} extension by default. Flask only autoescapes .html, .htm, .xml, and .xhtml files. Make sure your variables are escaped using `flask.Markup.escape`.",
            }
        )
