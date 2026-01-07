nums = [10, 20, 30, 40, 50, 60]
new_list=[v*2 for v,i in enumerate(nums) if v%2==0]
print(new_list)