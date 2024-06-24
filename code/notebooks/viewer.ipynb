# %%
# import libraries

import ast
import wfdb
import numpy as np
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# define constants

DATASET_PATH = './ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3/'
SAMPLING_RATE = 100
SAMPLE_NUMBER = 5

# %%
# define a function that load raw data by a specified local DATASET_PATH

def load_raw_data(df, SAMPLING_RATE, DATASET_PATH):
    df_array = []
    if SAMPLING_RATE == 100:
        for i in df.filename_lr.values:
            df_array.append(i[: 12] + i[18 :])
        data = [wfdb.rdsamp(DATASET_PATH + f) for f in tqdm(df_array)]
    else:
        for i in df.filename_hr.values:
            df_array.append(i[: 12] + i[18 :])
        data = [wfdb.rdsamp(DATASET_PATH + f) for f in tqdm(df_array)]
    data = np.array([signal for signal, meta in data])
    return data

# %%
# load and convert annotation data

Y = pd.read_csv(DATASET_PATH + 'ptbxl_database.csv', index_col = 'ecg_id')
Y.scp_codes = Y.scp_codes.apply(lambda x: ast.literal_eval(x))

# %%
# load raw signal data

X = load_raw_data(Y, SAMPLING_RATE, DATASET_PATH)

# %%
# load 'scp_statements.csv' file for diagnostic aggregation

agg_df = pd.read_csv(DATASET_PATH + 'scp_statements.csv', index_col = 0)
agg_df = agg_df[agg_df.diagnostic == 1]
agg_df.head()

# %%
# define a function that aggregate superclass diagnostic for later analysis

def aggregate_supclass_diagnostic(y_dic):
    tmp = []
    for key in y_dic.keys():
        if key in agg_df.index:
            tmp.append(agg_df.loc[key].diagnostic_class)
    ret = list(set(tmp))
    ret = ['sup_' + r for r in ret]
    return ret

# %%
# apply diagnostic superclass

Y['diagnostic_superclass'] = Y.scp_codes.apply(aggregate_supclass_diagnostic)
Y['diagnostic_superclass_len'] = Y['diagnostic_superclass'].apply(len)
vc = Y['diagnostic_superclass_len'].value_counts()

# %%
# show diagnostic superclass len plot

sns.set_style('whitegrid')
bar, axis = plt.subplots(figsize = (10, 6))
axis = sns.barplot(x = vc.values / vc.values.sum() * 100., y = vc.index, orient = 'h')
axis.set_title('Diagnostic Superclass Length Distribution', fontsize = 20)
axis.set_xlabel('percentage over all samples')
axis.set_ylabel('diagnostic superclass len')
for rect in axis.patches:
    axis.text(rect.get_width(), rect.get_y() + (rect.get_height() / 2), '%.1f%%' % rect.get_width())
plt.show()

# %%
# define a function that aggregate subclass diagnostic for analysis

def aggregate_subclass_diagnostic(y_dic):
    tmp = []
    for key in y_dic.keys():
        if key in agg_df.index:
            tmp.append(agg_df.loc[key].diagnostic_subclass)
    ret = list(set(tmp))
    ret = ['sub_' + r for r in ret]
    return ret

# %%
# apply diagnostic subclass

Y['diagnostic_subclass'] = Y.scp_codes.apply(aggregate_subclass_diagnostic)
Y['diagnostic_subclass_len'] = Y['diagnostic_subclass'].apply(len)
vc = Y['diagnostic_subclass_len'].value_counts()

# %%
# show diagnostic subclass len plot

sns.set_style('whitegrid')
bar, axis = plt.subplots(figsize = (10, 6))
axis = sns.barplot(x = vc.values / vc.values.sum() * 100., y = vc.index, orient = 'h')
axis.set_title('Diagnostic Subclass Length Distribution', fontsize = 20)
axis.set_xlabel('percentage over all samples')
axis.set_ylabel('diagnostic subclass len')
for rect in axis.patches:
    axis.text(rect.get_width(), rect.get_y() + (rect.get_height() / 2), '%.1f%%' % rect.get_width())
plt.show()

# %%
# reformat data for exploratory data analysis

all_superclass = pd.Series(np.concatenate(Y['diagnostic_superclass'].values))
all_subclass = pd.Series(np.concatenate(Y['diagnostic_subclass'].values))
superclass_cols = all_superclass.unique()
subclass_cols = all_subclass.unique()
update_cols = np.concatenate([superclass_cols, subclass_cols])
metadata_cols = ['age', 'sex', 'height', 'weight']

# %%
# define a class and a function that use that class to analyze distribution

class ClassUpdate():
    def __init__(self, cols):
        self.cols = cols
    def __call__(self, row):
        for sc in row['diagnostic_superclass']:
            row[sc] = 1
        for sc in row['diagnostic_subclass']:
            row[sc] = 1
        return row
def get_data_by_folds(folds, x, y, update_cols, feature_cols):
    assert len(folds) > 0, '# of provided folds should longer than 1'
    filt = np.isin(y.strat_fold.values, folds)
    x_selected = x[filt]
    y_selected = y[filt]
    for sc in update_cols:
        y_selected[sc] = 0
    cls_updt = ClassUpdate(update_cols)
    y_selected = y_selected.apply(cls_updt, axis = 1)
    return x_selected, y_selected[list(feature_cols) + list(update_cols) + ['strat_fold']]
x_all, y_all = get_data_by_folds(np.arange(1, 11), X, Y, update_cols, metadata_cols)

# %%
# show diagnostic superclass plot after EDA

vc = y_all[superclass_cols].sum(axis = 0)
sns.set_style('whitegrid')
bar, axis = plt.subplots(figsize = (10, 6))
axis = sns.barplot(x = vc.values / y_all.shape[0] * 100., y = vc.index, orient = 'h')
axis.set_title('Diagnositic Superclass Distribution', fontsize = 20)
axis.set_xlabel('percentage over all samples')
axis.set_ylabel('diagnositic superclass')
for rect in axis.patches:
    axis.text(rect.get_width(), rect.get_y() + rect.get_height() / 2, '%.1f%%' % rect.get_width())
plt.show()

# %%
# show diagnostic subclass plot after EDA

vc = y_all[subclass_cols].sum(axis = 0)
sns.set_style('whitegrid')
bar, axis = plt.subplots(figsize = (10, 6))
axis = sns.barplot(x = vc.values / y_all.shape[0] * 100., y = vc.index, orient = 'h')
axis.set_title('Diagnositic Subclass Distribution', fontsize = 20)
axis.set_xlabel('percentage over all samples')
axis.set_ylabel('diagnositic subclass')
for rect in axis.patches:
    axis.text(rect.get_width(), rect.get_y() + (rect.get_height() / 2), '%.1f%%' % rect.get_width())
plt.show()

# %%
# show per superclass ECGs graphs

for superclass in superclass_cols:
    filter = y_all[superclass] == 1
    y_selected = y_all.loc[filter]
    x_selected = x_all[filter]
    for i in range(SAMPLE_NUMBER):
        y_ = y_selected.iloc[i]
        x_ = x_selected[i]
        bar, axis = plt.subplots(x_.shape[1], 1, figsize = (10, 10))
        title = "Superclass = {}, Age = {}, Height = {}, Weight = {}, Sex = {}".format(superclass, y_['age'], y_['height'], y_['weight'], y_['sex'])
        axis[0].set_title(title, fontsize = 15)
        for c in np.arange(x_.shape[1]):
            sns.lineplot(x = np.arange(x_.shape[0]), y = x_[:, c], ax = axis[c])
        plt.tight_layout()
        plt.show()
