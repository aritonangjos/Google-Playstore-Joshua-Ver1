import pandas as pd
import numpy as np
import re


# def countLangs(x):
# try:
# return len(x.split(","))
# except:
#	return 0


# def value_to_float(x):
# if 'K' in x:
# if len(x) > 1:
# return float(x.replace('K', '')) * 1000
# return 1000.0
# if 'M' in x:
# if len(x) > 1:
# return float(x.replace('M', '')) * 1000000
# return 1000000.0
# if 'B' in x:
# return float(x.replace('B', '')) * 1000000000
# return x


def clean(in_df):
    df = in_df.copy(deep=True)

    df['Rating'] = df['Rating'].replace(np.nan, 0)

    # df['Size'] = df['Size'].apply(lambda x:x.replace('Varies with device', ''))
    df['Size'] = df['Size'].astype(str)
    df['Size'] = df['Size'].apply(lambda x: x.replace('M', ''))
    df['Size'] = df['Size'].apply(lambda x: x.replace('k', ''))
    # df['Size'] = df['Size'].apply(lambda x:re.match("\d+(\.)?\d*",x)[0])
    # df['Size'] = df['Size'].apply(value_to_float)
    df['Size'].astype(float)  # convert the app size column from string to float object

    df['Reviews'].astype(float)

    # df['rating_count'] = df['rating_count'].astype(str)
    # df['rating_count'] = df['rating_count'][:].apply(lambda x:x.replace('件の評価', ' '))
    # df['rating_count'] = df['rating_count'][:].str.split(' ', n=0, expand=True)
    # df['rating_count'].fillna("0",inplace=True)

    # df['rating_count'] = df['rating_count'].apply(value_to_float)
    df['Rating'] = df['Rating'].astype(float)

    df['free_or_not'] = df['price'] != 0  # boolean column for free or not

    # df['price']=df.price.astype(str) #making sure the price column is filled with just prices only

    df['Price'].fillna(value=0, inplace=True)

    # df.assign(free_boolean =df['Price']==0,inplace=True)  #Free or not

    # df['languages']=df['languages'].astype(str)  #replacing apps that have sum null values with enlgish as default
    # df['languages'].apply(lambda x:x.replace('nan', "English"))

    return df
