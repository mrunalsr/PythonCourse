#Example
"""list2 = [100,34,90,["Mohan","Shyam","Ram"],89]
print(list2[3][2])"""

row1 = ['😄','😄','😄']
row2 = ['😄','😄','😄']
row3 = ['😄','😄','😄']

matrix=[row1,row2,row3]   #nested list

print(f"{row1}\n{row2}\n{row3}")
position = input("Enter the position where you want to hide money : ")
#32
row_number=int(position[0])
col_number=int(position[1])
row_selected=matrix[row_number-1]
row_selected[col_number-1]='X'

print(f"{row1}\n{row2}\n{row3}")
