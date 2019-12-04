import pandas as pd
import numpy as np
from scipy.stats.contingency import expected_freq

def contingency_table(dataframe, columns_a, columns_b, order_a = False, order_b = False, informative = True, norm_axis = False):
    '''
    dataframe: enter the table on which you want to make the cross tabulation
    columns_a:  insert the text string representing the header of the single column
    columns_b:  insert the text string representing the header of the single column
    order_a: insert a list of values representative of the order of the categories in column A
    order_b:  insert a list of values representative of the order of the categories in column B
    informative: True, allows you to have in the same table frequencies, expected frequencies and discards. 
    '''
    
    if order_a != False:
        dataframe[columns_a] = pd.Categorical(dataframe[columns_a], categories=order_a)
        
    if order_b != False:
        dataframe[columns_b] = pd.Categorical(dataframe[columns_b], categories=order_b)
        

    crosstab = pd.crosstab(dataframe[columns_a],dataframe[columns_b], margins = True, dropna=False)
    
    
        
    if informative == True:
        expected = pd.DataFrame(expected_freq(crosstab), index =  crosstab.index, columns = crosstab.columns)
        crosstab_norm_all = pd.crosstab(dataframe[columns_a],dataframe[columns_b], margins = True, normalize = "all", dropna=False).applymap(lambda x: ("( {:.2f})".format(x) ))
        crosstab_norm_index = pd.crosstab(dataframe[columns_a],dataframe[columns_b], margins = True, normalize = "index", dropna=False).applymap(lambda x: ("( {:.2f})".format(x) ))
        crosstab_norm_columns = pd.crosstab(dataframe[columns_a],dataframe[columns_b], margins = True, normalize = "columns", dropna=False).applymap(lambda x: ("( {:.2f})".format(x) ))
        if norm_axis == False:
            crosstab = crosstab.applymap(str) + " " + expected.applymap(lambda x: ("( {:.2f})".format(x) )) + " " + (crosstab - expected).applymap(lambda x: ("( {:.2f})".format(x) )) + " " + crosstab_norm_all
        if norm_axis == "index":
            crosstab = crosstab.applymap(str) + " " + expected.applymap(lambda x: ("( {:.2f})".format(x) )) + " " + (crosstab - expected).applymap(lambda x: ("( {:.2f})".format(x) )) + " " + crosstab_norm_index
        if norm_axis == "columns":
            crosstab = crosstab.applymap(str) + " " + expected.applymap(lambda x: ("( {:.2f})".format(x) )) + " " + (crosstab - expected).applymap(lambda x: ("( {:.2f})".format(x) )) + " " + crosstab_norm_columns
      
    return crosstab

if __name__ == '__main__':
    data = pd.DataFrame({
        "key_a" : ["high", "medium", "low", "low", "low"],
        "key_b" : ["1","1","3","3","3"]
    })
    data2 = pd.DataFrame({
        "key_a" : [1, 2, 3, 4, 5],
        "key_b" : ["ugo","1","3","3","3"]
    })


    # test ordinal values 
    print(contingency_table(data,
                            "key_a",
                            "key_b",
                            order_a = ["low","medium","high"],
                            order_b = ["1","2","3"],
                            informative = True, 
                            norm_axis = False))
    # test categorical values
    print(contingency_table(data2,
                            "key_a",
                            "key_b",
                            informative = True, 
                            norm_axis = False))