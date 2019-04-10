import numpy as np
import inspect


def main():
    basics()


def basics():
    a1 = np.array(
        [
            [0, 1, 2, 3],
            [10, 11, 12, 13],
            [20, 21, 22, 23]
        ]
    )

    a = np.array(
        [
            [1, 2],
            [3, 4],
            [5, 6]
        ]
    )
    # print(a[[0, 1, 2]])
    print(a[[0, 1, 0]])
    # print(a[[0, 1, 2], [0, 1, 0]])


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


if __name__ == '__main__':
    main()
