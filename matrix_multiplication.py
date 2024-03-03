from random import *

def matrix_multiplication():
    m=[[0 for j in range (cols)] for i in range (rows)] 
    for i in range (rows): 
        for j in range (cols): 
            for k in range (rows): 
                m[i][j]+=matrix1[i][k]*matrix2[k][j] 
    print(m)



cols=int(input("Enter number of columns:"))
rows= int(input("Enter number of rows:"))
matrix1=[[0 for j in range(cols)]for i in range(rows)]
matrix2=[[0 for j in range(cols)]for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        matrix1[i][j]=randint(0,10)
        matrix2[i][j]=randint(0,10)

print(matrix1)
print(matrix2)
matrix_multiplication()



        
        
