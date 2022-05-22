import pandas as pd

def Save_DF(s1: str,DF1,index_flag: bool,header_flag: bool):
    DF1.to_excel(s1,index=index_flag,header=header_flag)
