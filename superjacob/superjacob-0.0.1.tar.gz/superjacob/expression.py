"""
expression.py

Classes:
    Var
        - Base class for individual variables
    Expression
        - Inherits from Var
        - Can be combined into larger expressions
"""
from typing import Union
from numbers import Number

import numpy as np

import superjacob as sj


class Var:
    """A Variable.

    Attributes:
        :name: str -- The common name for the variable (e.g. 'x', 'y', 'x1')

    Methods:
        eval () -> Number -- Evaluate the variable for a given input (always return the number itself)

    """
    def __init__(self, name, length=1):
        self._vars = None
        self.name = name
        self.length = length

    def eval(self, x: Union[Number, np.ndarray]):
        """
        Evaluate the variable at x (identity function)

        :param x: Number|np.ndarray -- The point to evaluate the Var at
        :return: Number -- The number x itself
        """
        self._check_length(x)
        return x

    def deriv(self, x: Union[bool, Number, np.ndarray], var=None) -> Union[Number, np.ndarray]:
        """Evaluate the derivative of this variable.

        `x` is a boolean indicator variable
            True (or non-zero) if this variable is being differentiated
            False (or zero) if this variable is not being differentiated

        :param x: bool | Number | np.ndarray -- Whether the derivative is being taken with
            respect to this variable
        :param var: Var -- The variable with respect to which the derivative is being taken
        :return: int | np.ndarray -- 1 or 0 (or array of ones with dimension `self.length`)
        """
        self._check_length(x)
        if x is not None:
            if self.length == 1:
                return 1
            else:
                return np.ones(self.length)
        else:
            return 0

    def _check_length(self, x):
        try:
            assert len(x) == self.length, f'Incorrect input size (required: {self.length}, given: {len(x)}'
        except TypeError:  # Assuming that this is a single number
            assert self.length == 1, f'Incorrect input size (required: {self.length}, given: 1'

    @property
    def vars(self):
        return [self]

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
        
    def __call__(self, *args, **kwargs):
        return self.eval(*args)

    def __add__(self, other):
        return sj.add(self, other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return sj.sub(self, other)

    def __rsub__(self, other):
        return sj.sub(other, self)

    def __mul__(self, other):
        return sj.mul(self, other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return sj.div(self, other)

    def __rtruediv__(self, other):
        return sj.div(other, self)

    def __pow__(self, power):
        return sj.pow(self, power)

    def __rpow__(self, base):
        return sj.pow(base, self)

    def __neg__(self):
        return sj.neg(self)

    # It's dangerous to compare just based on the name attribute
    # def __eq__(self, other):
    #     return self.name == other.name

    def __hash__(self):
        # BEWARE: This might be buggy
        return hash(id(self))

    def dot(self, other):
        return sj.dot(self, other)


class Expression(Var):
    def __init__(self, parent1, parent2, operation, varlist=None):
        """
        Initialize an Expression.

        :param parent1: First parent Expression
        :param parent2: Second parent Expression
        :param operation: Operation to combine the two parents
        :param varlist: List of Var objects
            Must be in the same order in which numbers will be passed in upon
            evaluation or differentiation of the Expression
        """
        super().__init__('f')
        self.parent1 = parent1
        self.parent2 = parent2
        self.parents = [self.parent1, self.parent2]
        self.operation = operation
        if varlist is None:
            self._vars = self._get_parent_vars(self.parent1)
            self._vars += [v for v in self._get_parent_vars(self.parent2) if v not in self._vars]
        else:
            self._vars = varlist
        self.matched_vars = self._match_vars_to_parents()

    def set_vars(self, varlist):
        self._vars = varlist
        self.matched_vars = self._match_vars_to_parents()

    @property
    def vars(self):
        return self._vars

    @vars.setter
    def vars(self, varlist):
        # Call set_vars here
        self.set_vars(varlist)

    def _match_vars_to_parents(self):
        """Matches variables to parent1 and parent2
        :return: list[tuple] -- Mapping of vars -> parent Expression objects
        """
        matched_vars = {}
        for var in self.vars:
            parents_of_var = []
            for parent in self.parents:
                if var in self._get_parent_vars(parent):
                    parents_of_var.append(parent)
            matched_vars[var] = parents_of_var
        return matched_vars

    def eval(self, *args):
        """Evaluate this Expression at the specified point

        TODO: Deal with unary operations

        :param args: tuple of values to evaluate the Expression at
        :return: Result (length depends on dimensionality of co-domain)
        """
        if self.parent2 is None:
            return self._unary_eval(*args)
        else:
            return self._binary_eval(*args)

    def deriv(self, *args, mode='forward', var=None):
        """Differentiate this Expression at the specified point.

        Currently just runs forward mode.

        #TODO: Deal with vector outputs
        #TODO: Reverse mode!

        :param args: tuple -- values to evaluate the Expression at
        :param mode: str -- Whether to run in forward or reverse mode
            (possible options: {'forward', 'reverse', 'auto'})
        :param var: Var -- Variable to take derivative with respect to
            Default: None (gets entire Jacobian)
        :return: tuple(Number) | Number -- Result (length depends on dimensionality of co-domain)
        """
        assert mode in ('forward', 'reverse', 'auto'), f'Invalid model specified: {mode}. ' \
                                                       f'Please choose one of "forward", "reverse", "auto".'
        if mode == 'auto':
            if len(self.vars) > 1:
                mode = 'reverse'
            else:
                mode = 'forward'
        if mode == 'forward':
            if var is None:
                res = []
                for var in self.vars:
                    res.append(self._deriv(var, mode, *args))
                if len(res) == 1:
                    return res[0]
                else:
                    return np.array(res)
            else:
                return self._deriv(var, mode, *args)
        else:
            rev = sj.reverse(self)
            return rev(*args, var=var)

    def _deriv(self, var, mode, *args):
        if self.parent2 is None:
            return self._unary_deriv(*args, mode=mode, var=var)
        else:
            return self._binary_deriv(*args, mode=mode, var=var)

    def _unary_eval(self, *args):
        return self.operation.eval(self._eval_parent(self.parent1, *args))

    def _binary_eval(self, *args):
        p1_args, p2_args = self._parse_args(*args)
        return self.operation.eval(self._eval_parent(self.parent1, *p1_args), self._eval_parent(self.parent2, *p2_args))

    def _unary_deriv(self, *args, mode='forward', var=None):
        res = self.operation.deriv(self._eval_parent(self.parent1, *args),
                                   self._deriv_parent(self.parent1, var, *args))
        return res

    def _binary_deriv(self, *args, mode='forward', var=None):
        p1_args, p2_args = self._parse_args(*args)
        res = self.operation.deriv(self._eval_parent(self.parent1, *p1_args),  # Evaluate and store once
                                   self._deriv_parent(self.parent1, var, *p1_args),
                                   self._eval_parent(self.parent2, *p2_args),
                                   self._deriv_parent(self.parent2, var, *p2_args))
        return res

    def _get_input_args(self, parent, *args):
        """Parse the arguments in terms of the ordering for the parent

        :param parent: Parent Expression to be evaluated
        :param args: Arguments in order of self.vars
        :return: list[Var]
        """
        return get_input_args(parent, self.vars, *args)

    def _check_input_length(self, *args):
        """Check that the input length matches this function's domain dimensionality.

        :param args: Input arguments
        :return: None

        :raises: AssertionError
        """
        assert len(args) == len(self.vars), \
            f'Input length does not match dimension of Expression domain ({len(args)}, {len(self.vars)})'

    def _parse_args(self, *args):
        """Check input length and parse arguments in correct order for each parent.

        :param args: tuple[Numeric] -- Arguments to be parsed
        :return: (tuple[Numeric], tuple[Numeric]) -- p1_args and p2_args
        """
        self._check_input_length(*args)
        p1_args = self._get_input_args(self.parent1, *args)
        p2_args = self._get_input_args(self.parent2, *args)
        return p1_args, p2_args

    @staticmethod
    def _get_parent_vars(parent: Union[Var, Number, None]):
        """Get the vars for given parent

        :param parent: Var | Number | None -- The parent of interest
        :return: list[Var]
        """
        if parent is None or isinstance(parent, Number):
            return []
        else:
            return parent.vars[:]

    @staticmethod
    def _eval_parent(parent: Union[Var, Number], *args) -> Number:
        """Evaluate a parent at `args`, checking if the parent is None or a Number

        :param parent: Var | Number | None -- The parent to evaluate
        :return: Number
        """
        if not isinstance(parent, Var):
            return parent
        else:
            return parent(*args)

    @staticmethod
    def _deriv_parent(parent: Union[Var, Number], var: Var, *args) -> Number:
        """Evaluate derivative of a parent at `args`, checking if the parent is a Number

        :param parent: The parent of interest
        :param var: Var -- Variable with respect to which the derivative is
            being taken
        :param args: Point to differentiate parent at
        :return: Number
        """
        if isinstance(parent, Var):
            if var in parent.vars:
                return parent.deriv(*args, var=var)
        return 0

    def __call__(self, *args, **kwargs):
        return self.eval(*args)

    def __str__(self):
        # TODO: Make this more informative
        if self.parent2 is None:
            return self.operation.opstr(self.parent1)
        else:
            return self.operation.opstr(self.parent1, self.parent2)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __hash__(self):
        # BEWARE: This might be buggy
        # For some reason this isn't inherited from Var...
        return hash(id(self))


class VectorExpression:
    """
    A wrapper expression that can handle vector-valued outputs
    """
    def __init__(self, expressions, varlist):
        self._vars = varlist
        self._expressions = self._match_vars_to_expressions(varlist, expressions)

    @property
    def vars(self):
        return self._vars

    @vars.setter
    def vars(self, varlist):
        self._vars = varlist
        self._expressions = self._match_vars_to_expressions(varlist, self._expressions.keys())  # This might not work

    def eval(self, *args):
        return [e(*self._get_expr_args(e, *args)) for e in self._expressions]

    def deriv(self, *args, mode='forward', var=None):
        res = np.zeros((len(self._expressions), len(self._vars)))
        for i, (e, v) in enumerate(self._expressions.items()):
            expr_args = self._get_expr_args(e, *args)
            expr_deriv = e.deriv(*expr_args, mode=mode)
            res[i, :] = self._parse_results(expr_deriv, v)
        return res

    def _get_expr_args(self, expr, *args):
        expr_vars_idx = self._expressions.get(expr, [])
        res = []
        for idx in expr_vars_idx:
            res.append(args[idx])
        return res

    def _parse_results(self, result_set, expr_vars):
        res = np.zeros(len(self._vars))
        res[expr_vars] = result_set
        return res

    @staticmethod
    def _match_vars_to_expressions(varlist, expressions):
        return {expr: VectorExpression._get_var_order(varlist, expr) for expr in expressions}

    @staticmethod
    def _get_var_order(varlist, expr):
        if not isinstance(expr, Var):
            return []
        var_order = [varlist.index(var) for var in expr.vars]
        return var_order

    def __call__(self, *args, **kwargs):
        return self.eval(*args)

    def __repr__(self):
        return '(' + ', '.join([str(e) for e in self._expressions.keys()]) + ')'

    def __str__(self):
        return repr(self)

def get_input_args(expression, varlist, *args):
    """Parse the arguments in terms of the ordering for the parent

    :param expression: Expression to be evaluated
    :param varlist: Ordered list of variables that matches `args`
    :param args: Arguments in order of self.vars
    :return: list[Var]
    """
    if not isinstance(expression, Var):
        return []
    input_args = [args[varlist.index(parent_var)] for parent_var in expression.vars]
    return input_args
