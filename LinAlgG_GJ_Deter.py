from os import system
def clear():
    system("cls")
def create_augmented_matrix(n):
    return [[0 for _ in range(n+1)] for _ in range(n)]

def print_array(arr):
    col_widths = [max(len(str(round(row[i], 2))) for row in arr) for i in range(len(arr[0]))]
    
    for row in arr:
        formatted_row = [
            str(int(x)) if isinstance(x, (int, float)) and x.is_integer() 
            else str(round(x, 2)) 
            for x in row
        ]
        padded_row = [formatted_row[i].ljust(col_widths[i]) for i in range(len(formatted_row))]
        print("".join(padded_row[:-1]) + "|  " + padded_row[-1])

def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_float_list(prompt, n):
    while True:
        try:
            values = list(map(float, input(prompt).split()))
            if len(values) == n:
                return values
            else:
                print(f"Invalid input. Please enter exactly {n} numbers.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def input_augmented_matrix(n):
    arr = create_augmented_matrix(n)
    print("Enter the coefficients of the augmented matrix:")
    for i in range(n):
        while True:
            row_input = get_valid_float_list(f'R{i+1} = ', n+1)
            confirm = input(f"You entered {row_input}. Press Enter to confirm or type 'edit' to change: ").strip().lower()
            if confirm != 'edit':
                arr[i] = row_input
                break
    return arr

def swap_rows(a, n, i):
    for j in range(i+1, n):
        if a[j][i] != 0:
            a[i], a[j] = a[j], a[i]
            print(f"\nSwapped R{i+1} with R{j+1} to avoid zero pivot:")
            print_array(a)
            return True
    return False

def gauss_elimination(a, n):
    for i in range(n):
        if a[i][i] == 0.0:
            if not swap_rows(a, n, i):
                solution = "\nError: Zero pivot encountered. No suitable row to swap."
                if getMatrixDeterminant(matrix, n) == 0:
                    solution = solution + "\n       The system may have no unique solution or infinitely many solutions."
                return solution, None
        pivot = a[i][i]
        if pivot != 1:
            print(f"\nStep {i+1}: Making pivot at R{i+1} a 1 by dividing R{i+1} by {pivot}")
            for k in range(n+1):
                a[i][k] /= pivot
            print_array(a)
        for j in range(i+1, n):
            ratio = a[j][i]
            if ratio != 0:
                print(f"\nStep {i+1}.{j+1}: Eliminating column {i+1} in R{j+1} by subtracting {ratio} times R{i+1} from R{j+1} (-{ratio}R{i+1} + R{j+1})")
                for k in range(n+1):
                    a[j][k] -= ratio * a[i][k]
                print_array(a)
    print("\nModified Augmented Matrix (Upper Triangular Form):")
    print_array(a)
    if all(a[i][i] == 0 for i in range(n)):
        solution = "The system has no unique solution (singular matrix)."
        return solution, None
    x = [0] * n
    x[n-1] = a[n-1][n]
    for i in range(n-2, -1, -1):
        x[i] = a[i][n]
        for j in range(i+1, n):
            x[i] -= a[i][j] * x[j]
    return x, a

def gauss_jordan(a, n):
    for i in range(n):
        if a[i][i] == 0.0:
            if not swap_rows(a, n, i):
                print("\nError: Zero pivot encountered. No suitable row to swap.")
                return None
        pivot = a[i][i]
        if pivot != 1:
            print(f"\nStep {i+1}: Making pivot at R{i+1} a 1 by dividing R{i+1} by {pivot}")
            for k in range(n+1):
                a[i][k] /= pivot
            print_array(a)
        for j in range(n):
            if j != i:
                ratio = a[j][i]
                if ratio != 0:
                    print(f"\nStep {i+1}.{j+1}: Eliminating column {i+1} in R{j+1} by subtracting {ratio} times R{i+1} from R{j+1} (-{ratio}R{i+1} + R{j+1})")
                    for k in range(n+1):
                        a[j][k] -= ratio * a[i][k]
                    print_array(a)
    print("\nModified Augmented Matrix (Reduced Row Echelon Form):")
    print_array(a)
    x = [a[i][n] for i in range(n)]
    return x

def getMatrixMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]

