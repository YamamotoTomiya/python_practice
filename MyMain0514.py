import MyModule05
import MyModule0514

s1="out0511.xlsx"
n1,header,index_col=0,0,0
DF2=MyModule05.read_file(s1,n1,header,index_col)

s2="b"
S1=MyModule0514.get_Series_string(DF2,s2)
print(S1)