import pandas as pd

def create_DF():
    DF=pd.DataFrame([[11,21,31],[12,22,32],[31,32,33]]
                    ,index=['one','two','three'],columns=['a','b','c'])
    return DF
