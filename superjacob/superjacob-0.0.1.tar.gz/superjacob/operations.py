from abc import ABC

import numpy as np
from numbers import Number
from .expression import Var, Expression


class OperationType(type):
    def __str__(self):
        return self.__name__


class BaseOperation:
    __metaclass__ = OperationType

    @classmethod
    def check_type(cls, *args):
        """
        :param args: tuple(Object) -- Parameters to check
        :return: None
        :raises: AssertionError if all elements of args are not a Var or Number
        """
        for x in args:
            if not isinstance(x, Var) and not isinstance(x, Number):
                raise TypeError("Not a number/Variable/Expression")

    @classmethod
    def reverse(cls, *args):
        """
        :param args: numbers -- values of the parent nodes
        :return: numbers -- the reverse mode derivative at the current node
        """
        raise NotImplementedError()


class UnaryOperation(BaseOperation, ABC):
    @classmethod
    def expr(cls, expr):
        """Create a new expression

        :param expr: Var | Number -- Parent expression
        :return: Var | Number -- new expression
        """
        cls.check_type(expr)
        return Expression(expr, None, cls)

    @classmethod
    def eval(cls, num):
        """Evaluate the operation at `num`

        :param num: Number -- argument to the unary operation
        :return: Number -- result of evaluation
        """
        raise NotImplementedError()

    @classmethod
    def deriv(cls, val, der):
        """Evaluate the derivative at value = `val` and derivative = `deriv`

        :param val: Number -- Value of the argument
        :param der: Number -- Value of the derivative of the argument
        :return: Number -- The derivative
        """
        raise NotImplementedError()

    @classmethod
    def opstr(cls, expr):
        """For use in the __str__ method of Expression

        :param expr: Expression -- Argument to operation
        :return: str
        """
        raise NotImplementedError()


class BinaryOperation(BaseOperation, ABC):
    @classmethod
    def expr(cls, expr1, expr2):
        """Create a new expression

        :param expr1: Var | Number -- Expression or number to become parent 1
        :param expr2: Var | Number -- Expression or number to become parent 2
        :return:
        """
        cls.check_type(expr1, expr2)
        return Expression(expr1, expr2, cls)

    @classmethod
    def eval(cls, num1, num2):
        """Evaluate the expression at `num2`, `num2`

        :param num1: Number -- First argument to the operation
        :param num2: Number -- Second argument to the operation
        :return:
        """
        raise NotImplementedError()

    @classmethod
    def deriv(cls, num1, deriv1, num2, deriv2):
        """Differentiate the expression at the given values

        :param num1: Number -- Value of parent 1
        :param deriv1: Number -- Value of derivative of parent 1
        :param num2: Number -- Value of parent 2
        :param deriv2: Number -- Value of parent 2
        :return:
        """
        raise NotImplementedError()

    @classmethod
    def opstr(cls, expr1, expr2):
        """For use in the __str__ method of Expression

        :param expr1: Expression -- First argument to operation
        :param expr2: Expression -- Second argument to operation
        :return: str
        """
        raise NotImplementedError()


class Add(BinaryOperation):
    @classmethod
    def eval(cls, num1, num2):
        # super().check_type(num1)
        # super().check_type(num2)
        return num1 + num2

    @classmethod
    def deriv(cls, num1, deriv1, num2, deriv2):
        return deriv1 + deriv2

    @classmethod
    def reverse(cls, *args):
        return (1, 1)

    @classmethod
    def opstr(cls, expr1, expr2):
        return f'{str(expr1)} + {str(expr2)}'


class Sub(BinaryOperation):
    @classmethod
    def eval(cls, num1, num2):
        return num1 - num2

    @classmethod
    def deriv(cls, num1, deriv1, num2, deriv2):
        return deriv1 - deriv2

    @classmethod
    def reverse(cls, *args):
        return (1, -1)

    @classmethod
    def opstr(cls, expr1, expr2):
        return f'{str(expr1)} - {str(expr2)}'


class Mul(BinaryOperation):
    @classmethod
    def eval(cls, num1, num2):
        return num1 * num2

    @classmethod
    def deriv(cls, num1, deriv1, num2, deriv2):
        return num1 * deriv2 + num2 * deriv1

    @classmethod
    def reverse(cls, *args):
        return (args[1], args[0])

    @classmethod
    def opstr(cls, expr1, expr2):
        return f'{str(expr1)} * {str(expr2)}'


class Div(BinaryOperation):
    @classmethod
    def eval(cls, num1, num2):
        return num1 / num2

    @classmethod
    def deriv(cls, num1, deriv1, num2, deriv2):
        return -(num1 * deriv2 - num2 * deriv1) / (num2 ** 2)

    @classmethod
    def reverse(cls, *args):
        return (1 / args[1], - args[0] / args[1]**2)

    @classmethod
    def opstr(cls, expr1, expr2):
        return f'{str(expr1)} / {str(expr2)}'


class Pow(BinaryOperation):
    @classmethod
    def eval(cls, num1, num2):
        return num1 ** num2

    @classmethod
    def deriv(cls, num1, deriv1, num2, deriv2):
        if num1 > 0:
            result = np.exp(num2 * np.log(num1)) * (deriv2 * np.log(num1) + num2 * deriv1 / num1)
            return result

        # deal with the case when log(num1) is complex
        else:
            result = np.exp(num2 * np.log(num1 + 0j)) * (deriv2 * np.log(num1 + 0j) + num2 * deriv1 / num1)
            return np.real(result)

    @classmethod
    def reverse(cls, *args):
        a = args[0] # parent 1 value -- base
        b = args[1] # parent 2 value -- exponent
        if a < 0:
            return np.real((b * a ** (b-1), np.log(a+0j) * a ** b))
        else:
            return (b * a ** (b-1), np.log(a) * a ** b)

    @classmethod
    def opstr(cls, expr1, expr2):
        return f'{str(expr1)}^{str(expr2)}'


