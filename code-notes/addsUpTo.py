nums = [0, 1, 2, 3, 4]
target = 0

def addsUpTo (nums, target):
    left = 0
    while left < len(nums)-1:
        r = left+1
        while r < len(nums):
            if nums[left]+nums[r] == target:
                return True
            r +=1
        left+=1

# don't add 'else' because it will cause to exit the inner loop. here, the else is implicit.
