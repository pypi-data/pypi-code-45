"""
Implementing reverse mode differentiation
"""
from numbers import Number

import numpy as np

from superjacob.expression import Expression, get_input_args


class ReverseDiff:
    """
    Class implementing reverse mode differentiation
    """

    def __init__(self, expr):
        self.expr = expr
        self.vars = expr.vars
        self.trace = []

    def forward(self, expr, *args, child=None):
        """Compute the forward pass of reverse mode differentiation

        :param expr: Var -- Expression to be differentiated
        :param args: tuple -- Arguments to differentiate the expression at
        :param child: Expression -- The last node visited in the trace (child of current expr)
        :return: Number -- evaluated expression
        """
        if expr is None:
            return None
        if isinstance(expr, Number):
            return expr
        if expr in self.trace:  # Here we check if we have already visited this node
            self._add_child(expr, child)
            return args[0]
        if not isinstance(expr, Expression):
            node = TraceNode(expr, args[0], [1])
            node.add_child(child)
            self.trace.append(node)
            return args[0]
        else:
            # Parsing args
            p1_args, p2_args = get_input_args(expr.parent1, expr.vars, *args), \
                               get_input_args(expr.parent2, expr.vars, *args)

            node = TraceNode(expr, child=child)

            parvals = self.forward(expr.parent1, *p1_args, child=node), \
                      self.forward(expr.parent2, *p2_args, child=node)

            # For now, implementing unary/binary as an if-statement. Consider subclassing
            if parvals[1] is None:
                currval = expr.operation.eval(parvals[0])
                d1val = expr.operation.reverse(parvals[0])
                derivs = [d1val]
            else:
                currval = expr.operation.eval(*parvals)
                derivs = expr.operation.reverse(*parvals)
            node.currval = currval
            node.derivs = derivs

            self.trace.append(node)
            return currval

    def reverse(self, var=None):
        """Compute the reverse pass of forward mode differentiation

        :param var: Var -- The variable with respect to which the derivative is taken
        :return: gradient
        """
        res = np.zeros(len(self.vars))
        for node in self.trace[::-1]:
            node_bar = node.bar
            if node in self.vars:
                if var and node == var:
                    return node_bar
                res[self.vars.index(node)] = node_bar
        return res

    def _add_child(self, parent, child):
        if child:
            self.trace[self.trace.index(parent)].add_child(child)

    def __call__(self, *args, **kwargs):
        self.forward(self.expr, *args)
        return self.reverse(**kwargs)


class TraceNode:
    """
    A lightweight class for storing elements of the evaluation trace.
    """

    def __init__(self, expr, currval=None, derivs=[], child=None):
        self.expr = expr
        self.currval = currval
        self.derivs = derivs
        if child is None:
            self.children = []
        else:
            self.children = [child]
        self._bar = None

    def add_child(self, child):
        if child:
            self.children.append(child)

    @property
    def bar(self):
        if self._bar:
            return self._bar
        if not self.children:
            self._bar = 1
        else:
            res = 0
            for child in self.children:
                res += child.bar * child.deriv_parent(self.expr)
            self._bar = res
        return self._bar

    @bar.setter
    def bar(self, value):
        assert not self._bar, 'Bar already set'
        self._bar = value

    def deriv_parent(self, parent_expr):
        """Get the derivative of this node with respect to `parent_expr`

        :param parent_expr: TraceNode -- parent with respect to which the derivative should be taken
        :return: Number
        """
        return self.derivs[self.expr.parents.index(parent_expr)]

    def __eq__(self, other):
        if isinstance(other, TraceNode):
            return self.expr == other.expr
        else:
            return self.expr == other

    def __str__(self):
        return str(self.expr)

    def __repr__(self):
        return repr(self.expr)