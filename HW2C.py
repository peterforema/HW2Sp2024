

def GaussSeidel (Aaug, x, Niter = 15):
    ''' Purpose: use the Gauss-Seidel method to estimate the solution to a set of N linear equations expressed in matrix
        form as Ax = b. Both A and b are contained in the function argument – Aaug.

        Aaug: an augmented matrix containing [A | b ] having N rows and N+1 columns, where N is the number of equations in the set.
        x: a vector (array) contains the values of the initial guess
        Niter: the number of iterations (new x vectors) to compute
        return value: the final new x vector.
        '''

    N = len(Aaug)    #N is the number of equations/length of matrix

    for iteration in range(Niter):  #loops
        for i in range(N): #for each equation for each iteration
            sigma = 0.0     #calculates the sum of the iteration
            for j in range(N):                              #This line adapted from ChatGPT
                if j != i:                                  #This line adapted from ChatGPT
                    sigma += Aaug[i][j] * x[j]              #This line adapted from ChatGPT
            x[i] = (Aaug[i][-1] - sigma) / Aaug[i][i]       #This line adapted from ChatGPT

    return x


def main():
    '''Example matrix 1 and 2 from Prof Smays HW2'''
    Aaug1 = [
        [3, 1, -1, 2],
        [1, 4, 1, 12],
        [2, 1, 2, 10]
    ]
    Guess = [0.0] * (len(Aaug1[0]) -1)
    Iterations = 25

    Result1 = GaussSeidel(Aaug1,Guess, Iterations)
    print("The solution for Matrix 1 is:", Result1)

    Aaug2 = [
        [3, 1, 4, 12, 12],
        [1, -10, 2, 4, 2],
        [-1, 2, 7, 3, 37],
        [9, 2, 3, 4, 21]
    ]
    Guess = [0] * (len(Aaug2[0]) -1)
    Iterations = 25

    Result2 = GaussSeidel(Aaug2,Guess, Iterations)
    print("The solution for Matrix 2 is:", Result2)

if __name__ == "__main__":
    main()