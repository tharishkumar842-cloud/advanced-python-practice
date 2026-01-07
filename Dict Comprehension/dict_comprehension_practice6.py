nums = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 7
}
new_nums={k:v*v for k, v in nums.items() if v%2==0}
print(new_nums)