import pandas as pd

def read_file(s1:str,n1:int,header,index_col):
    DataFrame=pd.read_excel(s1,sheet_name=n1,header=header,index_col=index_col)
    return DataFrame

def save_DF(s1:str,DF1,index_flag:bool,header_flag:bool):
    DF1.to_excel(s1,index=index_flag,header=header_flag)

def create_DF3():
    DF=pd.DataFrame([['za1','zb1','zc'],['za2','zb2','zc'],['za3','zb3','zc'],
                     ['za4','zb4','zd'],['za5','zb5','zd'],['za6','zb6','zd'],
                     ['za7','zb7','ze'],['za8','zb8','ze'],['za9','zb9','ze'],
                     ['za10','zb10','ze']]
                    ,index=[1,2,3,4,5,6,7,8,9,10],columns=['a','b','c'])
    return DF