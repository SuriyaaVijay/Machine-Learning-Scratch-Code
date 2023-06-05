import pandas as pd

RegNo = [ 2020503561 , 2020503562 , 2020503563 , 2020503564 , 2020503565 ]
Name = [ 'Mane' , 'Sane' , 'Kroos' , 'Zlatan' , 'Coro' ]
CGPA = [ 9.5 , 6.3 , 8.4 , 7.7 , 9.1 ] 
std_list = list ( zip ( RegNo , Name , CGPA ) )
 
std_frame = pd.DataFrame ( std_list , columns = [ 'Register_Number' , 'Name' , 'CGPA' ] )
print ( "\n DataFrame ( Student Info )\n\n" , std_frame )

frame1 = std_frame [ [ "Register_Number" , "CGPA" ] ]
print ( "\n DataFrame ( Register Number , CGPA )\n\n" , frame1 )

std_frame.to_csv ( 'df1.csv' )
std_frame = pd.read_csv ( 'df1.csv' , index_col = 'Register_Number' )
print ( "\n Your info\n" , std_frame.loc [ [ 2020503562 ] ] )