import MyModule05
import MyModule0512

s1="out0511.xlsx"
n1=0
header=0
index_col=0
DF2=MyModule05.read_file(s1,n1,header,index_col)

colmn_name="b"
s2="zb3"
s3="zb9"
DF3=MyModule0512.get_DF_s1_2_s2(DF2,colmn_name,s2,s3)
print(DF3)