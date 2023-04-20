# Que = solve the homogenous system Ax=0 and write the general solution in parametric vector form.

# m=int(input("Enter the Nuber of Rows : "))
# n=int(input("Enter the Nuber of columns : "))
# dimensions=[m,n]
# mtx=[]
# for i in range(m):
#     k=list(map(float,input(" Enter the matrix as space seperated values row by row : ").split()))
#     mtx.append(k)

# #print(mtx)

# m=[[1,-10,-24,-42],[1,-8,-18,-32],[-2,20,51,87]]

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

# this is the code to input the values of rows and columns /matrix within the program you can make it a comment to import via file


file_location=r"E:\One Drive\OneDrive - indraprashtha institute of information technology\IIITD Projects\Math\Assignment-1\coordinates.txt"

file=open(file_location,'r+')
dimensions=len(file.readlines())  #getting the dimensions / no. of rows of the matrix
file.seek(0,0)
mtx=[]
for i in range(int(dimensions)):            # getting optimum range to get the no. of rows as list.
    j=[float(j) for j in file.readline().strip().split()]
    mtx.append(j)

file.close()
# this is the code to import the values of matrix via a file you can make it a comment to import by hardcoding the input.

print("The Matrix is :")
print()
for i in mtx:
    print(f"     {i}")
print()



print()
def RREF(M):            # Defining the RREF function to calculate the required form
    if not M: return
    count = 0
    rowCount = len(M)                   #no. of rows is equal to no. of nested lists
    columnCount = len(M[0])                # no. of columns is equal to no. of element in one of the nested list
    
    for r in range(rowCount):
        if count >= columnCount:        # exiting the function when the count > or equal to column count
            return
        i = r
        while M[i][count] == 0:
            i += 1

            if i == rowCount:
                i = r
                count += 1
                if columnCount == count:
                    return
        M[i],M[r] = M[r],M[i]
        lv = M[r][count]
        M[r] = [ mrx / float(lv) for mrx in M[r]]      #making the row operations by diving the row by the required number.

        for i in range(rowCount):
            if i != r:
                lv = M[i][count]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]      #zip function allows us to select values one by one from two lists simultanelosly.
        count += 1

RREF( mtx )
print("The Row reduced echelon form of the given matrix is :-")
print()
for i in mtx:
  print (f"     {i}")
print()

pivot=[]      #this will take care of the index of the pivot columns
for i in range(len(mtx)):
    for j in range(len(mtx[0])):
        if mtx[i][j] != 0.0:
            pivot.append(j)
            break
        else:
            continue
# print(pivot,"pivot")

nonpivot=[]                             #this will take care of the index of the non-pivot columns
t=[i for i in range(len(mtx[0]))]
for i in t:
    if i not in pivot:
        nonpivot.append(i)
# print(nonpivot,"nonpivot")        

# soln=[]

pram_sols={}                 #Dictionary of the parametric solutions
for i in nonpivot:
    k=[-1*j[i] for j in mtx]         #multiplying -1 to the values to gain the required paraemetric form
    try:
        k[i]==0                         #if k[i]==0 then it will not prompt error as i have used try and except conditions
        # k[i]+=1
    except:
        pass
    pram_sols[i+1]=k


print("The required parametric form of the matrix is printed below :-")
print()


Solutions=[]         # list containing actual parametric solutions
for j in pram_sols.keys():
    U=[]
    l=[]
    sum=0
    for i in pram_sols.keys():
        if i == j:
            for o in pram_sols[i]:
                l.append(o)

    # print(l)
    for k in range(len(mtx[0])):
        if k+1==j:
            U.append(1.0)          #appending 1.0 if x3 is in the parametric form of itself.
        elif k in nonpivot:     
            U.append(0.0)          #appending 0.0 if x3 is not in the parametric form of itself.
        else:
            U.append(l[sum])
            sum=sum+1
    
    Solutions.append(U)



if nonpivot[0]==len(mtx[0])-1 :   #making the case when the matrix forms identity matrix at the augmented matrix.
    print(f"x{nonpivot[0]} {[i[nonpivot[0]] for i in mtx]}")

else:
    for i in range(len(nonpivot)):
        print(f"     x{nonpivot[i]+1} {Solutions[i]},",end='  ')                  












