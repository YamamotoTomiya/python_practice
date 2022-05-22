import MyModule0502
import pandas as pd

df=pd.DataFrame([[11,21,31],[12,22,32],[31,32,33]]
                    ,index=['one','two','three'],columns=['a','b','c'])
print(df)
MyModule0502.Save_DF('out1.xlsx',df,True,True)
MyModule0502.Save_DF('out2.xlsx',df,False,True)