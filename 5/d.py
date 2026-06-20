def has_duplicates(lst):
    return len(lst) != len(set(lst))

print(has_duplicates([1, 2, 3, 4]))
print(has_duplicates([1, 2, 2, 3]))