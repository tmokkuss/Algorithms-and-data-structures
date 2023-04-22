nums = list(map(int, input().split()))

max_num = max(nums)

print("*" * (max_num + 1))

for i in range(max_num, 0, -1):
    row = ""
    for num in nums:
        if num >= i:
            row += "*"
        else:
            row += " "
    print("*" + row + "*")

