from itertools import count
import numpy as np

# array1 = [
# ['7' , '2' , '1' , '9', '1'],#[1,4]
# ['3' , '8' , '4' ,'6', '3'],
# ['9' , '0' , '7' , '5', '2'], 
# ['6' , '1' , '3' , '4', '9'],
# ['2' , '1' , '3' , '4', '3'],  
# ]

# array1 = [
# ['7' , '2' , '1' , '9'],#[1,4]
# ['3' , '8' , '4' , '6'],
# ['9' , '0' , '7' , '5'], 
# ['6' , '1' , '3' , '4'],  
# ]
array1 = [
['7' , '2' , '1'],#[1,4]
['3' , '8' , '4'],
['9' , '0' , '7'],  
]

rows , cols = len(array1) , len( array1[0])
count = 1 

# for i in range(rows): #i = 0 , i = 1 , i = 2 , i = 3 
#     array1[i][i],array1[i][len(array1)-count] = array1[i][len(array1)-count],array1[i][i]
#     count +=1 




for i in range(1):
    #for col0 
    #left shifting column 1
    temp1 = array1[0][0]  # Store first element
    for j in range(rows-1): #i = 1
        array1[j][0] = array1[j+1][0]  # Move each element up
    # right shifting row 1  
    temp2 = array1[0][len(array1)-1]  # Store first element
    for j in range(rows-1,1,-1): #i = 1
        array1[0][j] = array1[0][j-1]
    array1[0][1] = temp1
    # print(temp2)

    # right shifting last column
    temp3 = array1[len(array1)-1][len(array1)-1]  # Store first element
    for j in range(rows-1,1,-1): #i = 1
        array1[j][len(array1)-1] = array1[j-1][len(array1)-1]
    array1[1][len(array1)-1] = temp2
    # print(temp3)
    # left shifting last row 
    for j in range(rows-1): #i = 1
        array1[len(array1)-1][j] = array1[len(array1)-1][j+1]
    array1[len(array1)-1][len(array1)-2] = temp3









for i in range(rows):
    print(array1[i])
            
                
                

           