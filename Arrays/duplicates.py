# 10. Write a function to find the duplicate values of an array
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)

arr_with_duplicates = [1, 2, 3, 2, 4, 5, 1]
print("Duplicate Values:", find_duplicates(arr_with_duplicates))