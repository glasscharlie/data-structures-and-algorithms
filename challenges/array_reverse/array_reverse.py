list = [1, 4, 5, 6, 8]
otherlist = ["test", "test2", "test3", 4]


def reverse(array):
    for i in range(1, len(array)):
        tmp = array[i : (i + 1)]
        if i == len(array) - 1:
            array = tmp + array[:i]
        else:
            array = tmp + array[:i] + array[i + 1:]
    return array

print(reverse(list))


reverse(list)
reverse(otherlist)