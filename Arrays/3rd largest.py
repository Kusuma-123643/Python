#Write a method to find the third largest number in an array
arr = list(map(int, input().split()))

if len(arr) < 3:
    print("No Third Largest")
else:
    largest = second_largest = third_largest = None

    for n in arr:
        if largest is None or n > largest:
            third_largest = second_largest
            second_largest = largest
            largest = n
        elif n != largest and (second_largest is None or n > second_largest):
            third_largest = second_largest
            second_largest = n
        elif n != largest and n != second_largest and (third_largest is None or n > third_largest):
            third_largest = n

    print("Third Largest:", third_largest if third_largest is not None else "No Third Largest")