def hamming(a, b):
    if len(a) != len(b):
        raise ValueError("Error.")

    result = 0
    for i in range(len(a)):
        if a[i - 1] != b[i - 1]:
            result = result + 1

    return result
