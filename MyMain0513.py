import MyModule05
import MyModule0513

s1="out0511.xlsx"
n1,header,index_col=0,0,0
DF2=MyModule05.read_file(s1,n1,header,index_col)

colmn_name="c"
s1="zd"
DF3=MyModule0513.get_DF_S1(DF2,colmn_name,s1)
print(DF3)
