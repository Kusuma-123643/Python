#Write a method to find the second largest number in an array
arr = list(map(int, input().split()))
if len(arr) < 2:
    print("No Second Largest")
else:
    largest = arr[0]
    second_largest = None
    for n in arr[1:]:
        if n > largest:
            second_largest = largest
            largest = n
        elif n != largest and (second_largest is None or n > second_largest):
            second_largest = n
    print("Second Largest:", second_largest if second_largest is not None else "No Second Largest")