
"""
Laboratory work No. 4
Task: 5 (NumPy, statistics, matrix operations)
Variant: 24
Description: In the matrix, swap the largest elements in the first and last columns.
             Calculate the correlation coefficient between the elements of the first
             and last columns. Round the result to hundredths.
             Demonstrate NumPy array creation, indexing, slicing, ufuncs,
             and statistical functions (mean, median, var, std, corrcoef).

Developer: Student
Date: 2026-05-14
Version: 1.0
"""

import numpy as np
import pandas as pd

def create_random_matrix(rows, cols, low = 0, high = 100):
    """
    Create a random integer matrix with given dimensions.
    Uses NumPy's random.randint.
    """
    lst = [0, 1, 2, 3, 4, 5]
    arr = np.array(lst)
    print(f"array is {arr}")
    df = pd.DataFrame({
        'A': [0, 1, 2],
        'B': [3, 4, 5]
    })
    print (f"Data Frame: \n{df}")
    arr = df.values
    print(f"Array from values: \n{arr}")
    
    return np.random.randint(low, high, size=(rows, cols))

def swap_max_in_columns(matrix: np.ndarray):
    """
    Swap the maximum elements of the first and last columns in-place.
    Returns the modified matrix.
    """
    if matrix.shape[1] < 2:
        raise ValueError("Matrix must have at least 2 columns to swap.")
    #find indices of maximum values in first and last columns
    col_first = matrix[:, 0]
    col_last = matrix[:, -1]
    idx_max_first = np.argmax(col_first)
    idx_max_last = np.argmax(col_last)
    #swap the values
    matrix[idx_max_first, 0], matrix[idx_max_last, -1] = matrix[idx_max_last, -1], matrix[idx_max_first, 0]
    return matrix

def correlation_first_last_columns(matrix: np.ndarray):
    """
    Compute Pearson correlation coefficient between first and last columns.
    Returns the correlation coefficient.
    """
    col_first = matrix[:, 0]
    col_last = matrix[:, -1]
    # np.corrcoef returns a 2x2 matrix, take the off-diagonal element
    corr_matrix = np.corrcoef(col_first, col_last)
    return corr_matrix[0, 1]

def demonstrate_numpy_operations(matrix: np.ndarray):
    """
    Demonstrate various NumPy operations: attributes, indexing, slicing, ufuncs,
    and statistical functions (mean, median, var, std).
    """
    print("\nNumPy Operations Demonstration ")
    print(f"Matrix shape: {matrix.shape}")
    print(f"Matrix size: {matrix.size}")
    print(f"Data type: {matrix.dtype}")
    print(f"Number of dimensions: {matrix.ndim}")
     
    #indexing and slicing
    print("\nIndexing and Slicing")
    print(f"First row: {matrix[0, :]}")
    print(f"Last column: {matrix[:, -1]}")
    print(f"Submatrix (first 2 rows, first 2 columns):\n{matrix[:2, :2]}")
    
    #universal functions (ufuncs)
    print("\nUniversal functions (ufuncs)")
    print(f"Square root of each element (first row): {np.sqrt(np.abs(matrix[0, :]))}")  # abs to avoid negative sqrt
    print(f"Element-wise sin (first column): {np.sin(matrix[:, 0])}")
    print(f"Element-wise > 50: {matrix > 50}")
    
    #  statistical functions
    print("\nStatistical Functions")
    print(f"Mean of all elements: {np.mean(matrix)}")
    print(f"Median of all elements: {np.median(matrix)}")
    print(f"Variance of all elements: {np.var(matrix)}")
    print(f"Standard deviation of all elements: {np.std(matrix)}")

def task5_run():
    """Main program: read matrix dimensions, create random matrix,
    perform swapping, compute correlation, demonstrate NumPy features.
    """
    while True:
        try:
            # egt matrix dimensions from user
            rows = int(input("Enter number of rows (n): "))
            cols = int(input("Enter number of columns (m): "))
            if rows <= 0 or cols <= 0:
                print("Rows and columns must be positive integers.")
                continue
            if cols < 2:
                print("For column swapping, matrix must have at least 2 columns.")
                continue
            
            #create random matrix
            print("\nGenerating random integer matrix...")
            matrix = create_random_matrix(rows, cols, low=1, high=100)  # positive ints
            print("Original matrix:")
            print(matrix)
            
            # demonstrate general NumPy operations
            demonstrate_numpy_operations(matrix)
            
            #swap max elements in first and last columns
            swapped_matrix = swap_max_in_columns(matrix.copy())  # use copy to keep original if needed
            print("\n=== After swapping maximum elements in first and last columns ===")
            print(swapped_matrix)
            
            #compute correlation coefficient between first and last columns
            corr = correlation_first_last_columns(swapped_matrix)
            print(f"\nCorrelation coefficient between first and last columns: {corr:.4f}")
            print(f"Rounded to hundredths: {corr:.2f}")
            
            #(Optional) additional check: show max values locations
            first_col = swapped_matrix[:, 0]
            last_col = swapped_matrix[:, -1]
            print(f"\nFirst column: {first_col}")
            print(f"Last column: {last_col}")
            print(f"Max of first column: {np.max(first_col)} at index {np.argmax(first_col)}")
            print(f"Max of last column: {np.max(last_col)} at index {np.argmax(last_col)}")
            
        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        
        # Repeat or exit
        again = input("\nDo you want to try another matrix? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting program.")
            break
