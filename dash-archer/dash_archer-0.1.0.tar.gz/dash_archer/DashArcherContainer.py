# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashArcherContainer(Component):
    """A DashArcherContainer component.
DashArcherContainer component is a wrapper for ArcherContainer component
from react-archer module. See usage: https://github.com/pierpo/react-archer

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- arrowLength (number; optional): A size in px.
- arrowThickness (number; optional): A size in px.
- id (string; optional): The ID used to identify this component in Dash callbacks.
- noCurves (boolean; optional): Set this to true if you want angles instead of curves.
- offset (number; optional): Optional number for space between element and start/end of stroke.
- strokeColor (string; optional): A color string '#ff0000'.
- strokeDasharray (string; optional): Adds dashes to the stroke. It has to be a string representing an array
of sizes. See https://www.w3schools.com/graphics/svg_stroking.asp
- strokeWidth (number; optional): A size in px."""
    @_explicitize_args
    def __init__(self, children=None, arrowLength=Component.UNDEFINED, arrowThickness=Component.UNDEFINED, id=Component.UNDEFINED, noCurves=Component.UNDEFINED, offset=Component.UNDEFINED, strokeColor=Component.UNDEFINED, strokeDasharray=Component.UNDEFINED, strokeWidth=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'arrowLength', 'arrowThickness', 'id', 'noCurves', 'offset', 'strokeColor', 'strokeDasharray', 'strokeWidth']
        self._type = 'DashArcherContainer'
        self._namespace = 'dash_archer'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'arrowLength', 'arrowThickness', 'id', 'noCurves', 'offset', 'strokeColor', 'strokeDasharray', 'strokeWidth']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashArcherContainer, self).__init__(children=children, **args)
