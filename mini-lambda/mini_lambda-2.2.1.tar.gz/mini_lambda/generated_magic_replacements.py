# ----
# This file is generated by mini_lambda_methods_generation.py - do not modify it !
# ----
from mini_lambda.main import LambdaExpression
from sys import getsizeof

__all__ = [
    'Iter',
    'Str',
    'Bytes',
    'Sizeof',
    'Hash',
    'Bool',
    'Len',
    'Int',
    'Float',
    'Complex',
    'Oct',
    'Hex',
]


# ******* All replacement methods for the magic methods throwing exceptions ********
def Iter(*args, **kwargs):
    """ This is a replacement method for LambdaExpression '__iter__' magic method """
    return LambdaExpression._get_expression_for_method_with_args(iter, *args, **kwargs)


def Str(*args, **kwargs):
    """ This is a replacement method for LambdaExpression '__str__' magic method """
    return LambdaExpression._get_expression_for_method_with_args(str, *args, **kwargs)


def Bytes(*args, **kwargs):
    """ This is a replacement method for LambdaExpression '__bytes__' magic method """
    return LambdaExpression._get_expression_for_method_with_args(bytes, *args, **kwargs)





def Sizeof(*args, **kwargs):
    """ This is a replacement method for LambdaExpression '__sizeof__' magic method """
    return LambdaExpression._get_expression_for_method_with_args(getsizeof, *args, **kwargs)


def Hash(*args, **kwargs):
    """ This is a replacement method for LambdaExpression '__hash__' magic method """
    return LambdaExpression._get_expression_for_method_with_args(hash, *args, **kwargs)


def Bool(*args, **kwargs):
    """ This is a replacement method for LambdaExpression '__bool__' magic method """
    return LambdaExpression._get_expression_for_method_with_args(bool, *args, **kwargs)


def Len(*args, **kwargs):
    """ This is a replacement method for LambdaExpression '__len__' magic method """
    return LambdaExpression._get_expression_for_method_with_args(len, *args, **kwargs)


def Int(*args, **kwargs):
    """ This is a replacement method for LambdaExpression '__int__' magic method """
    return LambdaExpression._get_expression_for_method_with_args(int, *args, **kwargs)


def Float(*args, **kwargs):
    """ This is a replacement method for LambdaExpression '__float__' magic method """
    return LambdaExpression._get_expression_for_method_with_args(float, *args, **kwargs)


def Complex(*args, **kwargs):
    """ This is a replacement method for LambdaExpression '__complex__' magic method """
    return LambdaExpression._get_expression_for_method_with_args(complex, *args, **kwargs)


def Oct(*args, **kwargs):
    """ This is a replacement method for LambdaExpression '__oct__' magic method """
    return LambdaExpression._get_expression_for_method_with_args(oct, *args, **kwargs)


def Hex(*args, **kwargs):
    """ This is a replacement method for LambdaExpression '__hex__' magic method """
    return LambdaExpression._get_expression_for_method_with_args(hex, *args, **kwargs)


