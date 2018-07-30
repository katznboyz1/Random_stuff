nums = [1, 2, 3]
for _ in range(100):
	print (nums[0])
	nums[2] = nums[0] + nums[1]
	nums[0] = nums[1]
	nums[1] = nums[2]