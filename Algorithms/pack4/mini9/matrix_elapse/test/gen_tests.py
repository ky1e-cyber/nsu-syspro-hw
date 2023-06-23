import sys
import numpy as np

MAX_VALUE = 2 ** 10
MIN_VALUE = -(2 ** 10)

if __name__ == "__main__":
    size = int(sys.argv[1])
    samples = int(sys.argv[2])



    for i in range(samples):
        matrix1 = np.random.randint(
            low = MIN_VALUE, 
            high = MAX_VALUE, 
            size = (size, size)
        )
        matrix2 = np.random.randint(
            low = MIN_VALUE,
            high = MAX_VALUE, 
            size = (size, size)
        )

        product = matrix1 * matrix2

        np.savetxt(f"first_matrix_{i}", matrix1)
        np.savetxt(f"second_matrix_{i}", matrix2)
        np.savetxt(f"product_matrix_{i}", product)