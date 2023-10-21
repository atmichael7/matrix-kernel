'''
Mike B

Purpose: This is a small exercise that interacts with matrices and kernel filters in order to manipulate said matrices.
Inspired from my image processing class at university, this program takes in integer inputs from a 2d matrix array and
an input kernel filter and generates an output matrix with the result and displays it. 

Use: The user creates an input matrix in the code (hard coded) and calls the kernelApplication function with the
input matrix and kernel arguements respectively. The application function will create a temporary matrix of 
column and row size that is 2 greater to create a buffer zone for the kernel when it inpsects each index of the modified 
input matrix. It then goes through each index of the modified input matrix and cross references it against the input
kernel and does a summation based on that. The result of the temp matrix is returned to the caller. 


# How to: 
 1. Go to the matrices.py and create an input matrix with the desired values
 2. In matrices.py, either create or use an already existing kernel that will be used on the input matrix
 3. Come back here and call the goThruMatrix function with the first arguement as 2
        and the second arguement as a call to kernalApplication with the kernel and input matrix arguements respectively

        Ex) goThruMatrix(2, kernalApplication(inputKernelName, inputMatrixName))

'''

# Matrices for input and kernels
from matrices import *

 # This includes all other supporting functions that the application requires
from matrixApplication import *




goThruMatrix(2, kernalApplication(x_dir_kernel, matrix))

