# Linear Equation Solver

A Python application for solving systems of linear equations using **Gaussian Elimination** and **Gauss–Jordan Elimination**. The program also computes matrix determinants, verifies row-echelon forms, and displays every row operation step-by-step, making it a useful educational tool for learning linear algebra.

## Features

- Solve systems of linear equations using **Gaussian Elimination**
- Continue to **Gauss–Jordan Elimination** to obtain Reduced Row Echelon Form (RREF)
- Calculate the determinant of a square matrix
- Detect and handle zero pivots through row swapping
- Verify whether an input matrix is in **Row Echelon Form (REF)** or **Reduced Row Echelon Form (RREF)**
- Input validation for matrix dimensions and coefficients
- Step-by-step visualization of every elementary row operation
- Detect singular matrices and report when a unique solution does not exist

## Technologies

- Python 3
- Python Standard Library (no external dependencies)

## Usage

1. Download the file.

2. Run the program.

```bash
python main.py
```
or simply run using Python directly from your file system.

3. Enter:
   - The number of unknowns.
   - The augmented matrix coefficients.
   - The desired operation:
     - Gaussian Elimination
     - Determinant Calculation

After Gaussian Elimination, you may optionally continue to Gauss–Jordan Elimination to compute the Reduced Row Echelon Form.

## Example

```text
Enter the number of unknowns (n):
> 3

R1 = 2 1 -1 8
R2 = -3 -1 2 -11
R3 = -2 1 2 -3
```

The program will display each row operation before presenting the final solution.

## Learning Objectives

This project demonstrates:

- Gaussian Elimination
- Gauss–Jordan Elimination
- Matrix determinants
- Elementary row operations
- Row Echelon Form (REF)
- Reduced Row Echelon Form (RREF)
- Basic numerical linear algebra concepts
