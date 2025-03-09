
# 15. Write a method to find the number of even numbers and odd numbers in an array
def count_even_odd(arr):
    even_count = sum(1 for num in arr if num % 2 == 0)
    odd_count = len(arr) - even_count
    return even_count, odd_count
arr={1,8,3,6,3,90}

print("Even and Odd Count:", count_even_odd(arr))
