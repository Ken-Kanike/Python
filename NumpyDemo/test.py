# ==============================================================================
# Comprehensive NumPy Masterclass (NumpyDemo)
# ==============================================================================
import numpy as np

# 1. Random Number Generation (Original Code preserved & extended)
print("--- 1. Random Number Generation ---")
print("Random integer up to 10:", np.random.randint(10))

# Setting seed for reproducibility
np.random.seed(42)
print("Reproducible random float [0, 1):", np.random.rand())
print("Random integers (array of 5):   ", np.random.randint(1, 100, size=5))
print("Standard Normal Distribution:   ", np.random.normal(loc=0, scale=1, size=4))

# 2. Creating NumPy ndarrays
print("\n--- 2. Array Creation & Attributes ---")
arr_1d = np.array([10, 20, 30, 40, 50], dtype=np.int32)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)

print(f"1D Array: {arr_1d}, Shape: {arr_1d.shape}, Dtype: {arr_1d.dtype}")
print(f"2D Array:\n{arr_2d}\nDimensions: {arr_2d.ndim}, Total elements: {arr_2d.size}")

# Common generation routines
zeros_arr = np.zeros((2, 3))          # 2x3 matrix of 0.0
ones_arr = np.ones((2, 2))            # 2x2 matrix of 1.0
identity_arr = np.eye(3)              # 3x3 Identity matrix
ranged_arr = np.arange(0, 20, 5)      # [0, 5, 10, 15]
linear_spaced = np.linspace(0, 1, 5)  # 5 evenly spaced numbers from 0 to 1
print("Linspace (0 to 1 in 5 steps):", linear_spaced)

# 3. Indexing, Slicing & Boolean Filtering
print("\n--- 3. Indexing, Slicing & Boolean Masking ---")
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Element at row 1, col 2:", matrix[1, 2])     # 60
print("First two rows, columns 1 to end:\n", matrix[:2, 1:])

# Boolean Masking (Vectorized Filtering)
mask = matrix > 45
print("Elements greater than 45:", matrix[mask])

# 4. Vectorized Arithmetic & Broadcasting
print("\n--- 4. Vectorization & Broadcasting ---")
# Operations happen element-wise without explicit Python loops (Fast C-speed!)
vec_a = np.array([1, 2, 3])
vec_b = np.array([10, 20, 30])
print("Vector Addition:      ", vec_a + vec_b)
print("Scalar Multiplication:", vec_a * 5)
print("Element-wise Powers:  ", vec_a ** 2)

# Broadcasting: Expanding compatible dimensions automatically
matrix_3x3 = np.ones((3, 3))
row_vector = np.array([10, 20, 30])
broadcasted_sum = matrix_3x3 + row_vector  # row_vector broadcast across all 3 rows
print("Broadcasted Result:\n", broadcasted_sum)

# 5. Statistical & Aggregation Functions
print("\n--- 5. Statistical Functions ---")
data = np.array([12, 45, 67, 89, 23, 56, 78, 90])
print(f"Mean:      {np.mean(data):.2f}")
print(f"Median:    {np.median(data)}")
print(f"Std Dev:   {np.std(data):.2f}")
print(f"Variance:  {np.var(data):.2f}")
print(f"Max & Min: {np.max(data)} at index {np.argmax(data)}, {np.min(data)}")

# 6. Reshaping, Flattening & Stacking
print("\n--- 6. Reshaping & Stacking ---")
flat = np.arange(12)
reshaped_3x4 = flat.reshape((3, 4))
print("Reshaped (3x4):\n", reshaped_3x4)
print("Flattened back:", reshaped_3x4.flatten())

# Horizontal & Vertical Stacking
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Vertical Stack (vstack):\n", np.vstack((a, b)))
print("Horizontal Stack (hstack):", np.hstack((a, b)))

# 7. Linear Algebra Operations
print("\n--- 7. Linear Algebra (np.linalg) ---")
matrix_A = np.array([[2, 1], [5, 3]])
matrix_B = np.array([[1, 2], [3, 4]])

# Matrix Multiplication using '@' operator or np.matmul
dot_product = matrix_A @ matrix_B
print("Matrix Product (A @ B):\n", dot_product)

# Determinant and Inverse
det_A = np.linalg.det(matrix_A)
inv_A = np.linalg.inv(matrix_A)
print(f"Determinant of A: {det_A:.2f}")
print("Inverse of A:\n", inv_A)
# Verification: A @ inv_A == Identity
print("A @ Inv(A) (Identity matrix verification):\n", np.round(matrix_A @ inv_A))