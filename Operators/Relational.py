# 5. Print the smaller and larger number
def find_smaller_larger(a, b):
    smaller = min(a, b)
    larger = max(a, b)
    return smaller, larger

val1, val2 = 15, 20
small, large = find_smaller_larger(val1, val2)
print("Smaller Number:", small)
print("Larger Number:", large)