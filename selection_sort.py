def sel_sort(nums):
    for i in range(len(nums)-1,):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j

            nums[i], nums[minpos] = nums[minpos], nums[i]


nums = [3, 8, 4, 6, 7, 3, 1, 89, 34, 134, 106]

sel_sort(nums)

print(nums)
