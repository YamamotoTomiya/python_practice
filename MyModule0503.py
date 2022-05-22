import random 
import pandas as pd

def create_DF2(n1):
    df=pd.DataFrame(index=[],columns=['a','b','c'])
    for i in range(n1):
        a=random.randint(11,50)
        b=random.randint(11,50)
        c=random.randint(11,50)
        df=df.append({'a':a,'b':b,'c':c},ignore_index=True)
    return df

def save_DF(s1,DF1,index_flag,header_flag):
    DF1.to_excel(s1,index=index_flag,header=header_flag)