def getMatrixDeterminant(m, n):
    square_matrix = [row[:n] for row in m]
    if len(square_matrix) == 2:
        return square_matrix[0][0] * square_matrix[1][1] - square_matrix[0][1] * square_matrix[1][0]
    determinant = 0
    for c in range(len(square_matrix)):
        determinant += ((-1) ** c) * square_matrix[0][c] * getMatrixDeterminant(getMatrixMinor(square_matrix, 0, c), n-1)
    return determinant

def is_row_echelon(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    leading_index = -1
    for row in matrix:
        nonzero_indices = [i for i, val in enumerate(row) if val != 0]
        if not nonzero_indices:
            continue
        if nonzero_indices[0] <= leading_index:
            return False
        leading_index = nonzero_indices[0]
        for i in range(leading_index + 1, num_rows):
            if matrix[i][leading_index] != 0:
                return False
    return True

def is_reduced_row_echelon(matrix):
    if not is_row_echelon(matrix):
        return False
    for row in matrix:
        leading_ones = [i for i, val in enumerate(row) if val == 1]
        if len(leading_ones) > 1:
            return False
        if leading_ones:
            leading_index = leading_ones[0]
            for i in range(len(matrix)):
                if i != matrix.index(row) and matrix[i][leading_index] != 0:
                    return False
    return True

while True:
    clear()
    gauss_array = []
    n = get_valid_integer("Enter the number of unknowns (n):\n> ")
    matrix = input_augmented_matrix(n)
    clear()
    print("Augmented Matrix:")
    print_array(matrix)
    if is_row_echelon(matrix):
        print("\nThe matrix is in Row Echelon Form.")
    else:
        print("\nThe matrix is NOT in Row Echelon Form.")
    if is_reduced_row_echelon(matrix):
        print("The matrix is in Reduced Row Echelon Form.")
    else:
        print("The matrix is NOT in Reduced Row Echelon Form.")
    while True:
        print("\nChoose the operation you want to perform:")
        print("1. Gauss Elimination (solve system of equations using an augmented matrix)")
        print("2. Determinant Calculation (using the first n columns of the augmented matrix)")
        print("3. Exit")
        choice = input("Enter 1, 2, or 3.\n> ").strip()
        clear()
        print("Augmented Matrix:")
        print_array(matrix)
        if choice == "1":
            solution, gauss_array = gauss_elimination(matrix, n)
            if isinstance(solution, list):
                print("\nSolution:")
                for i in range(n):
                    print(f'X{i+1} = {solution[i]:.2f}', end='\t')
                print("\n")
                choice = input("Would you like to continue the elimination process using Gauss-Jordan? (yes/no): ").strip().lower()
                if choice in ['yes', 'y']:
                    solution = gauss_jordan(gauss_array, n)
                    if solution:
                        print("\nFinal Solution:")
                        for i in range(n):
                            print(f'X{i+1} = {solution[i]:.2f}', end='\t')
                        print("\n")
            elif isinstance(solution, str):
                print(solution)
            choice = input("\nEnter Y to start over, N to exit.\n> ")
            if choice.lower() == "y":
                break
            else:
                print("Shutting down.")
                exit()
        elif choice == "2":
            det = getMatrixDeterminant(matrix, n)
            print(f"\nDeterminant: {det}")
            if det == 0:
                print("The system may have no unique solution or infinitely many solutions.")
            choice = input("Enter Y to start over, N to exit.\n> ")
            if choice.lower() == "y":
                break
            else:
                print("Shutting down.")
                exit()
        elif choice == "3":
            exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")