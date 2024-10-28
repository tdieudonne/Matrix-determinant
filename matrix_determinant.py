#This is the program that calculate the determinant of any square matrix

import os

#function to print matrix
def printMatrix(M, title):
	print("----------")
	print(format(" ", "<3"), end = "")
	print(title)
	print()

	#get rows and columns
	rows = len(M)
	cols = len(M[0])

	#loop through matrix to get items
	for i in range(rows):
		print(format(" ", "<3"), end="")
		for j in range(cols):
			print(format(round(M[i][j], 5), "<5"), end = "")
		print()

	print()

#function to compute Identity matrix of given order
def IMatrix(dim):
	#function to calculate identity matrix

	return [[1. if i==j else 0. for j in range(dim)] for i in range(dim)]

#function to compute zero matrix of given order
def ZeroMatrix(dim):
	return [[0. for j in range(dim)] for i in range(dim)]


#function to return the copy of Entered matrix
def copy_matrix(M):
	rows = list(range(len(M)))
	cols = list(range(len(M[0])))

	CM = [[M[i][j] for j in cols ] for i in rows]
	return CM

#function to help us get input from the user
def get_item(i, j):
	data = float(input(f"Enter item at [{i}][{j}] "))
	return data

#First you have to Enter the dimension of the matrix you want to calculate it's determinant
#remember that we can only calculate the determinant of a square matrix
dim = int(input("Enter dimension: "))

#list comprehension to get the determinant
AM = [[ get_item(i, j) for j in range(dim)] for i in range(dim)]



IM = IMatrix(dim)
ZM = ZeroMatrix(dim)

#clear the screen before printing the matrix
os.system("cls")


#real function to calculate the determinant
#This is the recurssive function and it must have the base condition
def Matrix_Determinant(M, det = 0):
	indices = list(range(len(M)))
	
	#base condition
	if len(M) == 2:
		val = M[0][0]*M[1][1]-M[1][0]*M[0][1]
		return val

	for fc in indices:
		sub_matrix = copy_matrix(M)
		sub_matrix = sub_matrix[1:]
		rows = len(sub_matrix)
		for i in range(rows):
			sub_matrix[i] = sub_matrix[i][0:fc] + sub_matrix[i][fc+1:]
		sign = (-1)**(fc % 2)
		sub_determinant = Matrix_Determinant(sub_matrix)
		det += sign*M[0][fc]*sub_determinant
	return det #This is the determinant

#print the Entered matrix
printMatrix(AM, "AM")

print("Determinant: ", Matrix_Determinant(AM))
