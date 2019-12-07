from typing import Union
import numpy as np
from superjacob.expression import Expression, Var, VectorExpression
from superjacob import operations as ops
from superjacob.reverse import ReverseDiff


def make_expression(*exprs: Union[Var, Expression], vars=None) -> Union[Expression, VectorExpression]:
    """Returns an expression with the varlist in the specified order

    :param expr: Expression | VectorExpression -- the expression (or iterable of expressions
    :param vars: list[Var] -- A list of Var objects, default None
    """
    # for expr in exprs:
    #     if vars is not None:
    #         expr.set_vars(vars)
    if len(exprs) > 1:
        return VectorExpression(exprs, varlist=vars)
    else:
        exprs[0].set_vars(vars)
        return exprs[0]


# Operations
def add(expr1, expr2):
    return ops.Add.expr(expr1, expr2)


def sub(expr1, expr2):
    return ops.Sub.expr(expr1, expr2)


def mul(expr1, expr2):
    return ops.Mul.expr(expr1, expr2)


def div(expr1, expr2):
    return ops.Div.expr(expr1, expr2)


def pow(expr1, expr2):
    return ops.Pow.expr(expr1, expr2)


def sqrt(expr):
    return ops.Sqrt.expr(expr)


def neg(expr):
    return ops.Neg.expr(expr)


def exp(expr):
    return ops.Exp.expr(expr)


def log(expr1, expr2 = np.e):
    return ops.Log.expr(expr1, expr2)


def nlog(expr):
    return ops.NLog.expr(expr)


def sin(expr):
    return ops.Sin.expr(expr)


def cos(expr):
    return ops.Cos.expr(expr)


def tan(expr):
    return ops.Tan.expr(expr)


def csc(expr):
    return ops.Csc.expr(expr)


def sec(expr):
    return ops.Sec.expr(expr)


def cot(expr):
    return ops.Cot.expr(expr)


def arcsin(expr):
    return ops.ArcSin(expr)


def arccos(expr):
    return ops.ArcCos(expr)


def arctan(expr):
    return ops.ArcTan(expr)


def sinh(expr):
    return (exp(expr) - exp(-expr)) / 2


def cosh(expr):
    return (exp(expr) + exp(-expr)) / 2


def tanh(expr):
    return (exp(expr) - exp(-expr)) / (exp(expr) + exp(-expr))


def logistic(expr, k=1, x0=0, L=1):
    return L / (1 + exp(-k * (expr - x0)))


# Convenience function for reverse mode
def reverse(expr):
    return ReverseDiff(expr)


##def dot(expr1, expr2):
##    return ops.Dot.expr(expr1, expr2)
