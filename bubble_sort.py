
def sort(nums):
    for i in range(0, len(nums), 1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


nums = [2, 53, 12, 4, 45, 76, 5, 6, 980, 1]
sort(nums)
print(nums)
