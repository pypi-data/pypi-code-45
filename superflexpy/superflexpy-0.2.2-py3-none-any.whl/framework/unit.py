"""
Copyright 2019 Marco Dal Molin et al.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

This file is part of the SuperflexPy modelling framework. For details about it,
visit the page https://superflexpy.readthedocs.io

CODED BY: Marco Dal Molin
DESIGNED BY: Marco Dal Molin, Fabrizio Fenicia

This file contains the implementation of the Unit class.
"""

from copy import copy, deepcopy
from ..utils.common_class import CommonClass


class Unit(CommonClass):
    """
    This class defines a Unit. A unit can be part of a node and it is a
    collection of elements. It's task is to build the basic sructure,
    connecting different elements. Mathematically, it is a directed acyclic
    graph.
    """

    def __init__(self, layers, id, copy_pars=True):
        """
        This is the initializer of the class Unit.

        Parameters
        ----------
        layers : list(list(superflexpy.framework.element.BaseElement))
            This list defines the structure of the unit. The elements are
            arranged in layers (upstream to downstram) and each layer can
            contain multiple elements.
        id : str
            Itentifier of the unit. All the units of the framework must have an
            id.
        copy_pars : bool
            True if the parameters of the elements are copied instead of being
            shared among the different Units.
        """

        self._error_message = 'module : superflexPy, Unit : {},'.format(id)
        self._error_message += ' Error message : '

        if copy_pars:
            # Deep-copy the elements
            self._layers = []
            for l in layers:
                self._layers.append([])
                for el in l:
                    self._layers[-1].append(deepcopy(el))
        else:
            self._layers = layers

        self.id = id

        self._check_layers()
        self.add_prefix_parameters(id)
        self.add_prefix_states(id)
        self._construct_dictionary()

    # METHODS FOR THE USER

    def set_input(self, input):
        """
        This method sets the inputs to the unit.

        Parameters
        ----------
        input : list(numpy.ndarray)
            List of input fluxes.
        """

        self.input = input

    def get_output(self, solve=True):
        """
        This method solves the Unit, solving each Element and putting together
        their outputs according to the structure.

        Parameters
        ----------
        solve : bool
            True if the elements have to be solved (i.e. calcualte the states).

        Returns
        -------
        list(numpy.ndarray)
            List containig the output fluxes of the unit.
        """

        # Set the first layer (it must have 1 element)
        self._layers[0][0].set_input(self.input)

        for i in range(1, len(self._layers)):
            # Collect the outputs
            outputs = []
            for el in self._layers[i - 1]:
                if el.num_downstream == 1:
                    outputs.append(el.get_output(solve))
                else:
                    loc_out = el.get_output(solve)
                    for o in loc_out:
                        outputs.append(o)

            # Fill the inputs
            ind = 0
            for el in self._layers[i]:
                if el.num_upstream == 1:
                    el.set_input(outputs[ind])
                    ind += 1
                else:
                    loc_in = []
                    for _ in range(el.num_upstream):
                        loc_in.append(outputs[ind])
                        ind += 1
                    el.set_input(loc_in)

        # Return the output of the last element
        return self._layers[-1][0].get_output(solve)

    def append_layer(self, layer):
        """
        This method appends a layer to the structure.

        Parameters
        ----------
        layer : list(superflexpy.framework.elements.BaseElement)
            Layer to be appended.
        """

        self.insert_layer(layer, position=len(self._layers))

    def insert_layer(self, layer, position):
        """
        This method inserts a layer to the structure.

        Parameters
        ----------
        layer : list(superflexpy.framework.elements.BaseElement)
            Layer to be inserted.
        position : int
            Position where the layer is inserted.
        """

        layer_loc = []
        for el in layer:
            layer_loc.append(deepcopy(el))

        self._layers.insert(position, layer_loc)
        self._construct_dictionary()
        self._check_layers()

    def parse_structure(self, structure):
        raise NotImplementedError('Functionality in the TODO list')

    def get_internal(self, id, attribute):
        """
        This method allows to inspect attributes of the objects that belong to
        the unit.

        Parameters
        ----------
        id : str
            Id of the object.
        attribute : str
            Name of the attribute to expose.

        Returns
        -------
        Attribute exposed
        """

        return self._find_attribute_from_name(id, attribute)

    def call_internal(self, id, method, **kwargs):
        """
        This method allows to call methods of the objects that belong to the
        unit.

        Parameters
        ----------
        id : str
            Id of the object.
        method : str
            Name of the method to call.

        Returns
        -------
        Output of the called method.
        """

        method = self._find_attribute_from_name(id, method)
        return method(**kwargs)

    # METHODS USED BY THE FRAMEWORK

    def add_prefix_parameters(self, id):
        """
        This method adds the prefix to the states of the elements that are
        contained in the unit.

        Parameters
        ----------
        id : str
            Prefix to add.
        """

        for l in self._layers:
            for el in l:
                try:
                    el.add_prefix_parameters(id)
                except AttributeError:
                    continue

    def add_prefix_states(self, id):
        """
        This method adds the prefix to the states of the elements that are
        contained in the unit.

        Parameters
        ----------
        id : str
            Prefix to add.
        """

        # add the Prefix to the elements
        for l in self._layers:
            for el in l:
                try:
                    el.add_prefix_states(id)
                except AttributeError:
                    continue

    # PROTECTED METHODS

    def _construct_dictionary(self):

        self._content_pointer = {}

        for i in range(len(self._layers)):
            for j in range(len(self._layers[i])):
                if self._layers[i][j].id in self._content_pointer:
                    message = '{}The element {} already exist.'.format(self._error_message, self._layers[i][j].id)
                    raise KeyError(message)
                self._content_pointer[self._layers[i][j].id] = (i, j)

        self._content = {}
        for k in self._content_pointer.keys():
            l, el = self._content_pointer[k]
            self._content[(l, el)] = self._layers[l][el]

    def _find_attribute_from_name(self, id, function):
        # Search the element
        (l, el) = self._find_content_from_name(id)
        element = self._layers[l][el]

        # Call the function on the element
        try:
            method = getattr(element, function)
        except AttributeError:
            message = '{}the method {} does not exist.'.format(self._error_message, function)
            raise AttributeError(message)

        return method

    def _check_layers(self):

        # Check layer 0
        if len(self._layers[0]) != 1:
            message = '{}layer 0 has {} elements.'.format(self._error_message, len(self._layers[0]))
            raise ValueError(message)

        if self._layers[0][0].num_upstream != 1:
            message = '{}The element in layer 0 has {} upstream elements.'.format(self._error_message, len(self._layers[0][0].num_upstream))
            raise ValueError(message)

        # Check the other layers
        for i in range(1, len(self._layers)):
            num_upstream = 0
            num_downstream = 0
            for el in self._layers[i - 1]:
                num_downstream += el.num_downstream
            for el in self._layers[i]:
                num_upstream += el.num_upstream

            if num_downstream != num_upstream:
                message = '{}Downstream : {}, Upstream : {}'.format(self._error_message, num_downstream, num_upstream)
                raise ValueError(message)

        # Check last layer
        if len(self._layers[-1]) != 1:
            message = '{}last layer has {} elements.'.format(self._error_message, len(self._layers[-1]))
            raise ValueError(message)

        if self._layers[-1][0].num_downstream != 1:
            message = '{}The element in the last layer has {} downstream elements.'.format(self._error_message, len(self._layers[-1][0].num_downstream))
            raise ValueError(message)

    # MAGIC METHODS

    def __copy__(self):
        layers = []
        for l in self._layers:
            layers.append([])
            for el in l:
                layers[-1].append(copy(el))
        return self.__class__(layers=layers,
                              id=self.id,
                              copy_pars=False)  # False because the copy is customized here

    def __deepcopy__(self, memo):
        return self.__class__(layers=self._layers,
                              id=self.id,
                              copy_pars=True)  # init already implements deepcopy

    def __repr__(self):
        str = 'Module: superflexPy\nUnit: {}\n'.format(self.id)
        str += 'Layers:\n'
        id_layer = []
        for l in self._layers:
            id_layer.append([])
            for el in l:
                id_layer[-1].append(el.id)

        str += '\t{}\n'.format(id_layer)

        for l in self._layers:
            for el in l:
                str += '********************\n'
                str += el.__repr__()
                str += '\n'

        return str
