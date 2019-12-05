import numpy as np
import pandas as pd

from logging import warning 
import sys
from aif360.datasets import BinaryLabelDataset



class LoadData(BinaryLabelDataset):
    """Base class for every :obj:`BinaryLabelDataset` provided out of the box by
    aif360.

    It is not strictly necessary to inherit this class when adding custom
    datasets but it may be useful.

    This class is very loosely based on code from
    https://github.com/algofairness/fairness-comparison.
    """ 

    def __init__(self, data_path, label_name,
                 protected_attribute_names, privileged_classes,
                 favorable_classes = [1],
                 instance_weights_name='', scores_name='', 
                 quick_drop=False, na_values=[],
                 metadata=None, drop_cutoff_col=80,drop_cutoff_row=5,
                 num_imp_strategy='mean',cat_imp_strategy='common'):



        # keep = (set(numerical_features) | set(protected_attribute_names)
        #       | set(categorical_features) | set([label_name]))


        if instance_weights_name:
            keep |= set([instance_weights_name])
        df = pd.read_csv(data_path)
        # df = df[sorted(keep - set(features_to_drop), key=df.columns.get_loc)]
        # categorical_features = sorted(set(categorical_features) - set(features_to_drop), key=df.columns.get_loc)
        missing = df.isnull().sum()
        missing_percent = 100 * df.isnull().sum() / len(df)
        missing_df = pd.concat([missing, missing_percent], axis=1)
        missing_df = missing_df.rename(columns = {0 : 'Missing', 1 : 'Percent'})
        missing_df = missing_df[missing_df.iloc[:,1] != 0].sort_values('Percent', ascending=False).round(2)
        warning("Out of {} columns, there are {} with missing values.".format(df.shape[1],missing_df.shape[0]))
        # Code here for the missing df that could be included?

        if quick_drop:
            before = len(df)
            df.dropna(axis=0, thresh=1, inplace=True)
            after = len(df)
            count = before-after
            warning("Missing Data: {} rows removed from {}.".format(count,type(self).__name__))
        else:
            # Here two things are done:
            # First, dropping all columns that have more than drop_cutoff_col % of missing records
            # Seconds, dropping all records for columns with less than drop_cutoff_row % of missing records
            drop_cols_list = []
            drop_rows_list = []
            rest_list = []
            for col_name, values in missing_df.iterrows():
                if values['Percent'] > drop_cutoff_col:
                    drop_cols_list.append(col_name)
                if values['Percent'] < drop_cutoff_row:
                    drop_rows_list.append(col_name)
                else:
                    rest_list.append(col_name)
        
            df.drop(drop_cols_list, inplace=True, axis=1) # Check here the axis
            print('Dropped ' + str(len(drop_cols_list)) + ' columns that have more than ' + str(drop_cutoff_col) + ' percent of missing values.')
            
            df.dropna(how='any', subset=drop_rows_list,inplace=True)

            # For the rest of columns, we want to impute. So will loop through the rest of them
            # Now will just use same strategy for each. May ask user input for strategy for each column

            # Ask user for columns to customize what columns get imputed with some values or what
            # Column/Value tuple user input

            # Standardize
            
            for col_name in rest_list:
                col = df[col_name]
                # Checking dtype for column
                # If numerical:
                if col.dtype == 'int' or col.dtype == 'float':
                    if num_imp_strategy == 'mean':
                        col.fillna((col.mean()), inplace=True)
                    if num_imp_strategy == 'median':
                        # print(col,'2')
                        col.fillna((col.median()), inplace=True)
                    if num_imp_strategy == 'mode':
                        col.fillna((col.mode()), inplace=True)
                    else:
                        if type(num_imp_strategy == 'int') or type(num_imp_strategy) == 'float':
                            col.fillna((col.mode()), inplace=True)
                        else:
                            print('num_imp_strategy is invalid. Must be mean, median, mode or a number')
                            sys.exit(1)
                if col.dtype == 'object':
                    # Here I will assume objects is string. May want to look at this later
                    if cat_imp_strategy == 'common':
                        col.fillna(col.value_counts().index[0],inplace=True)
                    # If the user wants it to be something else they specify
                    else:
                        col.fillna(cat_imp_strategy,inplace=True)

            # 5. Create a one-hot encoding of the categorical variables.
            privileged = df[protected_attribute_names]

            df_without = df.drop(protected_attribute_names, axis = 1)

            df_without = pd.get_dummies(df_without, prefix_sep='=')

            df = df_without

            df[protected_attribute_names]  = privileged


            # 6. Map protected attributes to privileged/unprivileged
            privileged_protected_attributes = []
            unprivileged_protected_attributes = []
            for attr, vals in zip(protected_attribute_names, privileged_classes):
                privileged_values = [1.]
                unprivileged_values = [0.]
                if callable(vals):
                    df.loc[attr] = df[attr].apply(vals)
                elif np.issubdtype(df[attr].dtype, np.number):
                    # this attribute is numeric; no remapping needed
                    privileged_values = vals
                    unprivileged_values = list(set(df[attr]).difference(vals))
                else:
                    # find all instances which match any of the attribute values
                    priv = np.logical_or.reduce(np.equal.outer(vals, df[attr].to_numpy()))
                    df.loc[priv, attr] = privileged_values[0]
                    df.loc[~priv, attr] = unprivileged_values[0]

                privileged_protected_attributes.append(
                    np.array(privileged_values, dtype=np.float64))
                unprivileged_protected_attributes.append(
                    np.array(unprivileged_values, dtype=np.float64))

            # 7. Make labels binary
            favorable_label = 1.
            unfavorable_label = 0.
            if callable(favorable_classes):
                df.loc[label_name] = df[label_name].apply(favorable_classes)
            elif np.issubdtype(df[label_name], np.number) and len(set(df[label_name])) == 2:
                # labels are already binary; don't change them
                favorable_label = favorable_classes[0]
                unfavorable_label = set(df[label_name]).difference(favorable_classes).pop()
            else:
                # find all instances which match any of the favorable classes
                pos = np.logical_or.reduce(np.equal.outer(favorable_classes, 
                                                        df[label_name].to_numpy()))
                df.loc[pos, label_name] = favorable_label
                df.loc[~pos, label_name] = unfavorable_label

        super(LoadData, self).__init__(df=df, label_names=[label_name],
            protected_attribute_names=protected_attribute_names,
            privileged_protected_attributes=privileged_protected_attributes,
            unprivileged_protected_attributes=unprivileged_protected_attributes,
            instance_weights_name=instance_weights_name,
            scores_names=[scores_name] if scores_name else [],
            favorable_label=favorable_label,
            unfavorable_label=unfavorable_label, metadata=metadata)

      