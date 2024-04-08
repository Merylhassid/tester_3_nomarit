from colors import bcolors
from matrix_utility import *
import numpy as np

def polynomialInterpolation(table_points, x):
    matrix = [[point[0] ** i for i in range(len(table_points))] for point in table_points] # Makes the initial matrix

    b = [[point[1]] for point in table_points]

    # print(bcolors.OKBLUE, "The matrix obtained from the points: ", bcolors.ENDC,'\n', np.array(matrix))
    # print(bcolors.OKBLUE, "\nb vector: ", bcolors.ENDC,'\n',np.array(b))
    matrixSol = np.linalg.solve(matrix,b) #solveMatrix(matrix, b)

    result = sum([matrixSol[i][0] * (x ** i) for i in range(len(matrixSol))])
    # print(bcolors.OKBLUE, "\nThe polynom:", bcolors.ENDC)
    # print('P(X) = '+'+'.join([ '('+str(matrixSol[i][0])+') * x^' + str(i) + ' ' for i in range(len(matrixSol))])  )
    print(bcolors.OKGREEN, f"\nThe Result of P(X={x}) is:", bcolors.ENDC)
    print(result)
    return result


if __name__ == '__main__':
    print("https://github.com/Merylhassid/tester_3_nomarit\ngroup:Almog Babila 209477678, Hai karmi 207265678, Yagel Batito 318271863, Meryl Hassid 324569714\nstudent:Meryl Hassid 324569714")

    table_points = [(1.2, 1.5095), (1.3, 1.6984), (1.4, 1.9043), (1.5, 2.1293), (1.6, 2.3756)]
    x = 1.47
    y = 1.67
    # print(bcolors.OKBLUE, "----------------- Interpolation & Extrapolation Methods -----------------\n", bcolors.ENDC)
    # print(bcolors.OKBLUE, "Table Points: ", bcolors.ENDC, table_points)
    # print(bcolors.OKBLUE, "Finding an approximation to the point: ", bcolors.ENDC, x,'\n')
    polynomialInterpolation(table_points, x)
    polynomialInterpolation(table_points, y)

    print(bcolors.OKBLUE, "\n---------------------------------------------------------------------------\n", bcolors.ENDC)
