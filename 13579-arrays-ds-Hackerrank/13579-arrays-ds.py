def reverse_array(arr):
    return arr[::-1]
n = int(input())
arr = list(map(int, input().split()))
ans = reverse_array(arr)
print(*ans)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna