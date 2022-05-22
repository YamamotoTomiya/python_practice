import pandas as pd

def get_DF_S1(DF1,colmn_name,s1):
    a=list(DF1.reset_index().query('{}==@s1'.format(colmn_name)).index)
    DF2=DF1.iloc[a[0]:a[-1]+1,:]
    return DF2
