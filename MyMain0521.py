import MyModule05

s1="owid-covid-data20220517.xlsx"
n1,header,index_col=0,0,0
DF2=MyModule05.read_file(s1,n1,header,index_col)

column_name="location"
s1="Japan"
DF1=MyModule05.get_DF_S1(DF2,column_name,s1)
s1_name="Japan20220517.xlsx"
index_flag,header_flag=True,True
MyModule05.save_DF(s1_name,DF1,index_flag,header_flag)
s2="date"
date1="2021-04-01 00:00:00"
date2="2022-03-31 00:00:00"
DF2=MyModule05.get_DF_s1_2_s2(DF1,s2,date1,date2)
s3="total_deaths"
total_deaths=MyModule05.get_Series_string(DF2,s3)
print(total_deaths)