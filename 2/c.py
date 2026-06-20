def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


print(is_sorted([1, 2, 3, 4]))
print(is_sorted([1, 3, 2, 4]))


def is_sorted(lst):
    return lst == sorted(lst)


print(is_sorted([1, 2, 3, 4]))
print(is_sorted([1, 3, 2, 4]))
