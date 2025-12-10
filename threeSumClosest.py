def threeSumClosest(nums, target):
    nums.sort()
    closest = float('inf')

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if abs(total - target) < abs(closest - target):
                closest = total

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total

    return closest

# test
nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))  # output: 2
