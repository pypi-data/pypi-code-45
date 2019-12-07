# -*- coding: utf-8 -*-
"""
scrip for customized primitives
"""

import pandas as pd
import numpy as np
import featuretools as ft
from featuretools.primitives import make_agg_primitive, make_trans_primitive
from featuretools.variable_types import Text, Numeric, Categorical, Boolean, Index, DatetimeIndex, Datetime, TimeIndex, Discrete, Ordinal

def enc(col):

    en = 0 if len(col)==0 else 1

    return en

def min_date(col):

    return pd.to_datetime(np.min(col))

def max_date(col):

    return pd.to_datetime(np.max(col))

def n_uni(col):

    return len(set(col))

def f1s(col):

    return col.tolist()[0]

def max_boo(col):

    return np.max(col)

def seasons(vals):

    return (vals.dt.month%12 + 3)//3

def weekday(vals):

    return vals.dt.weekday.values

def is_weekend(vals):

    return vals.dt.weekday.values>4

 

enco = make_agg_primitive(function=enc,

                               input_types=[Index], #the reason why using Index is because actually we will count 'index' on 'Where' condition;

                               return_type=Numeric,

                         name='If',stack_on_self=False)

min_d = make_agg_primitive(function=min_date,

                          input_types=[Datetime],

                          return_type=Numeric,name='Min',stack_on_self=False)

max_d = make_agg_primitive(function=max_date,

                          input_types=[Datetime],

                          return_type=Numeric,name='Max',stack_on_self=False)#,name='Max')

u_uniq = make_agg_primitive(function=n_uni,

                          input_types=[Discrete],

                          return_type=Numeric,name='Unique',stack_on_self=False)#,name='Max')

f1st = make_agg_primitive(function=f1s,

                               input_types=[Categorical],

                               return_type=Categorical,name='First')

max_bol = make_agg_primitive(function=max_boo,

                            input_types=[Boolean],

                            return_type=Boolean,

                            name='MaxBol',stack_on_self=False)

season = make_trans_primitive(function=seasons,

                             input_types=[Datetime],

                             return_type=Ordinal,

                             name='Season')

weekday = make_trans_primitive(function=weekday,

                             input_types=[Datetime],

                             return_type=Ordinal,

                             name='Weekday')

 

is_weekend = make_trans_primitive(function=is_weekend,

                             input_types=[Datetime],

                             return_type=Numeric,

                             name='Is_weekend')
