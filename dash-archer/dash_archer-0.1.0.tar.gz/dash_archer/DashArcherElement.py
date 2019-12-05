# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashArcherElement(Component):
    """A DashArcherElement component.
DashArcherElement component is a wrapper for ArcherElement component
from react-archer module. See usage: https://github.com/pierpo/react-archer

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional): The ID used to identify this component in Dash callbacks.
- relations (dict; optional): The relations specify where arrows are drawn. relations has the following type: list of dicts containing keys 'targetId', 'targetAnchor', 'sourceAnchor', 'label', 'style'.
Those keys have the following types:
  - targetId (string; optional)
  - targetAnchor (a value equal to: 'top', 'bottom', 'left', 'right'; optional)
  - sourceAnchor (a value equal to: 'top', 'bottom', 'left', 'right'; optional)
  - label (a list of or a singular dash component, string or number; optional)
  - style (dict; optional): style has the following type: dict containing keys 'arrowLength', 'arrowThickness', 'noCurves', 'strokeColor', 'strokeWidth', 'strokeDasharray'.
Those keys have the following types:
  - arrowLength (number; optional)
  - arrowThickness (number; optional)
  - noCurves (boolean; optional)
  - strokeColor (string; optional)
  - strokeWidth (number; optional)
  - strokeDasharray (number; optional)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, relations=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'relations']
        self._type = 'DashArcherElement'
        self._namespace = 'dash_archer'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'relations']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashArcherElement, self).__init__(children=children, **args)
