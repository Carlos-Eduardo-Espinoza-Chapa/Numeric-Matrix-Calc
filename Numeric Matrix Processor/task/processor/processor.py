import sys
def menu():
    print("1. Add matrices", "2. Multiply matrix by a constant", "3. Multiply matrices", "4. Transpose matrix", "5. Calculate a determinant", "0. Exit", sep="\n")
    choice = input("Your choice: ")
    return choice

def addmatrix():
    Dimensions_A = [int(i) for i in input("Enter size of first matrix: ").split()]
    print("Enter first matrix:\n")
    Matriz_A = [[float(j) for j in input().split()] for i in range(Dimensions_A[0])]
    Dimensions_B = [int(i) for i in input("Enter size of second matrix: ").split()]
    print("Enter second matrix:\n")
    Matriz_B = [[float(j) for j in input().split()] for i in range(Dimensions_B[0])]
    if len(Matriz_A) == len(Matriz_B) and len(Matriz_A[0]) == len(Matriz_B[0]):
        print("The result is:")
        Matriz_R = [[Matriz_A[i][j] + Matriz_B[i][j] for j in range(Dimensions_A[1])] for i in range(Dimensions_A[0])]
        for i in range(Dimensions_A[0]):
            print()
            for j in range(Dimensions_A[1]):
                print(Matriz_R[i][j], end=" ")
    else:
        print("The operation cannot be performed.")

def escmult():
    Dimensions_A = [int(i) for i in input("Enter size of matrix: ").split()]
    print("Enter matrix:\n")
    Matriz_A = [[float(j) for j in input().split()] for i in range(Dimensions_A[0])]
    const_num = float(input())
    print("The result is: ")
    for i in range(Dimensions_A[0]):
        print()
        for j in range(Dimensions_A[1]):
            print(Matriz_A[i][j] * const_num, end=" ")

def multi():
    Dimensions_A = [int(i) for i in input("Enter size of first matrix: ").split()]
    print("Enter first matrix:\n")
    Matriz_A = [[float(j) for j in input().split()] for i in range(Dimensions_A[0])]
    Dimensions_B = [int(i) for i in input("Enter size of second matrix: ").split()]
    print("Enter second matrix:\n")
    Matriz_B = [[float(j) for j in input().split()] for i in range(Dimensions_B[0])]
    if Dimensions_A[1] != Dimensions_B[0]:
        print("The operation cannot be performed.")
    else:
        Matriz_R = [[sum(a * b for a, b in zip(A_col, B_rows)) for B_rows in zip(*Matriz_B)] for A_col in Matriz_A]
        for i in range(Dimensions_A[0]):
            print("\n")
            for j in range(Dimensions_B[1]):
                print(Matriz_R[i][j], end=" ")

def trans():
    print("1. Main diagonal", "2. Side diagonal", "3. Vertical line", "4. Horizontal line", sep="\n")
    choice = input("Your choice: ")
    Dimensions_A = [int(i) for i in input("Enter matrix size: ").split()]
    print("Enter matrix:\n")
    Matriz_A = [[float(j) for j in input().split()] for i in range(Dimensions_A[0])]
    print("The result is:\n")
    if choice == "1":
        for i in range(len(Matriz_A[0])):
            print()
            for j in range(len(Matriz_A)):
                print(Matriz_A[j][i], end=" ")
    elif choice == "2":
        for i in reversed(range(len(Matriz_A[0]))):
            print()
            for j in reversed(range(len(Matriz_A))):
                print(Matriz_A[j][i], end=" ")
    elif choice == "3":
        for i in range(len(Matriz_A)):
            print()
            for j in reversed(range(len(Matriz_A[0]))):
                print(Matriz_A[i][j], end=" ")
    elif choice == "4":
        for i in reversed(range(len(Matriz_A))):
            print()
            for j in range(len(Matriz_A[0])):
                print(Matriz_A[i][j], end=" ")
###this code below was kindly provided on stackoverflow by the user stackPusher, and I just did minimal adaptations to make it work
###in python 3, but otherwise, I take no ownership of it :D, im just using it as a placeholder until i refactor the code
def transposeMatrix(m):
    return list(map(list,zip(*m)))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(list(cofactors))):
        for c in range(len(list(cofactors))):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors
### end of the placeholder code ###

if __name__ == "__main__":
    while True:
        print()
        choice = menu()
        if choice == "1":
            addmatrix()
            continue
        elif choice == "2":
            escmult()
            continue
        elif choice == "3":
            multi()
            continue
        elif choice == "4":
            trans()
            continue
        elif choice == "5":
            Dimensions_A = [int(i) for i in input("Enter matrix size: ").split()]
            print("Enter matrix:\n")
            Matriz_A = [[float(j) for j in input().split()] for i in range(Dimensions_A[0])]
            print("The result is:\n")
            result = Determinant(Matriz_A)
            print(result)
        elif choice == "6":
            Dimensions_A = [int(i) for i in input("Enter matrix size: ").split()]
            print("Enter matrix:\n")
            Matriz_A = [[float(j) for j in input().split()] for i in range(Dimensions_A[0])]
            print("The result is:\n")
            Matriz_R = getMatrixInverse(Matriz_A)
            for i in range(Dimensions_A[0]):
                print()
                for j in range(Dimensions_A[1]):
                    print(Matriz_R[i][j], end=" ")
        else:
            sys.exit()
        break

