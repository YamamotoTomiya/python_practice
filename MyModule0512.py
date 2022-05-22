import pandas as pd

def get_DF_s1_2_s2(DF1,colmn_name,s1,s2):
    a=DF1.reset_index().query('{}==@s1'.format(colmn_name)).index[0]
    b=DF1.reset_index().query('{}==@s2'.format(colmn_name)).index[0]
    DF2=DF1.iloc[a:b+1,:]
    return DF2

