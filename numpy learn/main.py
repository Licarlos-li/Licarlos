import numpy as np
import pysnooper


@pysnooper.snoop(output='./debug.log')
def learn():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([1, 2, 3, 4, 5], ndmin=2)
    c = np.array([1, 2, 3], dtype=complex)
    dt = np.dtype('i4')
    print(a.shape)

    x = np.empty([3, 2], dtype=int)
    x = np.arange(10, 20, 2)

    a = np.arange(10)
    s = slice(2, 7, 2)
    print(a[s])

    x = np.array([[1, 2], [3, 4], [5, 6]])
    y = x[[0, 1, 2], [0, 1, 0]]
    print(y)

if __name__ == '__main__':
    learn()

