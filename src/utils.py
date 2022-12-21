

# work with df in tabular representation
import warnings
from scipy.stats import stats
import researchpy as rp
from datetime import time
import pandas as pd
# round the df in the correlation matrix
import numpy as np
import os
from scipy.stats import t
from scipy import stats
from statistics import *
from scipy.stats import shapiro
from numpy import mean
from numpy import std

# Modules for df visualization
import seaborn as sns
import matplotlib.pyplot as plt
import statistics

from wordcloud import WordCloud

pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 200)

plt.rcParams['figure.figsize'] = [6, 6]


# overwrite the style of all the matplotlib graphs
sns.set()

# ignore DeprecationWarning Error Messages
warnings.filterwarnings('ignore')


def missing_percentage(df):
    """This function takes a DataFrame(df) as input and returns two columns, total missing values and total missing values percentage"""
    total = df.isnull().sum().sort_values(ascending=False)[
        df.isnull().sum().sort_values(ascending=False) != 0]
    percent = round(df.isnull().sum().sort_values(ascending=False) / len(df) * 100, 2)[
        round(df.isnull().sum().sort_values(ascending=False) / len(df) * 100, 2) != 0]
    return pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    # display missing values in descending
    print("Missing values in the dataframe in descending: \n",
          missing_percentage(df).sort_values(by='Total', ascending=False))

    # visualize where the missing values are located
    msno.matrix(df, color=(255 / 255, 192 / 255, 203 / 255))
    pink_patch = mpatches.Patch(color='pink', label='present value')
    white_patch = mpatches.Patch(color='white', label='absent value')
    plt.legend(handles=[pink_patch, white_patch])
    plt.savefig('missing_plot.png')
    plt.show()


def coerce_df_columns_to_best_dtype(df, boolean_column_list):

    # convert to boolean dtype
    df[boolean_column_list] = df[boolean_column_list].astype(
        'bool', errors='ignore')

    # convert object columns to string datatype
    df = df.convert_dtypes()

    # select numeric columns
    df_numeric = df.select_dtypes(include=[np.number]).columns.to_list()

    # select non-numeric columns
    df_string = df.select_dtypes(include='string').columns.tolist()

    # print out the name and number of numeric column
    print("Number of numeric columns: ", len(df_numeric))
    print("List of numeric columns: ", df_numeric, "\n")

    # print out the name and number of categorical column
    print("Number of categorical columns: ", len(df_string))
    print("List of string columns: ", df_string, "\n\n")

    # return datatype for each column after coercing
    return df.info()
