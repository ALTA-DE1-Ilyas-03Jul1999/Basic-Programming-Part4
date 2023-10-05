def mean_median(array_input):
    if not array_input:
        return None

    sorted_array = sorted(array_input)
    n = len(sorted_array)

    # Compute the mean
    mean = sum(sorted_array) / n

    # Compute the median
    if n % 2 == 0:  # If even
        median = (sorted_array[n//2 - 1] + sorted_array[n//2]) / 2.0
    else:  # If odd
        median = sorted_array[n//2]

    return (mean, median)

if __name__ == '__main__':
    print(mean_median([1, 2, 3, 4])) # (2.5, 2.5)
    print(mean_median([1, 2, 3, 4, 5])) # (3.0, 3)
    print(mean_median([7, 8, 9, 13, 15])) # (10.4, 9)
    print(mean_median([10, 20, 30, 40, 50])) # (30.0, 30)
    print(mean_median([15, 20, 30, 60, 120])) # (49.0, 30)