class Sqrt(UnaryOperation):
    @classmethod
    def eval(cls, num1):
        return np.sqrt(num1)

    @classmethod
    def deriv(cls, num1, deriv1):
        return 1 / 2 / np.sqrt(num1) * deriv1

    @classmethod
    def reverse(cls, *args):
        a = args[0]
        return 1 / 2 / np.sqrt(a)

    @classmethod
    def opstr(cls, expr):
        return f'sqrt({str(expr)})'
    

class Neg(UnaryOperation):
    @classmethod
    def eval(cls, num1):
        return -num1

    @classmethod
    def deriv(cls, num1, deriv1):
        return -deriv1

    @classmethod
    def reverse(cls, *args):
        return -1

    @classmethod
    def opstr(cls, expr):
        return f'-{str(expr)}'

    
class Exp(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return np.exp(num)

    @classmethod
    def deriv(cls, num, deriv):
        return deriv*np.exp(num)

    @classmethod
    def reverse(cls, *args):
        return np.exp(args[0])

    @classmethod
    def opstr(cls, expr):
        return f'exp({str(expr)})'


class NLog(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return np.log(num)

    @classmethod
    def deriv(cls, val, der):
        return der / val

    @classmethod
    def reverse(cls, *args):
        return 1 / args[0]

    @classmethod
    def opstr(cls, expr):
        return f'ln({str(expr)})'


class Log(BinaryOperation):
    @classmethod
    def eval(cls, num, base=np.e):
        return np.log(num) / np.log(base)

    @classmethod
    def deriv(cls, val, der, base=np.e, base_der=0):
        return (((der / val) * np.log(base)) - ((base_der / base) * np.log(val))) / (np.log(base)**2)

    @classmethod
    def reverse(cls, *args):
        a = args[0]
        b = args[1]
        return (1 / np.log(b) / a, - np.log(a) / np.log(b)**2 / b)

    @classmethod
    def opstr(cls, expr1, expr2):
        # This might be wrong
        return f'log_{str(expr2)}({str(expr1)})'


class Sin(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return np.sin(num)

    @classmethod
    def deriv(cls, val, der):
        return np.cos(val) * der

    @classmethod
    def reverse(cls, *args):
        return np.cos(args[0])

    @classmethod
    def opstr(cls, expr):
        return f'sin({str(expr)})'


class Cos(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return np.cos(num)

    @classmethod
    def deriv(cls, val, der):
        return -np.sin(val) * der

    @classmethod
    def reverse(cls, *args):
        return -np.sin(args[0])

    @classmethod
    def opstr(cls, expr):
        return f'cos({str(expr)})'


class Tan(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return np.tan(num)

    @classmethod
    def deriv(cls, val, der):
        return der / (np.cos(val) ** 2)

    @classmethod
    def reverse(cls, *args):
        return 1 / (np.cos(args[0]) ** 2)

    @classmethod
    def opstr(cls, expr):
        return f'tan({str(expr)})'


class Csc(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return 1/np.sin(num)

    @classmethod
    def deriv(cls, val, der):
        return -der*(1/np.sin(val))*(1/np.tan(val))

    @classmethod
    def reverse(cls, *args):
        return -1*(1/np.sin(args[0]))*(1/np.tan(args[0]))

    @classmethod
    def opstr(cls, expr):
        return f'csc({str(expr)})'


class Sec(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return 1/np.cos(num)

    @classmethod
    def deriv(cls, val, der):
        return der*(1/np.cos(val))*np.tan(val)

    @classmethod
    def reverse(cls, *args):
        return 1*(1/np.cos(args[0]))*np.tan(args[0])

    @classmethod
    def opstr(cls, expr):
        return f'sec({str(expr)})'


class Cot(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return 1/np.tan(num)

    @classmethod
    def deriv(cls, val, der):
        return -der*(1/np.sin(val))**2

    @classmethod
    def reverse(cls, *args):
        return -1*(1/np.sin(args[0]))**2

    @classmethod
    def opstr(cls, expr):
        return f'cot({str(expr)})'


class ArcSin(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return np.arcsin(num)

    @classmethod
    def deriv(cls, val, der):
        return der / np.sqrt(1 - val**2)

    @classmethod
    def reverse(cls, *args):
        return 1 / np.sqrt(1 - args[0]**2)


class ArcCos(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return np.arccos(num)

    @classmethod
    def deriv(cls, val, der):
        return - der / np.sqrt(1 - val**2)

    @classmethod
    def reverse(cls, *args):
        return - 1 / np.sqrt(1 - args[0]**2)


class ArcTan(UnaryOperation):
    @classmethod
    def eval(cls, num):
        return np.arctan(num)

    @classmethod
    def deriv(cls, val, der):
        return der / (1 + val**2)

    @classmethod
    def reverse(cls, *args):
        return 1 / (1 + args[0]**2)


# Vector operations
##class Dot(BinaryOperation):
##    @classmethod
##    def eval(cls, vec1, vec2):
##        return np.dot(vec1, vec2)
##
##    @classmethod
##    def deriv(cls, vec1, deriv1, vec2, deriv2):
##        return np.dot(vec1, deriv2) + np.dot(deriv1, vec2)
