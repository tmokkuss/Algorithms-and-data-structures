def sort_array(nums):
    evens = sorted([num for num in nums if num % 2 == 0])
    odds = sorted([num for num in nums if num % 2 != 0], reverse=True)

    return evens + odds


nums = [9, 4, 2, 7, 5, 1, 8, 3, 6]
sorted_nums = sort_array(nums)
print(sorted_nums)