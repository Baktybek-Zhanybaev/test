import random
nums = []
for i in range(100):

    nums.append(random.randint(0, 1))
max_zero = 0
current_zeros = 0
print(nums)
for i in nums:
    if i == 0:
        current_zeros += 1
        if current_zeros > max_zero:
            max_zero = current_zeros
    else:
            current_zeros = 0
print(max_zero)
