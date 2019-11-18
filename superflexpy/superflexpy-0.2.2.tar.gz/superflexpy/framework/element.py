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

This file contains the implementation of Element classes with different levels
of specialization.
"""

from copy import deepcopy, copy
import numpy as np


class BaseElement():
    """
    This is the abstract class for the cration of a BaseElement. A BaseElement
    does not have parameters or states.
    """

    _num_downstream = None
    _num_upstream = None
    input = {}

    def __init__(self, id):
        """
        This is the initializer of the abstract class BaseElement.

        Parameters
        ----------
        id : str
            Itentifier of the element. All the elements of the framework must
            have an id.
        """

        self.id = id
        self._error_message = 'module : superflexPy, Element : {},'.format(id)
        self._error_message += ' Error message : '

    def set_input(self, input):
        """
        To be implemented by any child class. It should transform a list of
        numpy arrays in a dictionary.

        Parameters
        ----------
        input : list(numpy.ndarray)
            List of input fluxes to the element.
        """

        raise NotImplementedError('The set_input method must be implemented')

    def get_output(self, solve=True):
        """
        To be implemented by any child class. It solves the element and returns
        the output fluxes.

        Parameters
        ----------
        solve : bool
            True if the element has to be solved (i.e. calcualte the states).

        Returns
        -------
        list(numpy.ndarray)
            List of output fluxes.
        """

        raise NotImplementedError('The get_output method must be implemented')

    @property
    def num_downstream(self):
        """
        Number of downstream elements.
        """

        return self._num_downstream

    @property
    def num_upstream(self):
        """
        Number of upstream elements
        """

        return self._num_upstream

    def __repr__(self):

        str = 'Module: superflexPy\nElement: {}\n'.format(self.id)
        return str

    def __copy__(self):
        ele = self.__class__(id=self.id)
        return ele

    def __deepcopy__(self, memo):
        ele = self.__class__(id=self.id)
        return ele


class ParameterizedElement(BaseElement):
    """
    This is the abstract class for the cration of a ParameterizedElement. A
    ParameterizedElement has parameters but not states.
    """

    _prefix_parameters = ''

    def __init__(self, parameters, id):
        """
        This is the initializer of the abstract class ParameterizedElement.

        Parameters
        ----------
        parameters : dict
            Parameters controlling the element. The parameters can be either
            a float (constant in time) or a numpy.ndarray of the same length
            of the input fluxes (time variant parameters).
        id : str
            Itentifier of the element. All the elements of the framework must
            have an id.
        """

        BaseElement.__init__(self, id)

        self._parameters = parameters
        self.add_prefix_parameters(id)

    def get_parameters(self, names=None):
        """
        This method returns the parameters of the element.

        Parameters
        ----------
        names : list(str)
            Names of the parameters to return. The names must be the ones
            returned by the mehod get_parameters_name. If None, all the
            parameters are returned.

        Returns
        -------
        dict:
            Parameters of the element.
        """

        if names is None:
            return self._parameters
        else:
            return {n: self._parameters[n] for n in names}

    def get_parameters_name(self):
        """
        This method returns the names of the parameters of the element.

        Returns
        -------
        list(str):
            List with the names of the parameters.
        """

        return list(self._parameters.keys())

    def set_parameters(self, parameters):
        """
        This method sets the values of the parameters.

        Parameters
        ----------
        parameters : dict
            Contains the parameters of the element to be set. The keys must be
            the ones returned by the method get_parameters_name. Only the
            parameters that have to be changed should be passed.
        """

        for k in parameters.keys():
            if k not in self._parameters.keys():
                message = '{}The parameter {} does not exist'.format(self._error_message, k)
                raise KeyError(message)
            self._parameters[k] = parameters[k]

    def add_prefix_parameters(self, prefix):
        """
        This method add a prefix to the name of the parameters of the element.

        Parameters
        ----------
        prefix : str
            Prefix to be added. It cannot contain '_'.
        """

        if '_' in prefix:
            message = '{}The prefix cannot contain \'_\''.format(self._error_message)
            raise ValueError(message)

        # Extract the prefixes in the parameters name
        splitted = list(self._parameters.keys())[0].split('_')

        if prefix not in splitted:
            # Apply the prefix
            for k in list(self._parameters.keys()):
                value = self._parameters.pop(k)
                self._parameters['{}_{}'.format(prefix, k)] = value

            # Save the prefix for furure uses
            self._prefix_parameters = '{}_{}'.format(prefix, self._prefix_parameters)

    def __repr__(self):

        str = 'Module: superflexPy\nElement: {}\n'.format(self.id)
        str += 'Parameters:\n'
        for k in self._parameters:
            str += '\t{} : {}\n'.format(k, self._parameters[k])

        return str

    def __copy__(self):
        p = self._parameters  # Only the reference
        ele = self.__class__(parameters=p,
                             id=self.id)
        ele._prefix_parameters = self._prefix_parameters
        return ele

    def __deepcopy__(self, memo):
        p = deepcopy(self._parameters)  # Create a new dictionary
        ele = self.__class__(parameters=p,
                             id=self.id)
        ele._prefix_parameters = self._prefix_parameters
        return ele


class StateElement(BaseElement):
    """
    This is the abstract class for the cration of a StateElement. A
    StateElement has states but not parameters.
    """

    _prefix_states = ''

    def __init__(self, states, id):
        """
        This is the initializer of the abstract class StateElement.

        Parameters
        ----------
        states : dict
            Initial states of the element. Depending on the element the states
            can be either a float or a numpy.ndarray.
        id : str
            Itentifier of the element. All the elements of the framework must
            have an id.
        """
        BaseElement.__init__(self, id)

        self._states = states
        self._init_states = deepcopy(states)  # It is used to re-set the states
        self.add_prefix_states(id)

    def get_states(self, names=None):
        """
        This method returns the states of the element.

        Parameters
        ----------
        names : list(str)
            Names of the states to return. The names must be the ones
            returned by the mehod get_states_name. If None, all the
            states are returned.

        Returns
        -------
        dict:
            States of the element.
        """

        if names is None:
            return self._states
        else:
            return {n: self._states[n] for n in names}

    def get_states_name(self):
        """
        This method returns the names of the states of the element.

        Returns
        -------
        list(str):
            List with the names of the states.
        """

        return list(self._states.keys())

    def set_states(self, states):
        """
        This method sets the values of the states.

        Parameters
        ----------
        states : dict
            Contains the states of the element to be set. The keys must be
            the ones returned by the method get_states_name. Only the
            states that have to be changed should be passed.
        """

        for k in states.keys():
            if k not in self._states.keys():
                message = '{}The state {} does not exist'.format(self._error_message, k)
                raise KeyError(message)
            self._states[k] = states[k]

    def reset_states(self):
        """
        This method sets the states to the values provided to the __init__
        method. If a state was initialized as None, it will not be reset.
        """

        for k in self._init_states.keys():
            k_no_prefix = k.split('_')[-1]
            if self._init_states[k] is not None:
                self._states[self._prefix_states + k_no_prefix] = deepcopy(self._init_states[k])  # I have to isolate

    def add_prefix_states(self, prefix):
        """
        This method add a prefix to the id of the states of the element.

        Parameters
        ----------
        prefix : str
            Prefix to be added. It cannot contain '_'.
        """

        if '_' in prefix:
            message = '{}The prefix cannot contain \'_\''.format(self._error_message)
            raise ValueError(message)

        # Extract the prefixes in the parameters name
        splitted = list(self._states.keys())[0].split('_')

        if prefix not in splitted:
            # Apply the prefix
            for k in list(self._states.keys()):
                value = self._states.pop(k)
                self._states['{}_{}'.format(prefix, k)] = value

            # Save the prefix for furure uses
            self._prefix_states = '{}_{}'.format(prefix, self._prefix_states)

    def __repr__(self):

        str = 'Module: superflexPy\nElement: {}\n'.format(self.id)
        str += 'States:\n'
        for k in self._states:
            str += '\t{} : {}\n'.format(k, self._states[k])

        return str

    def __copy__(self):
        s = deepcopy(self._states)  # Create a new dictionary
        ele = self.__class__(states=s,
                             id=self.id)
        ele._prefix_states = self._prefix_states
        return ele

    def __deepcopy__(self, memo):
        s = deepcopy(self._states)  # Create a new dictionary
        ele = self.__class__(states=s,
                             id=self.id)
        ele._prefix_states = self._prefix_states
        return ele


class StateParameterizedElement(StateElement, ParameterizedElement):
    """
    This is the abstract class for the cration of a StateParameterizedElement.
    A StateParameterizedElement has parameters and states.
    """

    def __init__(self, parameters, states, id):
        """
        This is the initializer of the abstract class
        StateParameterizedElement.

        Parameters
        ----------
        parameters : dict
            Parameters controlling the element. The parameters can be either
            a float (constant in time) or a numpy.ndarray of the same length
            of the input fluxes (time variant parameters).
        states : dict
            Initial states of the element. Depending on the element the states
            can be either a float or a numpy.ndarray.
        id : str
            Itentifier of the element. All the elements of the framework must
            have an id.
        """

        StateElement.__init__(self, states, id)
        ParameterizedElement.__init__(self, parameters, id)

    def __repr__(self):

        str = 'Module: superflexPy\nElement: {}\n'.format(self.id)
        str += 'Parameters:\n'
        for k in self._parameters:
            str += '\t{} : {}\n'.format(k, self._parameters[k])
        str += 'States:\n'
        for k in self._states:
            str += '\t{} : {}\n'.format(k, self._states[k])

        return str

    def __copy__(self):
        p = self._parameters  # Only the reference
        s = deepcopy(self._states)  # Create a new dictionary
        ele = self.__class__(parameters=p,
                             states=s,
                             id=self.id)
        ele._prefix_states = self._prefix_states
        ele._prefix_parameters = self._prefix_parameters
        return ele

    def __deepcopy__(self, memo):
        p = deepcopy(self._parameters)  # Create a new dictionary
        s = deepcopy(self._states)  # Create a new dictionary
        ele = self.__class__(parameters=p,
                             states=s,
                             id=self.id)
        ele._prefix_states = self._prefix_states
        ele._prefix_parameters = self._prefix_parameters
        return ele


class ODEsElement(StateParameterizedElement):
    """
    This is the abstract class for the cration of a ODEsElement. An ODEsElement
    is an element with states and parameters that is controlled by an ordinary
    differential equation, of the form:

    dS/dt = input - output
    """
    _num_upstream = 1
    _num_downstream = 1
    _solver_states = []

    def __init__(self, parameters, states, solver, id):
        """
        This is the initializer of the abstract class ODEsElement.

        Parameters
        ----------
        parameters : dict
            Parameters controlling the element. The parameters can be either
            a float (constant in time) or a numpy.ndarray of the same length
            of the input fluxes (time variant parameters).
        states : dict
            Initial states of the element. Depending on the element the states
            can be either a float or a numpy.ndarray.
        solver : superflexpy.utils.root_finder.RootFinder
            Solver used to find the root(s) of the differential equation(s).
            Child classes may implement their own solver, therefore the tipe
            of the solver is not enforced.
        id : str
            Itentifier of the element. All the elements of the framework must
            have an id.
        """

        StateParameterizedElement.__init__(self, parameters=parameters,
                                           states=states, id=id)

        self._solver = solver

    def set_timestep(self, dt):
        """
        This method sets the timestep used by the element.

        Parameters
        ----------
        dt : float
            Timestep
        """
        self._dt = dt

    def get_timestep(self):
        """
        This method returns the timestep used by the element.

        Returns
        -------
        float
            Timestep
        """
        return self._dt

    def define_solver(self, solver):
        """
        This method define the solver to use for the differential equation.

        Parameters
        ----------
        solver : superflexpy.utils.root_finder.RootFinder
            Solver used to find the root(s) of the differential equation(s).
            Child classes may implement their own solver, therefore the tipe
            of the solver is not enforced.
        """

        self._solver = solver

    def _solve_differential_equation(self, **kwargs):
        if len(self._solver_states) == 0:
            message = '{}the attribute _solver_states must be filled'.format(self._error_message)
            raise ValueError(message)

        self.state_array = self._solver.solve(fun=self._differential_equation,
                                              S0=self._solver_states,
                                              dt=self._dt,
                                              **self.input,
                                              **{k[len(self._prefix_parameters):]: self._parameters[k] for k in self._parameters},
                                              **kwargs)

    def _differential_equation(self):
        """
        To be implemented by any child class. This method sets the differential
        equation(s) to be solved by the solver. The method must be implemented
        in order to satisfy the requirements of the solver.
        """

        raise NotImplementedError('The _differential_equation method must be implemented')

    def __copy__(self):
        p = self._parameters  # Only the reference
        s = deepcopy(self._states)  # Create a new dictionary
        ele = self.__class__(parameters=p,
                             states=s,
                             id=self.id,
                             solver=self._solver)
        ele._prefix_states = self._prefix_states
        ele._prefix_parameters = self._prefix_parameters
        return ele

    def __deepcopy__(self, memo):
        p = deepcopy(self._parameters)  # Create a new dictionary
        s = deepcopy(self._states)  # Create a new dictionary
        ele = self.__class__(parameters=p,
                             states=s,
                             id=self.id,
                             solver=self._solver)
        ele._prefix_states = self._prefix_states
        ele._prefix_parameters = self._prefix_parameters
        return ele


class LagElement(StateParameterizedElement):
    """
    This is the abstract class for the cration of a LagElement. An LagElement
    is an element with states and parameters that distributes the incoming
    fluxes according to a weight array

    Parameters must be called:
    - 'lag-time': characteristic time of the lag. Its definition depends on the
                  specific implementations of the element. It can be a scalar
                  (it will be applied to all the fluxes) of a list (with length
                  equal to the number of fluxes).

    States must be called:
    - lag: initial state of the lag function. If None it will be initialized
           to zeros. It can be a numpy.ndarray (it will be applied to all the
           fluxes) of a list on numpy.ndarray (with length equal to the number
           of fluxes).
    """

    _num_upstream = 1
    _num_downstream = 1

    def _build_weight(self, lag_time):
        """
        This method must be implemented by any child class. It calculates the
        weight array(s) based on th lag_time.

        Returns
        -------
        list(numpy.ndarray)
            List of weight array(s).
        """

        raise NotImplementedError('The _build_weight method must be implemented')

    def set_input(self, input):
        """
        This method sets the inputs to the elements. Since the name of the
        inputs is not important, the fluxes are stored as list.

        Parameters
        input : list(numpy.ndarray)
            List of input fluxes.
        """

        self.input = input

    def get_output(self, solve=True):
        """
        This method returns the output of the LagElement. It applies the lag
        to all the incoming fluxes, according to the weight array(s).

        Parameters
        ----------
        solve : bool
            True if the element has to be solved (i.e. calcualte the states).

        Returns
        -------
        list(numpy.ndarray)
            List of output fluxes.
        """

        if solve:

            # Create lists if we are dealing with scalars
            if isinstance(self._parameters[self._prefix_parameters + 'lag-time'], float):
                lag_time = [self._parameters[self._prefix_parameters + 'lag-time']] * len(self.input)
            elif isinstance(self._parameters[self._prefix_parameters + 'lag-time'], list):
                lag_time = self._parameters[self._prefix_parameters + 'lag-time']
            else:
                par_type = type(self._parameters[self._prefix_parameters + 'lag-time'])
                message = '{}lag_time parameter of type {}'.format(self._error_message, par_type)
                raise TypeError(message)

            if self._states[self._prefix_states + 'lag'] is None:
                lag_state = self._init_lag_state(lag_time)
            else:
                if isinstance(self._states[self._prefix_states + 'lag'], np.ndarray):
                    lag_state = [copy(self._states[self._prefix_states + 'lag'])] * len(self.input)
                elif isinstance(self._states[self._prefix_states + 'lag'], list):
                    lag_state = self._states[self._prefix_states + 'lag']
                else:
                    state_type = type(self._states[self._prefix_states + 'lag'])
                    message = '{}lag state of type {}'.format(self._error_message, state_type)
                    raise TypeError(message)

            self._weight = self._build_weight(lag_time)

            self.state_array = self._solve_lag(self._weight, lag_state, self.input)

            # Get the new lag value to restart
            final_states = self.state_array[-1, :, :]
            final_states[:, :-1] = final_states[:, 1:]
            final_states[:, -1] = 0

            self.set_states({self._prefix_states + 'lag': [final_states[i, :len(w)] for i, w in enumerate(self._weight)]})

        return [self.state_array[:, i, 0] for i in range(len(self.input))]

    @staticmethod
    def _solve_lag(weight, lag_state, input):

        max_length = max([len(w) for w in weight])

        output = np.zeros((len(input[0]), len(weight), max_length))  # num_ts, num_fluxes, len_lag

        for flux_num, (w, ls, i) in enumerate(zip(weight, lag_state, input)):
            for ts in range(len(input[0])):
                updated_state = ls + i[ts] * w
                output[ts, flux_num, :len(w)] = updated_state[:]
                ls = np.append(updated_state[1:], 0)

        return output

    def _init_lag_state(self, lag_time):

        ini_state = []
        for i in range(len(self.input)):
            ini_state.append(np.zeros(int(np.ceil(lag_time[i]))))
        return ini_state
